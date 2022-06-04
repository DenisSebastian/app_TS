import streamlit as st
import pandas as pd
import os

wd = os.getcwd()
file_name = "disturbed_df.csv"

fullname = os.path.join(wd, file_name)

st.title("APP VO")
st.subheader("Visualización de datos")

st.write("""
Serie de tiempo de NDVI
""")

df = pd.read_csv(fullname)
#df.iloc[:, 2:4].dropna()
st.line_chart(df.iloc[:, 2:4].dropna())
