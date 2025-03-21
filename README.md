# Booking Analytics & Q&A API

This project provides an API for booking analytics and Q&A responses using Flask.  
It includes functionalities for:
- Generating analytics reports (revenue trends, cancellation rates, booking countries, lead times).
- Answering booking-related questions using a Q&A system.
- Evaluating API performance (response accuracy & speed).
- Embedding-based search for efficient retrieval.

## 🚀 Features
- **Flask API** for analytics and Q&A.
- **Matplotlib** for generating charts in analytics.
- **Q&A System** for handling booking-related queries.
- **Performance Evaluation** for response accuracy & speed.

---

## 📂 **Project Structure**
```
📦 booking-analytics-qa
 ┣ 📁 Data                 # Directory that stores data
  ┣ 📜 hotel_bookings.csv               # The main data
 ┣ ⚙️ .env                 # File containing your api keys
 ┣ 📜 app.py               # Main Flask application
 ┣ 📜 analysis.py          # Generates analytics reports
 ┣ 📜 groq_qa.py           # Q&A system logic
 ┣ 📜 embedding.py         # Embedding-based search
 ┣ 📜 performance.py       # Evaluates API performance
 ┣ 📜 requirements.txt     # Required dependencies
 ┣ 📜 README.md            # Project documentation
```

---

## 🔧 **Setup & Installation**
### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/your-username/booking-analytics-qa.git
cd booking-analytics-qa
```

### 2️⃣ **Create a Virtual Environment (Recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🏃 **Running the Application**
### 1️⃣ **Start the Flask API**
```bash
python app.py
```
- The API will run at `http://127.0.0.1:8000`

### 2️⃣ **Run Performance Evaluation**
```bash
python performance.py
```
- Evaluates **response accuracy & speed** of the Q&A system.

---

## 🔥 **API Endpoints**
### **📌 1. Question-Answering API**
- **Endpoint:** `POST /ask`
- **Description:** Answers booking-related questions.
- **Request Example:**
```json
{
  "question": "What is the cancellation policy?"
}
```
- **Response Example:**
```json
{
  "answer": "The cancellation policy depends on your booking type..."
}
```

### **📌 2. Analytics Reports API**
- **Endpoint:** `POST /analytics`
- **Request Example:**
```json
{
  "report_type": "revenue_trends"
}
```
- **Response Example:**
```json
{
  "report": "Revenue Trends Over Time",
  "image": "base64_encoded_image_string"
}
```
🚀 **View Image**: Decode base64 using Python:
```python
import base64
with open("output.png", "wb") as file:
    file.write(base64.b64decode("base64_encoded_image_string"))
```

---

## 🛠 **Code Explanation**
### 📌 `app.py`
- Main Flask app to handle API requests.

### 📌 `analysis.py`
- Generates **matplotlib-based analytics reports**.

### 📌 `groq_qa.py`
- Implements **Q&A system logic**.

### 📌 `embedding.py`
- Embedding-based search for improved **question matching**.

### 📌 `performance.py`
- Evaluates **API response accuracy & speed**.

---

## 🤝 **Contributing**
1. **Fork the repository**  
2. **Create a new branch**  
3. **Make your changes**  
4. **Submit a Pull Request**  

---

## 🔗 **License**
This project is licensed under the **MIT License**.

---
### 🎯 **Now you're all set! Happy Coding! 🚀**

