from fastapi import FastAPI
import pandas as pd
import joblib

app = FastAPI()
pipe = joblib.load("pp.joblib")
df = pd.read_csv("data.csv")
df = pd.DataFrame( pipe.fit_transform(df) )

@app.get("/data")
def data():
    return df.sample(1).to_dict(orient="records")  

@app.get("/health")
def health():
    return {"status":"ok"}

@app.get("/cal")
def cal(x: int, y:int):    
    return {"x":x, "y":y, "sum":x+y}
