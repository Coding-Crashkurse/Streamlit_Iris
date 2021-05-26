import streamlit as st
import pandas as pd

df = pd.read_csv("iris.csv", sep=",")

st.write(df)
