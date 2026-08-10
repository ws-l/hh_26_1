import streamlit as st
import pandas as pd
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import set_config

set_config(transform_output="pandas", display="diagram")

st.set_page_config(page_title="Pipeline Demo", layout="wide")


# ------------------------------------------------------------
# 파이프라인 로드 (미리 학습해서 joblib으로 저장해둔 것)
# ------------------------------------------------------------
@st.cache_resource
def load_pipeline():
    return joblib.load("pipe.joblib")


pipeline = load_pipeline()


# ------------------------------------------------------------
# 페이지 함수들
# ------------------------------------------------------------
def page_home():
    st.title("Home")
    st.subheader("현황")
    if "df" in st.session_state:
        st.write("업로드된 원본 데이터")
        st.dataframe(st.session_state["df"].head())
    if "result" in st.session_state:
        st.write("파이프라인 적용 결과")
        st.dataframe(st.session_state["result"].head())


def data_upload():
    st.title("CSV 업로드")
    uploaded_file = st.file_uploader("creditApprovalUCI.csv 파일을 선택하세요", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write(df.head(10))
        st.session_state["df"] = df  # 다른 함수에서도 접근 가능하도록 세션 지정
        st.success("데이터 저장 완료")


def apply_pipeline():
    st.title("파이프라인 적용")
    if "df" not in st.session_state:
        st.info("먼저 'Data upload' 페이지에서 CSV를 올려주세요.")
        return

    df = st.session_state["df"]
    st.write("적용 대상 데이터")
    st.dataframe(df.head())

    if st.button("파이프라인 적용"):
        result = pipeline.fit_transform(df)
        st.session_state["result"] = result
        st.success("파이프라인 적용 완료! 'EDA' 페이지에서 확인하세요.")

    if "result" in st.session_state:
        st.write("처리 결과 미리보기")
        st.dataframe(st.session_state["result"].head(20))


def data_eda():
    st.title("EDA1 - Pairplot")
    if "result" not in st.session_state:
        st.info("먼저 '파이프라인 적용' 페이지에서 결과를 만들어주세요.")
        return

    tmp_df = st.session_state["result"]
    g = sns.pairplot(data=tmp_df)
    st.pyplot(g.fig)


def data_eda2():
    st.title("EDA2 - Jointplot")
    if "result" not in st.session_state:
        st.info("먼저 '파이프라인 적용' 페이지에서 결과를 만들어주세요.")
        return

    tmp_df = st.session_state["result"]
    numeric_cols = tmp_df.select_dtypes(include="number").columns.tolist()

    col1, col2 = st.columns(2)
    with col1:
        x_col = st.selectbox("X축 컬럼", numeric_cols, index=0)
    with col2:
        y_col = st.selectbox("Y축 컬럼", numeric_cols, index=1)

    g = sns.jointplot(data=tmp_df, x=x_col, y=y_col, kind="scatter")
    st.pyplot(g.figure)


def data_eda3():
    st.title("EDA3 - Heatmap")
    if "result" not in st.session_state:
        st.info("먼저 '파이프라인 적용' 페이지에서 결과를 만들어주세요.")
        return

    tmp_df = st.session_state["result"]
    numeric_df = tmp_df.select_dtypes(include="number")

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(data=numeric_df.corr(), annot=False, ax=ax)
    st.pyplot(fig)


# ------------------------------------------------------------
# 사이드바: 페이지 선택
# ------------------------------------------------------------
pages = {
    "Home": page_home,
    "Data upload": data_upload,
    "파이프라인 적용": apply_pipeline,
    "EDA1 (Pairplot)": data_eda,
    "EDA2 (Jointplot)": data_eda2,
    "EDA3 (Heatmap)": data_eda3,
}

st.sidebar.subheader("처리 선택")
choice = st.sidebar.selectbox("이동", list(pages.keys()))
pages[choice]()