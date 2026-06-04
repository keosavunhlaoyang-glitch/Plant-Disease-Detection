import torch
import torch.nn as nn
import json
from torchvision import models

model = None
classes = None


def build_model(num_classes):

    model = models.resnet18(weights=None)

    model.fc = nn.Sequential(
        nn.Dropout(0.3),
        nn.Linear(model.fc.in_features, num_classes)
    )

    return model


def load_model():

    global model, classes

    if model is not None:
        return model, classes

    # 📌 load classes
    with open("checkpoints/classes.json", "r", encoding="utf-8") as f:
        raw = json.load(f)

    # ✅ FIX: support both list & dict
    if isinstance(raw, dict):
        classes = [raw[str(i)] for i in range(len(raw))]
    else:
        classes = raw

    model = build_model(len(classes))

    state = torch.load(
        "checkpoints/resnet18_web.pth",
        map_location="cpu"
    )

    # 🔥 FIX: remove "module." prefix if exists
    new_state = {}
    for k, v in state.items():
        new_key = k.replace("module.", "")
        new_state[new_key] = v

    model.load_state_dict(new_state, strict=True)

    model.eval()

    return model, classes