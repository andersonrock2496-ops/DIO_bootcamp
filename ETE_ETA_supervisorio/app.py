import streamlit as st
import pandas as pd
import random
from datetime import datetime
import matplotlib.pyplot as plt

st.title("💧 Supervisório ETA/ETE")

def gerar_dados():
    return {
        "Hora": datetime.now().strftime("%H:%M:%S"),
        "pH": round(random.uniform(6, 9), 2),
        "Turbidez": round(random.uniform(1, 15), 2),
        "Nivel": round(random.uniform(30, 100), 2),
    }

dados = [gerar_dados() for _ in range(20)]

df = pd.DataFrame(dados)

st.dataframe(df)

fig, ax = plt.subplots()

ax.plot(df["pH"])

st.pyplot(fig)