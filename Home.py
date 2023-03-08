import streamlit as st
import pandas
st.set_page_config()
col1, col2 = st.columns(2)

with col1:
    st.image("photo.png", width = 350 )

with col2:
    st.title("Welcome to my programming projects portfolio")
    st.info("In some ways, programming is like painting. You start with a blank canvas and certain basic raw materials. You use a combination of science, art, and craft to determine what to do with them. - Andrew Hunt")

st.write("Below you can find some of the apps I have built in Python. Feel free to contact me!")

col3, empty_col,col4, = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep = ";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.write(f"[Demo]({row['demo']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"])
        st.write(f"[Source Code]({row['url']})")
        st.write(f"[Demo]({row['demo']})")

