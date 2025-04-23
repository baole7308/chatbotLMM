from chatbot import ChatBotApp
from interface import create_ui

if __name__ == "__main__":
    bot = ChatBotApp()
    demo = create_ui(bot)
    demo.launch()