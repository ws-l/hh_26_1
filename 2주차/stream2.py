import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("API 연결 예제")

df = pd.read_json("http://localhost:8000/image")

img = df.drop(columns="label")
img2 = Image.fromarray(img.values.reshape(14, 14,3).astype(np.uint8))

if st.button("확인"):
    st.image(img2)