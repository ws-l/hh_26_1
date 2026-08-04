from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/predict")
def predict(x: float, y: float):
    return {
        "x": x,
        "y": y,
        "result": x + y
    }

import pandas as pd
df = pd.read_csv("creditset2.csv")

@app.get("/data")
def data():
    return df.sample(100).to_dict(orient="records")