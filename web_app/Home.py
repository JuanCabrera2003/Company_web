import streamlit as st
import pandas
import lorem

st.set_page_config(layout="wide")

st.title("The best Company")

text = lorem.paragraph()
st.write(text)

st.header("Our Team")

col1, col2, col3 = st.columns([1.5,1.5,1.5])

#usamos pandas para ingresar a la informacion
data = pandas.read_csv("data.csv", sep=",")

with col1:
    for index, row in data[0:4].iterrows():
        full_name = (row["first name"] + " " + row["last name"]).title()
        st.subheader(full_name)
        st.write(row["role"])
        st.image("images/" + row["image"])


with col2:
    for index, row in data[4:8].iterrows():
        full_name = (row["first name"] + " " + row["last name"]).title()
        st.subheader(full_name)
        st.write(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in data[8:12].iterrows():
        full_name = (row["first name"] + " " + row["last name"]).title()
        st.subheader(full_name)
        st.write(row["role"])
        st.image("images/" + row["image"])
    
