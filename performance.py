import time
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample test questions and expected answers (modify these as needed)
TEST_QUESTIONS = [
    "What is the cancellation policy?",
    "How can I check my booking status?",
    "What are the top booking countries?",
    "How do I get a refund?"
]

EXPECTED_ANSWERS = [
    "The cancellation policy depends on your booking type. Some are refundable, while others are non-refundable.",
    "You can check your booking status by logging into your account and navigating to the bookings section.",
    "The top booking countries include USA, UK, and Germany, based on recent trends.",
    "To get a refund, visit our refund page and submit a request. Processing takes 3-5 business days."
]

API_URL = "http://127.0.0.1:8000/ask"  # Adjust if using a different endpoint


def get_api_response(question):
    """Sends a question to the API and returns the response along with time taken."""
    start_time = time.time()
    response = requests.post(API_URL, json={"question": question})
    end_time = time.time()
    
    response_time = round((end_time - start_time) * 1000, 2)  # Convert to milliseconds
    if response.status_code == 200:
        return response.json().get("answer", ""), response_time
    return "", response_time


def calculate_accuracy(predicted_answers, expected_answers):
    """Uses TF-IDF and Cosine Similarity to evaluate answer accuracy."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(predicted_answers + expected_answers)

    similarities = []
    for i in range(len(predicted_answers)):
        similarity = cosine_similarity(
            tfidf_matrix[i], tfidf_matrix[len(predicted_answers) + i]
        )[0][0]
        similarities.append(similarity)

    return round(sum(similarities) / len(similarities) * 100, 2)  # Convert to percentage


def evaluate_performance():
    """Runs performance tests and prints results."""
    predicted_answers = []
    response_times = []

    print("Evaluating API Performance...\n")

    for i, question in enumerate(TEST_QUESTIONS):
        answer, time_taken = get_api_response(question)
        predicted_answers.append(answer)
        response_times.append(time_taken)

        print(f"Question: {question}")
        print(f"Expected Answer: {EXPECTED_ANSWERS[i]}")
        print(f"Predicted Answer: {answer}")
        print(f"Response Time: {time_taken} ms\n")

    accuracy = calculate_accuracy(predicted_answers, EXPECTED_ANSWERS)
    avg_response_time = round(sum(response_times) / len(response_times), 2)

    print("---- Performance Report ----")
    print(f"Accuracy: {accuracy}%")
    print(f"Average Response Time: {avg_response_time} ms")


if __name__ == "__main__":
    evaluate_performance()
