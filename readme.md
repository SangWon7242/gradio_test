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
