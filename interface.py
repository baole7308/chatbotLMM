import gradio as gr

def create_ui(bot):
    with gr.Blocks(title="Streaming ChatBot") as demo:
        with gr.Tab("ChatBot"):
            chatbot = gr.Chatbot(label="Output")
            user_input = gr.Textbox(label="Input")
            send_button = gr.Button("Send")

            send_button.click(bot.chat_interface, inputs=[user_input, chatbot], outputs=[user_input, chatbot])
            user_input.submit(bot.chat_interface, inputs=[user_input, chatbot], outputs=[user_input, chatbot])

        with gr.Tab("PDF"):
            pdf_input = gr.File(label="Upload PDF", type="binary")
            pdf_question = gr.Textbox(label="Input")
            pdf_answer = gr.Textbox(label="Output", interactive=False)
            ask_button = gr.Button("Send")

            ask_button.click(bot.ask_pdf_question, inputs=[pdf_input, pdf_question], outputs=[pdf_answer])
            pdf_question.submit(bot.ask_pdf_question, inputs=[pdf_input, pdf_question], outputs=[pdf_answer])

    return demo
