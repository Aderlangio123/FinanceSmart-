import streamlit as st
import base64
import re

def verificarsenha(senha):
    senha = str(senha).strip()  # Remove espaços em branco no início e no final
    if len(senha) < 8:
        st.error("A senha deve conter no mínimo 8 caracteres não vazios!")
        return False
    return True

def verificar_email(email):
    email = email.strip()  
    padrao_email = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
    if not re.match(padrao_email, email):
        st.error("Email inválido. Certifique-se de que é um e-mail válido do Gmail!")
        return False
    return True

with open("cadastro.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.sidebar.image("img/logo-empresa.png")

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

image_path = "img/cadastroimagem (1).jpg"
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

def cadastro_usuario():
    st.markdown(f'<div class="titulo">FinanceSmart - Cadastro de Usuário</div>', unsafe_allow_html=True)
    st.markdown("""
        <style>
            .titulo {
                font-size: 35px;        
                font-weight: bold;             
                color: #5353ec;
                -webkit-text-stroke-width: 1.5px;
                -webkit-text-stroke-color: black;                
                text-align: center;           
                background-color: white;   
                border-radius: 15px;          
                margin-bottom: 20px;
                border: 4px solid black;
            }
        </style>
    """, unsafe_allow_html=True)

    if "email" in st.session_state and "nome_de_usuario" in st.session_state and "senha" in st.session_state and "foto_perfil" in st.session_state:
        st.write("Você já tem um cadastro.")
        if st.button("Ver suas informações"):
            st.switch_page("pages/Suas_Informações.py")
    else:
        email = st.text_input("Digite seu e-mail:")
        nome_de_usuario = st.text_input("Digite seu nome de usuário:")
        senha = st.text_input("Crie uma senha:", type="password")
        foto = st.file_uploader("Envie sua foto de perfil:", type=["jpg", "jpeg", "png"])

        if st.button("Cadastrar"):
            if verificar_email(email) and verificarsenha(senha):
                st.session_state.email = email
                st.session_state.nome_de_usuario = nome_de_usuario
                st.session_state.senha = senha
                st.session_state.foto_perfil = foto.read() if foto else None  

                st.write("Cadastro concluído com sucesso!")
                st.success("Você está autenticado agora!")

                if st.button("Ver suas informações"):
                    st.switch_page("pages/Suas_Informações.py")


cadastro_usuario()
