from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io

from core.model import load_model
from core.preprocess import preprocess
from core.inference import predict
from utils.disease_info import get_info

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def home():
    with open("templates/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):

    image = Image.open(io.BytesIO(await file.read())).convert("RGB")

    model, classes = load_model()

    img = preprocess(image)

    conf, pred = predict(model, img)

    label = classes[pred]

    if conf < 0.4:
        label = "ບໍ່ຮູ້ຈັກ"

    info = get_info(label)

    return {
    "class_lo": info["lo"],
    "confidence": conf
}