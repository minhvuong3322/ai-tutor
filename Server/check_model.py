import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("Danh sách model khả dụng:")
try:
    for m in client.models.list():
        # Chỉ hiện các model có hỗ trợ tạo nội dung (generateContent)
        if "generateContent" in m.supported_actions:
            print(f"- {m.name}")
except Exception as e:
    print(f"Lỗi: {e}")