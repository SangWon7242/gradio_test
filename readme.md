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
