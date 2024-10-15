import streamlit as st
import math

# Função para limpar os inputs
def clear_inputs():
    st.session_state['ciclo'] = 0
    st.session_state['dias_uso'] = 0
    st.session_state['quantidade_cpr_dia'] = 0
    st.session_state['tempo_autorizacao'] = 0
    st.session_state['quantidade_cpr_caixa'] = 0
    st.session_state['quantidade_ciclos'] = 0

# Inicializar os valores no session_state, se ainda não estiverem definidos
if 'ciclo' not in st.session_state:
    st.session_state['ciclo'] = 0
if 'dias_uso' not in st.session_state:
    st.session_state['dias_uso'] = 0
if 'quantidade_cpr_dia' not in st.session_state:
    st.session_state['quantidade_cpr_dia'] = 0
if 'tempo_autorizacao' not in st.session_state:
    st.session_state['tempo_autorizacao'] = 0
if 'quantidade_cpr_caixa' not in st.session_state:
    st.session_state['quantidade_cpr_caixa'] = 0
if 'quantidade_ciclos' not in st.session_state:
    st.session_state['quantidade_ciclos'] = 0

# Título da aplicação
st.title("Calculadora para Sistema de Terapia Específica")

# Botão para limpar os inputs antes da criação dos widgets
if st.button("Limpar Inputs"):
    clear_inputs()

# Entrada do usuário
ciclo = st.number_input("Ciclo (em dias):", min_value=0, step=1, key="ciclo")
dias_uso = st.number_input("Dias de uso (em dias):", min_value=0, step=1, key="dias_uso")
quantidade_cpr_dia = st.number_input("Quantidade CPR por dia (em unidades):", min_value=0, step=1, key="quantidade_cpr_dia")
tempo_autorizacao = st.number_input("Tempo de Autorização (em dias):", min_value=0, step=1, key="tempo_autorizacao")
quantidade_cpr_caixa = st.number_input("Quantidade CPR por caixa (em unidades):", min_value=0, step=1, key="quantidade_cpr_caixa")

st.markdown("##### Somente para Ciclos Limitados")
quantidade_ciclos = st.number_input("Quantidade de ciclos:", min_value=0, step=1, key="quantidade_ciclos")

# Exibir a mensagem de pausa e cálculo do valor de autorização
if dias_uso < ciclo:
    pausa = ciclo - dias_uso
    st.markdown(f"<p style='color:red;'><strong>Ciclo com pausa de {pausa} dias</strong></p>", unsafe_allow_html=True)

# Cálculo "QTDDE CAIXAS P/ CICLO"
def calcular_qtd_caixas(dias_uso, quantidade_cpr_dia, quantidade_cpr_caixa):
    if quantidade_cpr_caixa > 0:
        return math.ceil((dias_uso * quantidade_cpr_dia) / quantidade_cpr_caixa)
    return "???"

# Cálculo "QTDDE ENVIOS TTL" - corrigido com base no tempo de autorização e ciclo
def calcular_qtd_envios(tempo_autorizacao, ciclo):
    if ciclo > 0:
        return math.ceil(tempo_autorizacao / ciclo)
    return "???"

# Cálculo "TEMPO DE AUTORIZAÇÃO TTL"
def calcular_tempo_autorizacao(quantidade_ciclos, ciclo):
    if quantidade_ciclos > 0 and ciclo > 0:
        return quantidade_ciclos * ciclo
    return "N/A"

# Cálculo "CADA CAIXA ATENDERÁ POR" (corrigido)
def calcular_dias_por_caixa(quantidade_cpr_caixa, ciclo, quantidade_cpr_dia, dias_uso):
    if quantidade_cpr_caixa > 0 and quantidade_cpr_dia > 0:
        return math.floor((quantidade_cpr_caixa * ciclo) / (quantidade_cpr_dia * dias_uso))
    return "???"

# Calcular os valores
qtd_caixas_por_ciclo = calcular_qtd_caixas(dias_uso, quantidade_cpr_dia, quantidade_cpr_caixa)
qtd_envios_total = calcular_qtd_envios(tempo_autorizacao, ciclo)  
tempo_autorizacao_total = calcular_tempo_autorizacao(quantidade_ciclos, ciclo)
dias_por_caixa = calcular_dias_por_caixa(quantidade_cpr_caixa, ciclo, quantidade_cpr_dia, dias_uso)

# Exibir resultados na ordem solicitada
st.markdown(f"**Tempo de Autorização TTL (dias): {tempo_autorizacao_total}**")

# Colocando a mensagem de tempo de autorização logo após o resultado do tempo de autorização
if tempo_autorizacao_total != "N/A":
    st.markdown(f"<p style='color:red;'><strong>Insira o valor {tempo_autorizacao_total} logo acima do Tempo de Autorização TTL fornecido para ciclos limitados no input de tempo de autorização (o que seria o quarto bloquinho da sequência)</strong></p>", unsafe_allow_html=True)

# Exibir o restante dos resultados
st.write(f"**Quantidade de caixas para ciclo:** {qtd_caixas_por_ciclo}")
st.write(f"**Quantidade de envios TTL:** {qtd_envios_total}")
st.write(f"**Cada caixa atenderá por (dias):** {dias_por_caixa}")

st.markdown("---")

# Tabela de envios (Esquema de envios)
st.subheader("Esquema de Envios")
if isinstance(qtd_envios_total, int) and qtd_envios_total > 0:
    tabela_envios = []
    for i in range(1, min(qtd_envios_total + 1, 101)):  # Limitando a tabela a 100 linhas
        tabela_envios.append({"Envio": i, "Quantidade Caixa": qtd_caixas_por_ciclo})

    st.dataframe(tabela_envios, use_container_width=True)
else:
    st.write("Nenhuma informação disponível para gerar a tabela de envios.")
