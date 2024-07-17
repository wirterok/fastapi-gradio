from fastapi import FastAPI
import gradio as gr

from .predictors import predict_image_classes

router = FastAPI()

image_classes = gr.Interface(
    predict_image_classes,
    inputs=[
        gr.Image(type="pil", label="Upload an image:")
    ],
    outputs="text",
    title="LLM App",
)