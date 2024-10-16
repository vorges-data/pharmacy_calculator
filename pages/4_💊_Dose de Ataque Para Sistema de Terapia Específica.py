import streamlit as st
import math
from PIL import Image

image = Image.open('images/4bio.png')
st.sidebar.image(image, width=120)

# Função para limpar os inputs
def clear_inputs():
    st.session_state['medicamento_mg'] = 0
    st.session_state['quantidade_caixa'] = 0
    st.session_state['dose_ataque_1'] = 0
    st.session_state['dose_ataque_2'] = 0
    st.session_state['dose_ataque_3'] = 0
    st.session_state['dose_ataque_4'] = 0
    st.session_state['dose_ataque_5'] = 0
    st.session_state['dose_manutencao'] = 0
    st.session_state['intervalo_manutencao'] = 0

# Inicializar os valores no session_state, se ainda não estiverem definidos
if 'medicamento_mg' not in st.session_state:
    st.session_state['medicamento_mg'] = 0
if 'quantidade_caixa' not in st.session_state:
    st.session_state['quantidade_caixa'] = 0
if 'dose_ataque_1' not in st.session_state:
    st.session_state['dose_ataque_1'] = 0
if 'dose_ataque_2' not in st.session_state:
    st.session_state['dose_ataque_2'] = 0
if 'dose_ataque_3' not in st.session_state:
    st.session_state['dose_ataque_3'] = 0
if 'dose_ataque_4' not in st.session_state:
    st.session_state['dose_ataque_4'] = 0
if 'dose_ataque_5' not in st.session_state:
    st.session_state['dose_ataque_5'] = 0
if 'dose_manutencao' not in st.session_state:
    st.session_state['dose_manutencao'] = 0
if 'intervalo_manutencao' not in st.session_state:
    st.session_state['intervalo_manutencao'] = 0


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


# Título da aplicação
st.markdown("<h1 style='color:#007B45;'>Cálculo de Dose de Ataque para Sistema de Terapia Específica</h1>", unsafe_allow_html=True)

# Botão para limpar os inputs antes da criação dos widgets
if st.button("Limpar Inputs"):
    clear_inputs()

# Entradas do usuário (números inteiros)
medicamento_mg = st.number_input("Medicamento (em mg):", min_value=0, step=1, key="medicamento_mg")
quantidade_caixa = st.number_input("Quantidade por caixa (em unidades):", min_value=0, step=1, key="quantidade_caixa")
dose_ataque_1 = st.number_input("Dose Ataque 1 (em mg):", min_value=0, step=1, key="dose_ataque_1")
dose_ataque_2 = st.number_input("Dose Ataque 2 (em mg):", min_value=0, step=1, key="dose_ataque_2")
dose_ataque_3 = st.number_input("Dose Ataque 3 (em mg):", min_value=0, step=1, key="dose_ataque_3")
dose_ataque_4 = st.number_input("Dose Ataque 4 (em mg):", min_value=0, step=1, key="dose_ataque_4")
dose_ataque_5 = st.number_input("Dose Ataque 5 (em mg):", min_value=0, step=1, key="dose_ataque_5")

st.markdown("<h5 style='color:#007B45;'>Dose de Manutenção</h5>", unsafe_allow_html=True)
dose_manutencao = st.number_input("Dose Manutenção (em mg):", min_value=0, step=1, key="dose_manutencao")
intervalo_manutencao = st.number_input("Intervalo Manutenção (em dias):", min_value=0, step=1, key="intervalo_manutencao")

# Divisor e título "Resultado"
st.markdown("---") 
st.markdown("<h2 style='color:#007B45;'>Resultado</h2>", unsafe_allow_html=True)

# Cálculo das doses totais
ttl_medicamento_necessario = dose_ataque_1 + dose_ataque_2 + dose_ataque_3 + dose_ataque_4 + dose_ataque_5

# Cálculo do número de caixas necessárias
if ttl_medicamento_necessario > 0 and medicamento_mg > 0 and quantidade_caixa > 0:
    nro_caixas_necessarias = math.ceil(ttl_medicamento_necessario / (medicamento_mg * quantidade_caixa))
else:
    nro_caixas_necessarias = "???"

# Cálculo de caixas necessárias por envio
if dose_manutencao > 0 and intervalo_manutencao > 0 and medicamento_mg > 0 and quantidade_caixa > 0:
    caixas_por_envio = (30 / intervalo_manutencao) * dose_manutencao / medicamento_mg / quantidade_caixa
    caixas_por_envio = math.ceil(caixas_por_envio)
else:
    caixas_por_envio = "???"

# Título "Informações Para Dose De Ataque"
st.markdown("<h5 style='color:#007B45;'>Informações Para Dose De Ataque</h5>", unsafe_allow_html=True)
st.write(f"**TTL Medicamento Necessário (mg):** {ttl_medicamento_necessario}")
st.write(f"**Nro Caixas Necessárias:** {nro_caixas_necessarias}")

# Título "Informações Para Envio Mensal (30 Dias)"
st.markdown("<h5 style='color:#007B45;'>Informações Para Envio Mensal (30 Dias)</h5>", unsafe_allow_html=True)
st.write(f"**Caixas Necessárias por Envio:** {caixas_por_envio}")
