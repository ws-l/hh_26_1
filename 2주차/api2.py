from fastapi import FastAPI
import pandas as pd
import pickle
df = pd.read_csv("binary.csv")

with open("test.pkl", "rb") as f:
    saved = pickle.load(f)
arr = saved["pipe1"].fit_transform(df) #pipeline
df = pd.DataFrame(arr, columns = df.columns)

app = FastAPI()
@app.get("/data")
def data(row:int):
    return df.sample(row).to_dict(orient="records")