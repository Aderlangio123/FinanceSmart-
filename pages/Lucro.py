import streamlit as st
import base64
from datetime import datetime
import pytz  # Para manipulação de fuso horário

st.sidebar.image("img/logo-empresa.png")

def verificar_autenticacao():
    if "email" not in st.session_state or "nome_de_usuario" not in st.session_state or "senha" not in st.session_state:
        st.write("Você precisa se cadastrar primeiro para acessar esta página.")
        st.write("Por favor, vá até a página de cadastro para continuar.")
        if st.button("ir para cadastro"):
            st.switch_page("pages/cadastro.py")
        return False 
    return True 

def lucros():
    if not verificar_autenticacao(): 
        return 

    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    image_path = "img/fundo_lucro (1).jpg" 

    image_base64 = image_to_base64(image_path)

    css = f"""
        <style>
            .stApp {{
                background-image: url('data:image/jpeg;base64,{image_base64}');
                background-size: cover;  /* Faz a imagem cobrir toda a tela */
                background-position: center;  /* Alinha a imagem no centro */
                background-attachment: fixed;  /* A imagem fica fixa enquanto rola */
                height: 100vh;  /* Garante que a imagem ocupe toda a altura da tela */
                margin: 0;
            }}

            .content {{
                position: relative;
                z-index: 1;
                color: white;  /* Cor do texto para contraste */
                padding: 20px;
            }}
        </style>
    """

    st.markdown(css, unsafe_allow_html=True)

    if "lucros" not in st.session_state:
        st.session_state.lucros = []  

    st.markdown("""
        <h1 style='color: white; background-color: #333333; padding: 10px; border-radius: 10px; margin-bottom: 0;'>Painel De Lucros</h1>
    """, unsafe_allow_html=True)

    st.markdown("""
        <p style='color: white; background-color: #333333; padding: 10px; border-radius: 10px; margin-top: -14px;'>Insira seus lucros abaixo</p>
    """, unsafe_allow_html=True)

    valor_lucro = st.number_input("Informe o valor do lucro")

    nome_lucro = st.text_input("Nome ou descrição do lucro:")

    categorias = [
        "Vendas de Produtos", 
        "Serviços Prestados", 
        "Investimentos", 
        "Freelance / Trabalho Independente", 
        "Salário Mensal", 
        "Outros Lucros"
    ]
    categoria_lucro = st.selectbox("Escolha a categoria do lucro", categorias)

    if st.button("Adicionar lucro", key="button-lucro"):
        if valor_lucro > 0 and nome_lucro.strip() != "" and categoria_lucro != "":
            # Ajustando para o fuso horário correto
            fuso_horario = pytz.timezone("America/Sao_Paulo")
            horario_adicao = datetime.now(pytz.utc).astimezone(fuso_horario).strftime("%Y-%m-%d %H:%M:%S")
            
            lucro = {
                "nome": nome_lucro, 
                "valor": valor_lucro,
                "categoria": categoria_lucro,
                "hora": horario_adicao
            }
            st.session_state.lucros.append(lucro)
            st.success(f"Lucro: {nome_lucro} de R${valor_lucro:.2f} na categoria '{categoria_lucro}' no horário {horario_adicao} adicionado!")
        else:
            st.warning("Por favor, preencha todos os campos corretamente.")

lucros()
