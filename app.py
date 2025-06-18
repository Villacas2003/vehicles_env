import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la app
st.title("Análisis de vehículos en venta")

# Intentar cargar el archivo CSV
try:
    car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
    st.success("✅ Datos cargados correctamente.")
except FileNotFoundError:
    st.error("❌ El archivo 'vehicles_us.csv' no se encontró. Asegúrate de subirlo al repositorio.")
    st.stop()  # Detener ejecución si el archivo no existe

# Botón para construir histograma
if st.button('Mostrar histograma del odómetro'):
    st.write('📊 Histograma del odómetro de los vehículos')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para mostrar gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión (año vs precio)'):
    st.write('🔍 Gráfico de dispersión entre el año del modelo y el precio')
    if "model_year" in car_data.columns and "price" in car_data.columns:
        fig_scatter = px.scatter(car_data, x="model_year", y="price",
                                 title="Precio vs Año del Vehículo",
                                 labels={"model_year": "Año del modelo", "price": "Precio (USD)"})
        st.plotly_chart(fig_scatter, use_container_width=True)
    else:
        st.warning("Las columnas necesarias no existen en los datos.")



