# 💬 Streaming Chatbot with OpenAI, Flask & Gradio

Ứng dụng Chat Bot với khả năng **phản hồi dạng streaming** sử dụng OpenAI SDK. Backend được xây dựng bằng Flask và giao diện đơn giản bằng Gradio.

---

## 🚀 Tính năng

- 🤖 Chat GPT hỗ trợ streaming phản hồi
- 🔐 Sử dụng API Key từ OpenAI
- 🌐 Giao diện đơn giản bằng Gradio
- ⚡ Kết nối Flask backend và Gradio frontend

---

## 🛠️ Công nghệ sử dụng

- Python 3.x
- Flask
- OpenAI SDK
- Gradio

---

## 📦 Cài đặt

### 1. Clone project

```bash
git clone https://github.com/yourusername/streaming-chatbot.git
cd streaming-chatbot
```

### 2. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

> `requirements.txt` bao gồm:
>
> ```
> openai
> flask
> gradio
> requests
> ```

### 3. Cấu hình API Key

Tạo file `.env` (hoặc chỉnh trực tiếp trong code):

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Trong file Python, cấu hình như sau:

```python
import os
openai.api_key = os.getenv("OPENAI_API_KEY")
```

---

## ▶️ Chạy ứng dụng

### Bước 1: Chạy backend Flask

```bash
python app.py
```

### Bước 2: Chạy frontend Gradio

```bash
python gradio_app.py
```

---

## 📺 Demo Giao Diện

![Chatbot Screenshot](![Alt text](image.png)) _(bạn có thể chụp ảnh màn hình và đổi tên)_

---

## 📂 Cấu trúc thư mục

```
streaming-chatbot/
├── app.py             # Flask backend
├── gradio_app.py      # Giao diện Gradio
├── requirements.txt   # Các thư viện cần thiết
├── README.md          # Tài liệu này
└── .env               # Chứa API Key (không commit lên GitHub)
```

---

## 📜 Giấy phép

MIT License © 2025 Bảo

---

## 📬 Liên hệ

- Email: your_email@example.com
- GitHub: [@yourusername](https://github.com/yourusername)
