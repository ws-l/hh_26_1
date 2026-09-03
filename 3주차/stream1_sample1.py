#.py 파일
import streamlit as st
import pandas as pd
st.set_page_config(page_title="Multi Page", layout="wide")
def page_home():
    st.title("Home")
    st.subheader("현황")    
def data_upload():   
    uploaded_file = st.file_uploader(label="Select a file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state["df"] = df

pages = {"Home": page_home, "Data upload": data_upload}

st.sidebar.subheader("처리 선택")
choice = st.sidebar.selectbox("이동", list(pages.keys()))
pages[choice]()
