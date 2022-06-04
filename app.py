import streamlit as st
import pandas as pd
import os
import plotly.express as px


wd = os.getcwd()
file_name = "disturbed_df.csv"
files_csv = "data/csv"
fullname = os.path.join(wd,files_csv , file_name)

st.title("NDVI")
st.subheader("Visualización de Inicial datos de Prueba")

#st.write("""
#Serie de tiempo de NDVI
#""")

df = pd.read_csv(fullname)
#df = df.set_index("date")
serie_filter = "f_000"

serie_filter = st.selectbox("Seleccionar Serie", pd.unique(df["serie"]))
title_plot = str("Time Series NDVI serie "+serie_filter)
newdf = df.loc[(df.serie == serie_filter)].dropna()


width = 800
height = 600

fig = px.line(newdf, x='date', y='ndvi', title=title_plot, width = width, height= height)
fig.update_xaxes(rangeslider_visible=True,
     rangeselector=dict(
        buttons=list([
            dict(count=6, label="6 meses", step="month", stepmode="backward"),
            dict(count=1, label="1 año", step="year", stepmode="todate"),
            dict(count=2, label="2 años", step="year", stepmode="backward"),
            dict(count=5, label="5 años", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
st.plotly_chart(fig, use_container_width=False)

#st.line_chart(newdf.iloc[:, 2])
