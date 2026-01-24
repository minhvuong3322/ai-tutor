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
    
    if not data:
        return jsonify({"error": "No data provided"}), 400

    user_input = data.get("message")
    session_id = data.get("session_id", "anonymous") # Nhận session_id từ Client, mặc định là anonymous

    if not user_input:
        return jsonify({"error": "Thiếu trường 'message'."}), 400

    bot_response = get_response(user_input, session_id)

    return jsonify({
        "user_input": user_input,
        "bot_response": bot_response,
        "session_id": session_id
    })

if __name__ == "__main__":
    print(f"API chạy tại http://{get_local_ip()}:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
