import streamlit as st

st.title("기본 UI 예제")

name = st.text_input("이름을 입력하세요")
age = st.slider("나이", 0, 100, 25)

if st.button("확인"):
    st.write(f"이름: {name}, 나이: {age}")