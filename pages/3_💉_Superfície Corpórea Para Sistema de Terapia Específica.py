import streamlit as st
import math
from PIL import Image

image = Image.open('images/4bio.png')
st.sidebar.image(image, width=120)

# Função para limpar os inputs
def clear_inputs():
    st.session_state.peso = 0
    st.session_state.altura = 0
    st.session_state.dose = 0

# Inicializar os valores no session_state, se ainda não estiverem definidos
if 'peso' not in st.session_state:
    st.session_state.peso = 0
if 'altura' not in st.session_state:
    st.session_state.altura = 0
if 'dose' not in st.session_state:
    st.session_state.dose = 0

# Aplicando estilo ao botão "Limpar Inputs"
st.markdown("""
    <style>
    div.stButton > button {
        background-color: white;
        color: black;
        border: 1px solid #d9d9d9;
    }
    div.stButton > button:hover {
        background-color: white;
        border: 1px solid #BBD760;
        color: #007B45;
    }
    </style>
    """, unsafe_allow_html=True)


# Título da aplicação com cor personalizada
st.markdown("<h1 style='color:#007B45;'>Cálculo de Superfície Corpórea para Sistema de Terapia Específica</h1>", unsafe_allow_html=True)

# Botão para limpar os inputs antes da criação dos widgets
if st.button("Limpar Inputs"):
    clear_inputs()

# Entradas do usuário (números inteiros)
peso = st.number_input("Peso (em kg):", min_value=0, step=1, key="peso")
altura = st.number_input("Altura (em cm):", min_value=0, step=1, key="altura")
dose = st.number_input("Dose (em m²):", min_value=0.0, step=0.01, key="dose")

# Divisor e título "Resultado"
st.markdown("---")  # Adiciona uma linha divisória
st.markdown("<h2 style='color:#007B45;'>Resultado</h2>", unsafe_allow_html=True)

# Cálculo da Superfície Corpórea (m²) com arredondamento para 2 casas decimais
if peso > 0 and altura > 0:
    superficie_corporea = 0.007184 * (peso ** 0.425) * (altura ** 0.725)
    superficie_corporea = math.ceil(superficie_corporea * 100) / 100  # Arredonda para 2 casas decimais
else:
    superficie_corporea = "???"

# Cálculo da Dose em mg com arredondamento para inteiro
if isinstance(superficie_corporea, float) and superficie_corporea > 0 and dose > 0:
    dose_em_mg = superficie_corporea * dose
    dose_em_mg = math.ceil(dose_em_mg)  # Arredonda para cima
else:
    dose_em_mg = "???"

# Exibindo os resultados
st.write(f"**Superfície Corpórea (m²):** {superficie_corporea}")
st.write(f"**Dose em mg:** {dose_em_mg}")
