import streamlit as st
import time

st.title("title")
st.header("header")
st.subheader('subheader')
st.markdown("markdown")
st.caption("caption")
st.code("code")
st.latex("latex")

st.header("Cristiano ronaldo : ")
st.markdown("No 1 footballer in the world...")
st.image("download (2).jpg")

st.checkbox("yes")
st.button("Click")
st.radio("Pick your gender",['Male','Female'])

st.selectbox("Pick your gender",['Male','Female'])
st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune']) 
st.select_slider("pick a mark",['Bad','Good',"Excellent"])

st.slider("Pick a number",0,50)
st.number_input("pick a number",0,10)
st.text_input("Email address")

st.date_input("Travelling date")
st.time_input("School time")
st.text_area("Description")

st.file_uploader("upload a photo")
st.color_picker("choose your favourite color")

st.balloons()

st.subheader("Progress bar")
st.progress(50)

st.subheader("wait the execution")
with st.spinner("wait for it...."):
    time.sleep(10)

st.success("you did it!")
st.error("Error")
st.warning("Warning")
st.info("It's easy to build a streamlit app")
st.exception(RuntimeError('RuntimeError exception'))

st.sidebar.title("This is written inside the sidebar")
st.sidebar.button("click")
st.sidebar.radio("pick a gender : ",['Male','Female'])