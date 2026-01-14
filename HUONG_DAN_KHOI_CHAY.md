# Hướng dẫn khởi chạy dự án Simple Rule Chatbot

Dự án này bao gồm 2 phần:
- **Server**: Flask API (Python) chạy trên port 5000
- **Client**: Ứng dụng Electron (JavaScript/HTML)

## Cách 1: Chạy thủ công (Khuyến nghị)

### Bước 1: Cài đặt dependencies cho Server
```bash
cd Server
pip install -r requirements.txt
```

**Lưu ý trên Windows:** Nếu gặp lỗi `ModuleNotFoundError`, hãy thử dùng Python launcher:
```powershell
cd Server
py -m pip install -r requirements.txt
```

### Bước 2: Cài đặt dependencies cho Client
```bash
cd Client
npm install
```

### Bước 3: Khởi động Server
Mở một terminal và chạy:
```bash
cd Server
python api.py
```

**Lưu ý trên Windows:** Nếu lệnh `python` không hoạt động, hãy dùng:
```powershell
cd Server
py api.py
```

Server sẽ chạy tại `http://0.0.0.0:5000`

### Bước 4: Khởi động Client
Mở một terminal mới và chạy:
```bash
cd Client
npm start
```
hoặc
```bash
npm run dev
```

## Cách 2: Sử dụng launcher C++ (Tự động)

Nếu bạn muốn tự động khởi động cả server và client cùng lúc:

### Bước 1: Compile file main.cpp
```bash
g++ main.cpp -o launcher.exe
```

### Bước 2: Chạy launcher
```bash
launcher.exe
```

Launcher sẽ tự động:
1. Khởi động Flask server
2. Đợi 3 giây
3. Khởi động Electron app

## Lưu ý

- Đảm bảo bạn đã cài đặt:
  - Python 3.x
  - Node.js và npm
  - Electron (sẽ được cài tự động khi chạy `npm install`)
  
- Server phải chạy trước khi mở Client
- Nếu gặp lỗi port 5000 đã được sử dụng, hãy đóng ứng dụng đang dùng port đó hoặc thay đổi port trong `Server/api.py`

