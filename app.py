import streamlit as st
import pandas as pd

df = pd.read_csv("iris.csv", sep=",")

header = st.beta_container()
sidebar = st.beta_container()
main = st.beta_container()

with header:
    st.title("Willkommen auf diesem Example Dashboard")
    st.subheader("Analysiere den Iris Datensatz")

with sidebar:
    st.sidebar.title("Wähle dein Variablen aus")
    a = st.sidebar.selectbox("Variable A", list(df.columns)[0:4])
    b = st.sidebar.selectbox("Variable B", list(df.columns)[0:4], index=1)
    if a == b:
        st.sidebar.error('Variablen dürfen nicht identisch sein')

st.dataframe(df.head(10))

st.write(df)
