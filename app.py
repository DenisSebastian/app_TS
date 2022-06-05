import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.title("Series de NDVI")
st.subheader("Visualización de Inicial datos de Prueba")

# Selección de Bases
base_select = st.selectbox(
    label = "Seleccione Base",
    options = ["disturbed", "non_disturbed"])

wd = os.getcwd()
file_name = str(base_select + "_df.csv")
files_csv = "data/csv"
fullname = os.path.join(wd,files_csv , file_name)


#st.write("""
#Serie de tiempo de NDVI
#""")

df = pd.read_csv(fullname)
#df = df.set_index("date")
serie_filter = "f_000"


serie_filter = st.selectbox("Seleccionar Serie", pd.unique(df["serie"]))
title_plot = str("Time Series NDVI serie "+serie_filter)
df_serie = df.loc[(df.serie == serie_filter)]

checkbox_na = st.checkbox("Remove NA", value = True)

if checkbox_na:
    newdf = df_serie.dropna()
else:
    newdf = df_serie

width = 800
height = 550

fig = px.line(newdf, x='date', y='ndvi', title=title_plot,
        width = width, height= height)

fig.update_xaxes(rangeslider_visible=True,
     rangeselector=dict(
        buttons=list([
            dict(count=6, label="6 meses", step="month", stepmode="backward"),
            dict(count=1, label="1 año", step="year", stepmode="backward"),
            dict(count=2, label="2 años", step="year", stepmode="backward"),
            dict(count=5, label="5 años", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
st.plotly_chart(fig, use_container_width=False)

#st.line_chart(newdf.iloc[:, 2])
st.subheader("Descipción:")
st.write("Corresponde a registros del promedio NDVI (Landsat 8) de parcelas bosque esclerofilo de la zona Central de Chile, por un periodo desde 2000-01-03 a 2022-04-29")

st.latex(r'''
NDVI = \frac{NIR-RED}{NIR+RED}
     ''')
st.markdown("**Autor:** [denis.berroeta@uai.cl](denis.berroeta@uai.cl)")
