import streamlit as st
from datetime import datetime, timedelta

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

# Título da aplicação
st.title("Calculadora de Datas")

# Botão para limpar os inputs antes da criação dos widgets
if st.button("Limpar Inputs"):
    clear_inputs()

# Entrada do usuário
quantidade_medicamento = st.number_input("Quantidade de medicamento com o paciente (em dias):", min_value=0, step=1, key="quantidade_medicamento")
data_inicial = st.date_input("Data Inicial", value=st.session_state['data_inicial'], key="data_inicial")  # Mantém o formato padrão no input

# Exibe a data selecionada logo abaixo da entrada de Data Inicial
st.markdown(f"<p style='font-size:15px; color: #f9f9f9; margin-top:-08px;'>Data Inicial Selecionada: <strong>{data_inicial.strftime('%d/%m/%Y')}</strong></p>", unsafe_allow_html=True)

# Entrada do período
periodo = st.number_input("Período (em dias):", min_value=0, step=1, key="periodo")

# Divisor e título "Resultado"
st.markdown("---")  # Adiciona uma linha divisória
st.subheader("Resultado")

# Lógica para calcular a data "Possui medicamento até?"
if quantidade_medicamento and periodo:
    possui_medicamento_ate = data_inicial + timedelta(days=(periodo + quantidade_medicamento))
else:
    possui_medicamento_ate = None

# Lógica para calcular a data "Programar para"
if periodo and possui_medicamento_ate:
    programar_para = possui_medicamento_ate - timedelta(days=periodo)
else:
    programar_para = None

# Exibe os resultados formatados no padrão dd/mm/yyyy com estilização
if possui_medicamento_ate:
    st.markdown(f"<p style='font-size:15px; color: #f9f9f9;'>Possui medicamento até: <strong>{possui_medicamento_ate.strftime('%d/%m/%Y')}</strong></p>", unsafe_allow_html=True)

if programar_para:
    st.markdown(f"<p style='font-size:15px; color: #f9f9f9;'>Programar para: <strong>{programar_para.strftime('%d/%m/%Y')}</strong></p>", unsafe_allow_html=True)
