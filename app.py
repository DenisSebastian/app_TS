import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.title("Series de NDVI")
st.markdown("##### Visualización inicial datos de prueba")


col1, col2 = st.columns(2)

with col1:
    # Selección de Bases
    base_select = st.selectbox(
        label = "Seleccione Base",
        options = ["disturbed", "non_disturbed"])

# Generación path
wd = os.getcwd()
file_name = str(base_select + "_df.csv")
files_csv = "data/csv"
fullname = os.path.join(wd,files_csv , file_name)


# Lectura de Base
df = pd.read_csv(fullname)
#df = df.set_index("date")

with col2:
    # Selector de Serie
    serie_filter = st.selectbox("Seleccionar Serie", pd.unique(df["serie"]))



title_plot = str("Time Series NDVI serie "+serie_filter)
df_serie = df.loc[(df.serie == serie_filter)]



# checkbox para remove NA values de la serie
checkbox_na = st.checkbox("Remove NA", value = True)
if checkbox_na:
    newdf = df_serie.dropna()
else:
    newdf = df_serie

# Generación de Visualización
width = 750
height = 550

fig = px.line(newdf, x='date', y='ndvi', title=title_plot
        #,width = width, height= height
)

fig.update_traces(line_color='#02818a', line_width=1)
#fig.update_layout(
#    plot_bgcolor='white'
#)

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

# Descipción de la APP

st.subheader("Descipción:")
st.write("Corresponde a registros del promedio NDVI (Landsat 8) de parcelas bosque esclerofilo de la zona Central de Chile, por un periodo desde 2000-01-03 a 2022-04-29")

st.latex(r'''
NDVI = \frac{NIR-RED}{NIR+RED}
     ''')

st.image("images/descp_ndvi.jpeg")
st.markdown("**Autor:** [denis.berroeta@uai.cl](denis.berroeta@uai.cl)")
