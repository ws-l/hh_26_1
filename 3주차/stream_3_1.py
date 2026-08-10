#.py 파일
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Multi Page", layout="wide")

def page_home():
    st.title("Home")
    st.subheader("현황")    

#upload
def data_upload():   
    uploaded_file = st.file_uploader(label="Select a file", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(10))
        st.session_state["df"] = df #다른 함수에서도 접근 가능하도록 세션 지정
        st.success("데이터 저장 완료")

#explore
def data_eda():  
    tmp_df = st.session_state["df"]
    g = sns.pairplot(data=tmp_df )
    st.pyplot(g.figure)  

def data_eda2():  
    tmp_df = st.session_state["df"]
    fig, ax = plt.subplots()
    sns.heatmap(data=tmp_df.corr() )
    st.pyplot(fig)  

pages = {
    "Home": page_home,
    "Data upload": data_upload,
    "EDA1": data_eda,
    "EDA2": data_eda2,    
}

st.sidebar.subheader("처리 선택")
choice = st.sidebar.selectbox("이동", list(pages.keys()))
pages[choice]()
