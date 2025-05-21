import streamlit as st
import matplotlib.pyplot as plt
st.title("Mi primera pagina")
st.header("hola")
st.text("probando probando")
st.text("probando probando1111")


# Título de la app
st.title("Gráfica Simple con Matplotlib y Streamlit")

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Crear la figura y los ejes
fig, ax = plt.subplots()
ax.plot(x, y, marker='o', linestyle='-', label='Datos de ejemplo')

# Personalización
ax.set_title('Gráfica de Línea Simple')
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.grid(True)
ax.legend()

# Mostrar la gráfica en Streamlit
st.pyplot(fig)
