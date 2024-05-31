# gradio 사용법

## 설치

```
pip install gradio
```

## 데모코드

```py
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
```

## 실행

```
1. ctrl + F5
2. python app.py # 디렉토리 이동해서 실행
```

# Interface 핵심

```
1. fn: 사용자 인터페이스(UI)를 둘러싸는 함수
2. inputs: 입력에 사용할 Gradio 구성요소. 구성 요소 수는 함수의 인수 수와 일치해야 한다.
3. outputs: 출력에 사용할 Gradio 구성요소. 구성 요소 수는 함수의 반환 값 수와 일치해 한다.
```

# 데모용 URL 생성

```py
demo.launch(share=True) # `share=True` 데모용 URL 생성

# 사용시 데모 URL이 생성되어 다른 사람과 공유가 가능!
```

# 빠르게 개발하는 모드로 전환

- [참고자료](https://www.gradio.app/guides/developing-faster-with-reload-mode)

```
# 명령어
gradio run.py
```

# 개발 모드로 전환하기 위한 코드 작성

## ChatInterface 데모 코드 구현

```py
demo = gr.ChatInterface(
    yes_man,
    chatbot=gr.Chatbot(height=300),
    textbox=gr.Textbox(placeholder="Ask me a yes or no question", container=False, scale=7),
    title="Yes Man",
    description="Ask Yes Man any question",
    theme="soft",
    examples=["파이썬이란?", "객체지향 프로그래밍이란?", "프로그래밍 공부는 어떻게 해야하는가?"],
    cache_examples=True,
    retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
)

if __name__ == "__main__":
    demo.launch()
```

# 랭체인을 사용하기 위해 설치 모듈

```
pip install langchain openai
pip install langchain_community
pip install -U langchain-community
```

# 챗봇을 위한 준비 코드

```py
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
import openai
import gradio as gr
import os

os.environ["OPENAI_API_KEY"] = "sk-..."  # Replace with your key

llm = ChatOpenAI(temperature=1.0, model='gpt-3.5-turbo-0613')

def response(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))
    gpt_response = llm(history_langchain_format)
    return gpt_response.content
```
