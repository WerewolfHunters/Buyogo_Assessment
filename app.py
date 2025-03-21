# from flask import Flask, request, jsonify
# import matplotlib.pyplot as plt
# import io
# import base64
# from analysis import revenue_trends, cancellation_rate, top_booking_countries, lead_time_distribution
# from groq_qa import query_qa_system

# app = Flask(__name__)

# def plot_to_base64(fig):
#     """Helper function to convert a Matplotlib figure to base64."""
#     buf = io.BytesIO()
#     fig.savefig(buf, format='png')  # Save figure to buffer
#     buf.seek(0)
#     encoded_img = base64.b64encode(buf.getvalue()).decode('utf-8')
#     plt.close(fig)  # Close figure to free memory
#     return encoded_img

# @app.route('/ask', methods=['POST'])
# def ask_question():
#     """Answers booking-related questions."""
#     try:
#         data = request.get_json()
#         if not data or 'question' not in data:
#             return jsonify({"error": "Missing 'question' field"}), 400

#         answer = query_qa_system(data['question'])
#         return jsonify({"answer": answer})

#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# @app.route('/analytics', methods=['POST'])
# def get_analytics_report():
#     """Returns analytics reports based on requested type."""
#     try:
#         data = request.get_json()
#         if not data or 'report_type' not in data:
#             return jsonify({"error": "Missing 'report_type' field"}), 400

#         report_type = data['report_type']

#         if report_type == "revenue_trends":
#             fig = revenue_trends()
#             image_data = plot_to_base64(fig)
#             return jsonify({"report": "Revenue Trends Over Time", "image": image_data})

#         elif report_type == "cancellation_rate":
#             result = cancellation_rate()
#             return jsonify({"report": result})

#         elif report_type == "top_booking_countries":
#             fig = top_booking_countries()
#             image_data = plot_to_base64(fig)
#             return jsonify({"report": "Top 10 Booking Countries", "image": image_data})

#         elif report_type == "lead_time_distribution":
#             fig = lead_time_distribution()
#             image_data = plot_to_base64(fig)
#             return jsonify({"report": "Booking Lead Time Distribution", "image": image_data})

#         else:
#             return jsonify({"error": "Invalid report type"}), 400

#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True)


from flask import Flask, request, jsonify, send_file
import matplotlib.pyplot as plt
import io
from analysis import revenue_trends, cancellation_rate, top_booking_countries, lead_time_distribution
from groq_qa import query_qa_system

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    """Answers booking-related questions."""
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({"error": "Missing 'question' field"}), 400

        answer = query_qa_system(data['question'])
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/analytics', methods=['POST'])
def get_analytics_report():
    """Returns analytics reports based on requested type."""
    try:
        data = request.get_json()
        if not data or 'report_type' not in data:
            return jsonify({"error": "Missing 'report_type' field"}), 400

        report_type = data['report_type']
        fig = None  # Placeholder for Matplotlib figure

        if report_type == "revenue_trends":
            fig = revenue_trends()
        elif report_type == "top_booking_countries":
            fig = top_booking_countries()
        elif report_type == "lead_time_distribution":
            fig = lead_time_distribution()
        elif report_type == "cancellation_rate":
            result = cancellation_rate()
            return jsonify({"report": result})  # No image for cancellation rate
        else:
            return jsonify({"error": "Invalid report type"}), 400

        # Convert figure to image response
        img_io = io.BytesIO()
        fig.savefig(img_io, format='png')
        img_io.seek(0)
        plt.close(fig)  # Free memory

        return send_file(img_io, mimetype='image/png')  # Return as an image response

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
