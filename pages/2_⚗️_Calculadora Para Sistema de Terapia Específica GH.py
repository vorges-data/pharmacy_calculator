import streamlit as st
import math

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

# Título da aplicação
st.title("Calculadora para Sistema de Terapia Específica GH")

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
st.subheader("Resultado")
st.write(f"**Quantidade de caixas por envio:** {qtd_caixas}")
st.write(f"**Cada caixa atenderá por (dias):** {dias_por_caixa}")
st.write(f"**Quantidade total de envios:** {total_envios}")

st.markdown("---")

# Avisos conforme a quantidade de caixas (em vermelho)
if qtd_caixas != "???" and qtd_caixas > 5:
    st.markdown("<p style='color:red;'><strong>ATENÇÃO! Quantidade superior a 5 caixas</strong></p>", unsafe_allow_html=True)
    st.markdown("<p style='color:red;'>De acordo com legislação RDC 344/98 que aprova o regulamento técnico sobre substâncias e medicamentos sujeitos a controle especial:</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:red;'>Por gentileza, solicitar o envio de duas prescrições ou prescrição e justificativa.</p>", unsafe_allow_html=True)
    st.markdown("---")





# Tabela de envios (Esquema de envios)
st.subheader("Esquema de Envios")
if isinstance(total_envios, int) and total_envios > 0:
    tabela_envios = []
    for i in range(1, min(total_envios + 1, 101)):  # Limitando a tabela a 100 linhas
        tabela_envios.append({"Envio": i, "Quantidade Caixa": qtd_caixas})
    
    st.dataframe(tabela_envios, use_container_width=True)  # Removendo o índice com st.dataframe
else:
    st.write("Nenhuma informação disponível para gerar a tabela de envios.")
