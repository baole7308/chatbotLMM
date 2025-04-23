from openai import OpenAI
from dotenv import load_dotenv
import os
import signal
import atexit
import requests
from PyPDF2 import PdfReader
import io
import re
class ChatBotApp:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = os.getenv("BASE_URL")
        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url)

    def stream_response(self,chat_history, user_input):
        messages = [{"role": "system", "content": "Bạn là một trợ lý thân thiện."}]
        for user, bot in chat_history:
            messages.append({"role": "user", "content": user})
            messages.append({"role": "assistant", "content": bot})
        messages.append({"role": "user", "content": user_input})

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            stream=True
        )

        full_response = ""
        for chunk in response:
            content = chunk.choices[0].delta.content or ""
            full_response += content
            yield full_response

    def summarize_article(self,url):
        response = requests.get(url)
        article_content = response.text[:4000]  

        messages = [
            {"role": "system", "content": "Bạn là một trợ lý AI có khả năng tóm tắt bài viết."},
            {"role": "user", "content": f"Tóm tắt bài viết sau: {article_content}"}
        ]

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return response.choices[0].message.content.strip()
    
    def is_url(text):
        url_pattern = re.compile(r'https?://\S+')
        return bool(url_pattern.match(text))
    
    def chat_interface(self, user_input, chat_history):
        if ChatBotApp.is_url(user_input):
            summary = self.summarize_article(user_input)
            chat_history.append((user_input, summary))
            yield "", chat_history
        else:
            bot_reply = ""
            for partial_reply in self.stream_response(chat_history, user_input):
                bot_reply = partial_reply
                yield "", chat_history + [(user_input, bot_reply)]
            
    def extract_text_from_pdf(self,pdf_bytes):
        pdf_stream = io.BytesIO(pdf_bytes)  
        reader = PdfReader(pdf_stream)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    def ask_pdf_question(self,pdf_file, user_question):
        content = self.extract_text_from_pdf(pdf_file)
        messages = [
            {"role": "system", "content": "Bạn là trợ lý AI có thể trả lời câu hỏi dựa trên nội dung file PDF."},
            {"role": "user", "content": f"Nội dung PDF:\n{content}\n\nCâu hỏi: {user_question}"}
        ]

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content.strip()

    def shutdown_gradio(self):
        os.kill(os.getpid(), signal.SIGINT)

    def launch(self):
        atexit.register(self.shutdown_gradio)

