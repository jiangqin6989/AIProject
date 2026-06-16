"""Gradio demo: enter a name and display a greeting in a web page."""

import gradio as gr


def greet(name):
    """Return a greeting for the supplied name."""
    name = (name or "").strip()
    return f"Hello, {name or 'World'}!"


def create_app():
    """Create and configure the Gradio interface."""
    return gr.Interface(
        fn=greet,
        inputs=gr.Textbox(
            label="输入",
            placeholder="请输入你的名字",
        ),
        outputs=gr.Textbox(label="输出"),
        title="Hello World",
        description="输入名字并点击提交，查看程序输出。",
        examples=[["Python"], ["Gradio"]],
    )


def main():
    """Start the local Gradio web application."""
    app = create_app()
    app.launch(inbrowser=True)


if __name__ == "__main__":
    main()
