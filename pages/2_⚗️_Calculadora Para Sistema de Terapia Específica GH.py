import streamlit as st
import math
from PIL import Image

image = Image.open('images/4bio.png')
st.sidebar.image(image, width=120)

# Função para limpar os inputs
def clear_inputs():
    st.session_state['dias_uso'] = 0
    st.session_state['dosagem_por_dia'] = 0
    st.session_state['concentracao'] = 0
    st.session_state['tempo_autorizacao'] = 0

# Inicializar os valores no session_state, se ainda não estiverem definidos
if 'dias_uso' not in st.session_state:
    st.session_state['dias_uso'] = 0
if 'dosagem_por_dia' not in st.session_state:
    st.session_state['dosagem_por_dia'] = 0
if 'concentracao' not in st.session_state:
    st.session_state['concentracao'] = 0
if 'tempo_autorizacao' not in st.session_state:
    st.session_state['tempo_autorizacao'] = 0


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
st.markdown("<h1 style='color:#007B45;'>Calculadora para Sistema de Terapia Específica GH</h1>", unsafe_allow_html=True)

# Botão para limpar os inputs antes da criação dos widgets
if st.button("Limpar Inputs"):
    clear_inputs()

# Entrada do usuário
dias_uso = st.number_input("Dias de Uso (em dias):", min_value=0, step=1, key="dias_uso")
dosagem_por_dia = st.number_input("Dosagem por dia (em mg):", min_value=0, step=1, key="dosagem_por_dia")
concentracao = st.number_input("Concentração (em mg):", min_value=0, step=1, key="concentracao")
tempo_autorizacao = st.number_input("Tempo de Autorização (em dias):", min_value=0, step=1, key="tempo_autorizacao")

# Função para calcular o número de caixas por envio
def calcular_qtd_caixas(dosagem_por_dia, dias_uso, concentracao):
    if concentracao > 0:
        return math.ceil((dosagem_por_dia * dias_uso) / concentracao)
    return "???"

# Função para calcular o número total de envios
def calcular_total_envios(tempo_autorizacao, cada_caixa_atendera):
    if isinstance(cada_caixa_atendera, (int, float)) and cada_caixa_atendera > 0:
        return math.ceil(tempo_autorizacao / cada_caixa_atendera)
    return "???"

# Função para calcular quantos dias cada caixa atenderá
def calcular_dias_por_caixa(qtd_caixas, concentracao, dosagem_por_dia):
    if concentracao > 0 and dosagem_por_dia > 0:
        return math.floor((qtd_caixas * concentracao) / dosagem_por_dia)
    return "???"

# Calcular "QTDDE CAIXAS POR ENVIO"
qtd_caixas = calcular_qtd_caixas(dosagem_por_dia, dias_uso, concentracao)

# Calcular "CADA CAIXA ATENDERÁ POR"
dias_por_caixa = calcular_dias_por_caixa(qtd_caixas, concentracao, dosagem_por_dia)

# Calcular "QTDDE TOTAL DE ENVIOS"
total_envios = calcular_total_envios(tempo_autorizacao, dias_por_caixa)

# Exibindo os resultados
st.markdown("<h2 style='color:#007B45;'>Resultado</h2>", unsafe_allow_html=True)
st.write(f"**Quantidade de caixas por envio:** {qtd_caixas}")
st.write(f"**Cada caixa atenderá por (dias):** {dias_por_caixa}")
st.write(f"**Quantidade total de envios:** {total_envios}")

st.markdown("---")

# Avisos conforme a quantidade de caixas (em verde escuro)
if qtd_caixas != "???" and qtd_caixas > 5:
    st.markdown("<p style='color:#007B45;'><strong>ATENÇÃO! Quantidade superior a 5 caixas</strong></p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#007B45;'>De acordo com legislação RDC 344/98 que aprova o regulamento técnico sobre substâncias e medicamentos sujeitos a controle especial:</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#007B45;'>Por gentileza, solicitar o envio de duas prescrições ou prescrição e justificativa.</p>", unsafe_allow_html=True)
    st.markdown("---")

# Tabela de envios (Esquema de envios)
st.markdown("<h2 style='color:#007B45;'>Esquema de Envios</h2>", unsafe_allow_html=True)
if isinstance(total_envios, int) and total_envios > 0:
    tabela_envios = []
    for i in range(1, min(total_envios + 1, 101)):  # Limitando a tabela a 100 linhas
        tabela_envios.append({"Envio": i, "Quantidade Caixa": qtd_caixas})
    
    st.dataframe(tabela_envios, use_container_width=True)  # Removendo o índice com st.dataframe
else:
    st.write("Nenhuma informação disponível para gerar a tabela de envios.")
