import streamlit as st
from PIL import Image

st.set_page_config(page_title='Home', page_icon='🧪')

image = Image.open('images/4bio.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('<h2 style="color:#007B45;">4Bio - Medicamentos</h2>', unsafe_allow_html=True)
st.sidebar.markdown("""---""")

st.sidebar.write('Stephany Aranha')

st.write('<h1 style="color:#007B45;">4Bio Medicamentos - Calculadoras</h1>', unsafe_allow_html=True)
st.markdown("""---""")

st.markdown(
    """
    <h3 style="color:#007B45;">Como utilizar este Webapp?</h3>

    No menu lateral deste Web App há cinco páginas:

    - **1. Calculadora Para Sistema de Terapia Específica:**
        - Variáveis a serem informadas:
            - Ciclo (em dias);
            - Dias de Uso (em dias);
            - Quantidade CPR por dia (em dias);
            - Tempo de Autorização (em dias);
            - Quantidade CPR por caixa (em CPR);
            - Quantidade de Ciclos.

        - Resultado:
            - Quantidade de Caixas para o Ciclo;
            - Quantidade de Envios TTL;
            - Tempo de Autorização TTL;
            - Cada caixa atenderá por.

    - **2. Calculadora Para Sistema de Terapia Específica GH:**
        - Variáveis a serem informadas:
            - Dias de Uso (em dias);
            - Dosagem por dia (em mg);
            - Concentração (em mg);
            - Tempo de Autorização (em dias).

        - Resultado:
            - Quantidade de Caixas por envio;
            - Quantidade Total de envios;
            - Cada caixa atenderá por.

    - **3. Superfície Corpórea Para Sistema de Terapia Específica:**
        - Variáveis a serem informadas:
            - Peso (em kg);
            - Altura (em cm);
            - Dose (em m²).

        - Resultado:
            - Superfície Corpórea;
            - Dose em mg.

    - **4. Dose de Ataque Para Sistema de Terapia Específica:**
        - Variáveis a serem informadas:
            - Medicamento (em mg);
            - Quantidade por caixa (em unidade);
            - Dose Ataque 1 (em mg);
            - Dose Ataque 2 (em mg);
            - Dose Ataque 3 (em mg);
            - Dose Ataque 4 (em mg);
            - Dose Ataque 5 (em mg);
            - Dose Manutenção (em mg);
            - Intervalo Manutenção (em dias).

        - Resultado:
            - Informações para Dose de Ataque:
                - TTL Medicamento Necessária;
                - Número de Caixas necessárias.
            - Informações para envio mensal (30 dias):
                - Caixas necessárias por envio.

    - **5. Calculadora de Datas:**
        - Variáveis a serem informadas:
            - Quantidade de Medicamento com o paciente (em dias);
            - Data Inicial (em data);
            - Período (em dias).

        - Resultado:
            - Possui medicamento até;
            - Programar para.
    """, unsafe_allow_html=True
)
st.markdown("""---""")
st.write("Desenvolvido por: Stephany Aranha")
