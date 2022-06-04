import streamlit as st
import pandas as pd
import os

st.title("NDVI")
st.subheader("Visualización de Inicial datos")

st.write("""
Serie de tiempo de NDVI
""")

wd = os.getcwd()
file_name = "disturbed_df.csv"

fullname = os.path.join(wd, file_name)


df = pd.read_csv(fullname)
df = df.set_index("date")

newdf = df.loc[(df.serie == "f_000")].dropna()
st.line_chart(newdf.iloc[:, 2])
