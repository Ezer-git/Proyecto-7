import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")
# encabezado
st.header("Exploración de Datos de Vehículos en EE. UU")

# botón para generar histograma
if st.checkbox("Mostrar histograma de odómetro"):
    fig = px.histogram(car_data, x="odometer")
    st.write("Histograma del odómetro de los vehículos")
    st.plotly_chart(fig)

# botón para generar gráfico de dispersión
if st.checkbox("Mostrar gráfico de dispersión precio vs. odómetro"):
    fig = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
    st.write("Gráfico de dispersión entre odómetro y precio")
    st.plotly_chart(fig)