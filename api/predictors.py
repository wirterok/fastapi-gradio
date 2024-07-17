from transformers import AutoImageProcessor, AutoModelForImageClassification
from .validators import ValidateImageType
from PIL import Image

preprocessor = AutoImageProcessor.from_pretrained("google/mobilenet_v2_1.0_224")
model = AutoModelForImageClassification.from_pretrained("google/mobilenet_v2_1.0_224")

def predict_image_classes(image):
    inputs = preprocessor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    return model.config.id2label[predicted_class_idx]