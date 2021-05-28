import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

df = pd.read_csv("iris.csv", sep=",")

st.title("Willkommen auf diesem Example Dashboard")
st.subheader("Analysiere den Iris Datensatz")
st.write(f"Form des Datensatzes: {df.shape}")

st.sidebar.title("Wähle dein Variablen aus")
a = st.sidebar.selectbox("Variable A", list(df.columns)[0:4])
b = st.sidebar.selectbox("Variable B", list(df.columns)[0:4], index=1)
kmeans_slider = st.sidebar.slider(
    "Wähle die Anzahl der Centroids", min_value=2, max_value=8
)
if a == b:
    st.sidebar.warning("Variablen sollten nicht identisch sein")


df["cluster"] = KMeans(n_clusters=kmeans_slider, random_state=0).fit_predict(
    df.loc[:, (a, b)]
)
groupsize = df.groupby("cluster").size().reset_index().rename({0: "size"}, axis=1)
# st.write(groupsize)

col1, col2 = st.beta_columns(2)

fig = plt.figure()
plt.scatter(x=a, y=b, c="cluster", data=df)
col1.pyplot(fig)

for index, row in groupsize.iterrows():
    col2.markdown(
        f'Anzahl in Gruppe <strong>{row["cluster"]}</strong>: <strong>{row["size"]}</strong>.',
        unsafe_allow_html=True,
    )
