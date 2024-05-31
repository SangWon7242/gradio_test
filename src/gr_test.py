import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
  fn=greet,
  inputs="textbox",
  outputs="textbox"
)

demo.launch(share=True) # 데모용 URL 생성