import streamlit as st
import base64
from datetime import datetime

st.sidebar.image("img/logo-empresa.png")

def verificar_autenticacao():
    if "email" not in st.session_state or "nome_de_usuario" not in st.session_state or "senha" not in st.session_state:
        st.write("Você precisa se cadastrar primeiro para acessar esta página.")
        st.write("Por favor, vá até a página de cadastro para continuar.")
        if st.button("Ir para cadastro"):
            st.switch_page("pages/cadastro.py")
        return False
    return True

def obter_saudacao():
    agora = datetime.now()
    if 4 > agora.hour < 12:
        return "Bom dia"
    elif 12 <= agora.hour < 18:
        return "Boa tarde"
    else :
        return "Boa noite"

def inicio():
    if not verificar_autenticacao():
        return

    nome_usuario = st.session_state.get("nome_de_usuario", "Cliente")
    saudacao = obter_saudacao()

    st.markdown(f"""
        <style>
            .greeting-title {{
                font-family: 'Verdana', sans-serif;
                color: #fff;
                text-align: center;
                border-radius: 10px;
                background-color: #4682B4; /* Cor de fundo azul */
                padding: 20px;
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 20px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2);
            }}
        </style>
        <div class="greeting-title">
           Olá {nome_usuario}, {saudacao} ! 
        </div>
    """, unsafe_allow_html=True)

    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode("utf-8")

    image_path = "img/fundocadastro.jpg"
    image_base64 = image_to_base64(image_path)

    css = f"""
        <style>
            .stApp {{
                background-image: url('data:image/jpeg;base64,{image_base64}');
                background-size: cover;
                background-position: center;
                height: 100vh;
                margin: 0;
                width: 100%;
            }}
            .content {{
                position: relative;
                z-index: 1;
                color: white;
                padding: 20px;
            }}
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    with open("style.css") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)

    st.title("Finance Smart")

    st.markdown(
        """
        <style>
            .custom-title-1 {
                font-size: 25px;
                color: white;
                margin-bottom: 5px;
                -webkit-text-stroke-width: 1.5px;
                -webkit-text-stroke-color: black;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <style>
            .custom-title-2 {
                font-size: 35px;
                color: black;
                margin-bottom: 5px;
                -webkit-text-stroke-width: 1.5px;
                -webkit-text-stroke-color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<h1 class="custom-title-1">Controlando Seu Financeiro com Segurança!</h1>', unsafe_allow_html=True)

    st.markdown('<h1 class="custom-title-2">O que deseja fazer?</h1>', unsafe_allow_html=True)

    css = """
        <style>
            .button-container {
                display: flex;
            }

            .button-container .stButton {
                width: auto;
                height: 40px;
                font-size: 8px;
                text-align: center;
            }
        </style>
    """
    st.markdown(css, unsafe_allow_html=True)

    st.markdown('<div class="button-container">', unsafe_allow_html=True)

    if st.button("Adicionar Despesas", key="despesas_button"):
        st.switch_page("pages/Despesas.py")
    elif st.button("Adicionar Lucro", key="lucro_button"):
        st.switch_page("pages/Lucro.py")
    elif st.button("Ver extrato", key="extrato_button"):
        st.switch_page("pages/Saldo.py")
    elif st.button("Ver Listas de Despesas", key="despesas_lista_button"):
        st.switch_page("pages/Despesas_Total.py")
    elif st.button("Ver Listas de Lucros", key="lucros_lista_button"):
        st.switch_page("pages/Lucros_Totais.py")

inicio()
