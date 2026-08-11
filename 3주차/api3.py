#.py 파일 
from fastapi import FastAPI
import pandas as pd
import numpy as np

app = FastAPI()

df = pd.read_csv("creditset2.csv")

@app.get("/data")
def date_gen():
    return  df.sample(1).to_dict(orient="records")
