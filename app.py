import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Análisis de Datos de Vehículos Usados")
st.header("Explora los gráficos interactivos para entender mejor los datos")
st.subheader("Este proyecto permite analizar el mercado de vehículos usados en Estados Unidos mediante gráficos interactivos.")

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if st.button('Construir gráfico de dispersión'):  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="price", y="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
