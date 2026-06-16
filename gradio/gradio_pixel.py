"""Gradio demo: apply common visual effects to an uploaded image."""

import gradio as gr
from PIL import Image, ImageOps


def pixelate(image, block_size):
    """Return a pixelated copy of the uploaded image."""
    width, height = image.size
    block_size = max(1, int(block_size))

    small_size = (
        max(1, width // block_size),
        max(1, height // block_size),
    )
    small_image = image.resize(small_size, Image.Resampling.BILINEAR)
    return small_image.resize((width, height), Image.Resampling.NEAREST)


def process_image(image, effect, block_size, threshold):
    """Apply the selected effect to an uploaded image."""
    if image is None:
        return None

    image = ImageOps.exif_transpose(image).convert("RGB")

    if effect == "像素化":
        return pixelate(image, block_size)
    if effect == "灰度化":
        return ImageOps.grayscale(image)
    if effect == "黑白化":
        gray_image = ImageOps.grayscale(image)
        threshold = int(threshold)
        return gray_image.point(lambda value: 255 if value >= threshold else 0)
    if effect == "反色":
        return ImageOps.invert(image)

    return image.copy()


def create_app():
    """Create the image processing interface."""
    return gr.Interface(
        fn=process_image,
        inputs=[
            gr.Image(type="pil", label="导入图片"),
            gr.Radio(
                choices=["原图", "像素化", "灰度化", "黑白化", "反色"],
                value="像素化",
                label="处理方式",
            ),
            gr.Slider(
                minimum=2,
                maximum=64,
                value=12,
                step=1,
                label="像素块大小",
            ),
            gr.Slider(
                minimum=0,
                maximum=255,
                value=128,
                step=1,
                label="黑白阈值",
            ),
        ],
        outputs=gr.Image(type="pil", format="png", label="处理结果"),
        title="图片处理",
        description="上传图片，选择处理方式并调整参数，然后点击提交。",
        allow_flagging="never",
    )


def main():
    """Start the local Gradio web application."""
    app = create_app()
    app.launch(inbrowser=True)


if __name__ == "__main__":
    main()
