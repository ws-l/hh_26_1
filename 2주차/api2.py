from fastapi import FastAPI
import pandas as pd
df = pd.read_csv("binary.csv")

app = FastAPI()
@app.get("/data")
def data(row:int):
    return df.sample(row).to_dict(orient="records")