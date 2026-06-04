import torch

def predict(model, img):

    with torch.no_grad():
        outputs = model(img)
        probs = torch.softmax(outputs, dim=1)

        conf, pred = torch.max(probs, 1)

    return conf.item(), pred.item()