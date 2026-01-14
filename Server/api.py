from flask import Flask, request, jsonify
from chatbot import get_response  # Gọi hàm từ chatbot.py
import socket

app = Flask(__name__)

# Hàm lấy địa chỉ IP cục bộ
def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

# Endpoint test IP
@app.route("/get-ip", methods=["GET"])
def get_ip():
    return jsonify({"server_ip": get_local_ip()})

# Endpoint nhận input từ client → gọi chatbot.py → trả kết quả
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Thiếu trường 'message'."}), 400

    user_input = data["message"]
    bot_response = get_response(user_input)

    return jsonify({
        "user_input": user_input,
        "bot_response": bot_response
    })

if __name__ == "__main__":
    print(f"API chạy tại http://{get_local_ip()}:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
