from langchain_community.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("PUBLIC_SERVICE_KEY")  # Replace with your key

llm = ChatOpenAI(temperature=1.0, model='gpt-3.5-turbo-0613')

def response(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm(history_langchain_format)
    return gpt_response.content
  
custom_css = """
@font-face {
  font-family: 'GmarketSansMedium';
  src: url('https://fastly.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
  font-weight: normal;
  font-style: normal;
}

.gradio-container {
  font-family: 'GmarketSansMedium' !important;
}
"""  

demo = gr.ChatInterface(
    fn=response,
    chatbot=gr.Chatbot(height=600), # 챗봇의 높이
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
    title="Chat GPT를 이용한 챗봇",
    description="Ask Yes Man any question",
    theme="soft",
    examples=["파이썬이란?", "객체지향 프로그래밍이란?", "프로그래밍 공부는 어떻게 해야하는가?"],
    cache_examples=True,
    retry_btn="다시 보내기",
    undo_btn="이전 챗 삭제",
    clear_btn="전체 삭제",
    css=custom_css
)

if __name__ == "__main__":
    demo.launch()