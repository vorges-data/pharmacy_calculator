import streamlit as st
import math

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

# Título da aplicação
st.title("Cálculo de Dose de Ataque para Sistema de Terapia Específica")

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

st.markdown("##### Dose de Manutenção")
dose_manutencao = st.number_input("Dose Manutenção (em mg):", min_value=0, step=1, key="dose_manutencao")
intervalo_manutencao = st.number_input("Intervalo Manutenção (em dias):", min_value=0, step=1, key="intervalo_manutencao")

# Divisor e título "Resultado"
st.markdown("---")  # Adiciona uma linha divisória
st.subheader("Resultado")

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

# Título "INFORMAÇÕES PARA DOSE DE ATAQUE"
st.markdown("##### Informações Para Dose De Ataque")
st.write(f"**TTL Medicamento Necessário (mg):** {ttl_medicamento_necessario}")
st.write(f"**Nro Caixas Necessárias:** {nro_caixas_necessarias}")

# Título "INFORMAÇÕES PARA ENVIO MENSAL (30 DIAS)"
st.markdown("##### Informações Para Envio Mensal (30 Dias)")
st.write(f"**Caixas Necessárias por Envio:** {caixas_por_envio}")
