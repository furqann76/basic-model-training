from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

app = FastAPI()
w, b = np.load("model.npy")

class Input(BaseModel):
    x: float

@app.post("/predict/")
def predict(data: Input):
    y = w * data.x + b
    return {"x": data.x, "y_predicted": y}
