import streamlit as st
import base64
from datetime import datetime
import pytz  

def verificar_autenticacao():
    if "email" not in st.session_state or "nome_de_usuario" not in st.session_state or "senha" not in st.session_state:
        st.write("Você precisa se cadastrar primeiro para acessar esta página.")
        st.write("Por favor, vá até a página de cadastro para continuar.")
        if st.button("ir para cadastro"):
            st.switch_page("pages/cadastro.py")
        return False 
    return True 

from datetime import datetime
import pytz

def despesas():
    if not verificar_autenticacao():
        return 

    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    image_path = "img/despesaimagem1.jpg"

    image_base64 = image_to_base64(image_path)

    css = f"""
        <style>
            .stApp {{
                background-image: url('data:image/jpeg;base64,{image_base64}');
                background-size: cover;  
                background-position: center;  
                background-attachment: fixed;  
                height: 100vh; 
                margin: 0;
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

    if "despesas" not in st.session_state:
        st.session_state.despesas = []

    st.markdown("""
        <style>
            .titulo {
                font-size: 40px;        
                font-weight: bold;             
                color: #08a286;                
                text-align: center;           
                background-color: white;   
                padding: 20px;              
                border-radius: 15px;          
                box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1); 
                margin-bottom: 20px;
                border: 4px solid black; 
                -webkit-text-stroke-width: 1px;
                -webkit-text-stroke-color: black; 
            }

            .descricao {
                font-size: 35px;               
                color: black;                
                text-align: center;
                background-color: white;  
                border: 4px solid black;  
                border-radius: 15px;           
                padding: 10px;                 
                margin-bottom: 40px;     
                font-style: italic;   
                -webkit-text-stroke-width: 1px;
                -webkit-text-stroke-color: black; 
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="titulo">Painel De Despesas</div>', unsafe_allow_html=True)
    st.markdown('<div class="descricao">Insira suas despesas abaixo ⭣ </div>', unsafe_allow_html=True)

    nome_despesa = st.text_input("Nome ou descrição da despesa:")
    valor_despesa = st.number_input("Informe o valor da despesa", min_value=0.0, format="%.2f")

    # Lista de categorias de despesa
    categorias = [
        "Alimentação", "Transporte", "Saúde", "Educação", "Moradia", 
        "Lazer", "Roupas", "Tecnologia", "Impostos", "Outros"
    ]
    categoria_despesa = st.selectbox("Escolha a categoria da despesa", categorias)

    if st.button("Adicionar despesa"):
        if valor_despesa > 0 and nome_despesa.strip() != "" and categoria_despesa != "":
            # Ajustando para o fuso horário correto
            fuso_horario = pytz.timezone("America/Sao_Paulo")
            horario_adicao = datetime.now(pytz.utc).astimezone(fuso_horario).strftime("%Y-%m-%d %H:%M:%S")

            despesa = {
                "nome": nome_despesa, 
                "valor": valor_despesa, 
                "categoria": categoria_despesa,
                "hora": horario_adicao
            }
            st.session_state.despesas.append(despesa)
            st.success(f"Despesa '{nome_despesa}' de R${valor_despesa:.2f} na categoria '{categoria_despesa}' adicionada às {horario_adicao}!")
        else:
            st.warning("Por favor, preencha todos os campos corretamente.")

despesas()