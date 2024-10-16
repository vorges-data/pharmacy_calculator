import streamlit as st
from datetime import datetime, timedelta
from PIL import Image

image = Image.open('images/4bio.png')
st.sidebar.image(image, width=120)

# Função para limpar os inputs
def clear_inputs():
    st.session_state['quantidade_medicamento'] = 0
    st.session_state['data_inicial'] = datetime.today()
    st.session_state['periodo'] = 0

# Inicializar os valores no session_state, se ainda não estiverem definidos
if 'quantidade_medicamento' not in st.session_state:
    st.session_state['quantidade_medicamento'] = 0
if 'data_inicial' not in st.session_state:
    st.session_state['data_inicial'] = datetime.today()
if 'periodo' not in st.session_state:
    st.session_state['periodo'] = 0

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
st.markdown("<h1 style='color:#007B45;'>Calculadora de Datas</h1>", unsafe_allow_html=True)

# Botão para limpar os inputs antes da criação dos widgets
if st.button("Limpar Inputs"):
    clear_inputs()

# Entrada do usuário
quantidade_medicamento = st.number_input("Quantidade de medicamento com o paciente (em dias):", min_value=0, step=1, key="quantidade_medicamento")
data_inicial = st.date_input("Data Inicial", key="data_inicial")  # Removido 'value' para evitar o aviso

# Exibe a data selecionada logo abaixo da entrada de Data Inicial
st.markdown(f"<p style='font-size:15px; color:#007B45; margin-top:-8px;'>Data Inicial Selecionada: <strong>{st.session_state['data_inicial'].strftime('%d/%m/%Y')}</strong></p>", unsafe_allow_html=True)

# Entrada do período
periodo = st.number_input("Período (em dias):", min_value=0, step=1, key="periodo")

# Divisor e título "Resultado"
st.markdown("---")  # Adiciona uma linha divisória
st.markdown("<h2 style='color:#007B45;'>Resultado</h2>", unsafe_allow_html=True)

# Lógica para calcular a data "Possui medicamento até?"
if quantidade_medicamento and periodo:
    possui_medicamento_ate = st.session_state['data_inicial'] + timedelta(days=(periodo + quantidade_medicamento))
else:
    possui_medicamento_ate = None

# Lógica para calcular a data "Programar para"
if periodo and possui_medicamento_ate:
    programar_para = possui_medicamento_ate - timedelta(days=periodo)
else:
    programar_para = None

# Exibe os resultados formatados no padrão dd/mm/yyyy com estilização
st.markdown(f"<p style='font-size:15px; color:black;'>Possui medicamento até: <strong>{possui_medicamento_ate.strftime('%d/%m/%Y') if possui_medicamento_ate else '???'}</strong></p>", unsafe_allow_html=True)

st.markdown(f"<p style='font-size:15px; color:black;'>Programar para: <strong>{programar_para.strftime('%d/%m/%Y') if programar_para else '???'}</strong></p>", unsafe_allow_html=True)
