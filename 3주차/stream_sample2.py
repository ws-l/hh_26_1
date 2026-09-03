#.py 파일
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Multi Page", layout="wide")

def page_home():
    st.title("Home")
    st.subheader("현황")    

#data_upload를 수정해서...
#업로드된 파이프 적용된 결과를 앞의 5줄을 화면에출력
#업로드된 데이터프레임에 시각화 적용....

import joblib
pipe = joblib.load("pipe.joblib")

#upload
def data_upload():   
    uploaded_file = st.file_uploader(label="Select a file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        #pipe.fit_transform(df)
        st.session_state["df"] = df
        st.write(df.head(10))

#API이름의 기능을 추가하셔서, api호출한 결과를 화면에 출력해보세요.
#10초마다 리프레시해서 가져온 api 결과 값을 db에 저장해보세요.
#from datetime import datetime
from sqlalchemy import create_engine
eng=create_engine('postgresql+psycopg2://postgres:12345@localhost:5432/postgres')
@st.fragment(run_every="10s")  #refresh
def API():
    tmp = pd.read_json("http://localhost:8000/data")
    st.write(tmp)
    tmp.to_sql("st333", eng, schema="public", if_exists="append", index=False    )
    st.success("DB good")
#    st.write(datetime.now().strftime("%Y%m%d-%H%M%S"))

#explore
def data_eda():  
    tmp_df = st.session_state["df"]
    g = sns.pairplot(data=tmp_df )
    st.pyplot(g.figure)  

pages = {"API":API,
    "Home": page_home,
    "Data upload": data_upload,
    "EDA":data_eda,
}

st.sidebar.subheader("처리 선택")
choice = st.sidebar.selectbox("이동", list(pages.keys()))
pages[choice]()
