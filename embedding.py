from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_hotel_bookings.csv")

df['date'] = pd.to_datetime(df['arrival_date_year'].astype(str) + '-' +
                            df['arrival_date_month'] + '-' +
                            df['arrival_date_day_of_month'].astype(str))

# Load sentence transformer model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

# Generate text data
df['text_data'] = df.apply(lambda row: f"Booking at {row['hotel']} on {row['date']}. Revenue: {row['adr']}", axis=1)

# Convert text data to embeddings
embeddings = model.encode(df['text_data'].tolist())

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Save index for future use
faiss.write_index(index, "faiss_index.bin")

print("✅ FAISS index created and saved.")
