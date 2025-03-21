import faiss
import numpy as np
import pandas as pd
import os
from sentence_transformers import SentenceTransformer
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# Load cleaned dataset
df = pd.read_csv("data/cleaned_hotel_bookings.csv")

df['date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' +
                            df['arrival_date_month'] + '-' +
                            df['arrival_date_day_of_month'].astype(str))

# Generate text data
df['text_data'] = df.apply(lambda row: f"Booking at {row['hotel']} on {row['date']}. Revenue: {row['adr']}", axis=1)

# Load FAISS index
index = faiss.read_index("faiss_index.bin")

# Load sentence transformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Initialize Groq's LLM
chat_model = ChatGroq(model_name="llama-3.3-70b-versatile", groq_api_key=groq_api_key)

def query_qa_system(question):
    """Retrieves relevant texts and queries Groq's LLM."""
    question_embedding = model.encode([question])
    
    # Retrieve most relevant texts
    _, I = index.search(np.array(question_embedding, dtype=np.float32), 5)
    retrieved_texts = [df['text_data'][i] for i in I[0] if i < len(df)] if I.size > 0 else []
    
    context = " ".join(retrieved_texts) if retrieved_texts else "No relevant data found."
    
    prompt = f"""
    You are an AI assistant answering queries based on hotel booking data.
    
    Context: {context}
    
    Question: {question}

    Answer:
    """
    
    response = chat_model.invoke([HumanMessage(content=prompt)])
    return response.content

if __name__ == "__main__":
    print(query_qa_system("What is the total revenue for July 2017?"))
