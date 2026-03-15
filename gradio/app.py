import gradio as gr

def to_gray(img):
  filtpxs = []
  for r,g,b in img.getdata():
    l = (r + g + b) // 3
    filtpxs.append((l, l, l))
  img.putdata(filtpxs)
  return img

my_inputs = [
  gr.Image(type="pil", show_label=False),
]

my_outputs = [
  gr.Image(type="pil", show_label=False)
]

with gr.Blocks() as demo:
  gr.Interface(
    fn=to_gray,
    inputs=my_inputs,
    outputs=my_outputs,
    flagging_mode="never",
    fill_width=True
  )

if __name__ == "__main__":
   demo.launch()
