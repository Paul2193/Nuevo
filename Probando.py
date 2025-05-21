import streamlit as st
import matplotlib.pyplot as plt
st.title("Mi primera pagina")
st.header("hola")
st.text("probando probando")
st.text("probando probando1111")

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Título
st.title("Boxplot Simple en Streamlit")

# Datos generados aleatoriamente o definidos
datos = [7, 15, 13, 17, 19, 21, 25, 30, 22, 18]

# Crear figura
fig, ax = plt.subplots()
ax.boxplot(datos)
ax.set_title("Diagrama de Caja (Boxplot)")
ax.set_ylabel("Valores")
ax.grid(True)

# Mostrar en Streamlit
st.pyplot(fig)

