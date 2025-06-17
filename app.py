import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.title("Análisis de vehículos en venta")

# Intentar cargar el archivo CSV
try:
    car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
    st.success("Datos cargados correctamente.")
except FileNotFoundError:
    st.error("❌ El archivo 'vehicles_us.csv' no se encontró. Asegúrate de subirlo al repositorio.")
    st.stop()  # Detener ejecución si el archivo no existe

# Botón para construir histograma
hist_button = st.button('Construir histograma')

# Si se hace clic en el botón
if hist_button:
    st.write("📊 Creación de un histograma para el conjunto de datos de anuncios de venta de coches")

    # Crear y mostrar el histograma
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


