import streamlit as st
import matplotlib.pyplot as plt
st.title("Mi primera pagina")
st.header("hola")
st.text("probando probando")
st.text("probando probando1111")


import matplotlib.pyplot as plt

# Datos de ejemplo
datos = [7, 15, 13, 17, 19, 21, 25, 30, 22, 18]

# Crear el boxplot
plt.boxplot(datos)
plt.title("Boxplot simple")
plt.ylabel("Valores")
plt.grid(True)
plt.show()

