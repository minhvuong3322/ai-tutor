import json
import os
from dotenv import load_dotenv
from google import genai  # <-- Import thư viện mới

# --- CẤU HÌNH ---
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("Chưa cấu hình GOOGLE_API_KEY trong file .env")

# Khởi tạo Client mới
client = genai.Client(api_key=API_KEY)

# --- CHUẨN BỊ DỮ LIỆU (KIẾN THỨC CHO AI) ---
def load_knowledge_base():
    try:
        base_path = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(base_path, "rules.json")
        
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            knowledge_text = "Dưới đây là thông tin về Trường Đại học Giao thông Vận tải TP.HCM (UTH):\n"
            for item in data:
                knowledge_text += f"- {item['response']}\n"
            return knowledge_text
    except Exception as e:
        print(f"Lỗi đọc rules.json: {e}")
        return ""

uth_info = load_knowledge_base()

# --- HÀM XỬ LÝ CHÍNH ---
def get_response(user_input):
    try:
        prompt = f"""
        Bạn là Chatbot tư vấn tuyển sinh và hỗ trợ sinh viên của Trường Đại học Giao thông Vận tải TP.HCM (UTH).
        
        Hãy sử dụng thông tin dưới đây để trả lời câu hỏi:
        ---
        {uth_info}
        ---
        
        Yêu cầu:
        1. Trả lời ngắn gọn, thân thiện, xưng hô là "mình" và "bạn".
        2. Chỉ trả lời dựa trên thông tin được cung cấp. Nếu không có thông tin, hãy nói "Hiện tại mình chưa có thông tin về vấn đề này, bạn vui lòng liên hệ Phòng Đào tạo nhé."
        3. Sử dụng emoji phù hợp.

        Câu hỏi của người dùng: {user_input}
        """
        
        # Gọi API theo cú pháp mới của google-genai
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=prompt
        )
        
        # Trả về text (nếu có lỗi attribute, dùng response.text)
        return response.text.strip()

    except Exception as e:
        print(f"Lỗi API: {str(e)}") # In lỗi ra terminal để dễ debug
        return f"Xin lỗi, hệ thống đang bảo trì một chút. (Lỗi: {str(e)})"

# --- TEST TRỰC TIẾP ---
if __name__ == "__main__":
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() in ["thoát", "exit", "quit"]:
            break
        print("UTHBot:", get_response(user_input))