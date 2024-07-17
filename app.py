from fastapi import FastAPI
import uvicorn
import gradio as gr

from api.interfaces import image_classes

app = FastAPI()

gr.mount_gradio_app(app, image_classes, path="/")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
