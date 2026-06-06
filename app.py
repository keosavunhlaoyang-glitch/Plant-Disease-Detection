import gradio as gr
import torch
from torchvision import transforms
from PIL import Image

# load model
model = torch.load("model.pth", map_location="cpu")
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

def predict(image):
    img = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(img)
        pred = torch.argmax(output, 1).item()

    return f"Class: {pred}"

interface = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Plant Disease AI"
)

interface.launch()