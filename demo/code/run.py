import gradio as gr
import os
from time import sleep


css_file = os.path.join(os.path.dirname(__file__), "file.css")


def set_lang(language):
    print(language)
    return gr.Code.update(language=language)


def set_lang_from_path():
    sleep(1)
    return gr.Code.update((css_file, ), language="css")


def code(language, code):
    return gr.Code.update(code, language=language)


io = gr.Interface(lambda x: x, "code", "code")

with gr.Blocks() as demo:
    lang = gr.Dropdown(value="python", choices=gr.Code.languages)
    with gr.Row():
        code_in = gr.Code(language="python", label="Input")
        code_out = gr.Code(label="Ouput")
    btn = gr.Button("Run")
    btn_two = gr.Button("Load File")

    lang.change(set_lang, inputs=lang, outputs=code_in)
    btn.click(code, inputs=[lang, code_in], outputs=code_out)
    btn_two.click(set_lang_from_path, inputs=None, outputs=code_out)
    io.render()

if __name__ == "__main__":
    demo.launch()
