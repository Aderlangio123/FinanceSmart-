import streamlit as st
import base64
from datetime import datetime 
from collections import defaultdict  # Para agrupar as despesas por categoria

with open("strong.css") as css:
                st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

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
    if "lucros" not in st.session_state:
        st.session_state.lucros = []

    if not verificar_autenticacao(): 
         return 
    
    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    image_path = "img/fundo_ltotal.jpg" 

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
    nome_usuario = st.session_state.get("nome_de_usuario", "Cliente")

    st.markdown(css, unsafe_allow_html=True)

    st.markdown(f'<div class="titulo">Lucros Atuais de  {nome_usuario} </div>', unsafe_allow_html=True)
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
                margin-bottom: 20px;
                border: 4px solid black;
            }
            }
        </style>
    """, unsafe_allow_html=True)

    if "lucros" not in st.session_state or len(st.session_state.lucros) == 0:
            st.warning("Nenhum lucro registrado.")
            return

        # Agrupar lucros por categoria
    lucros_por_categoria = defaultdict(list)
    for lucro in st.session_state.lucros:
            lucros_por_categoria[lucro["categoria"]].append(lucro)

    total_geral = 0

    st.markdown(f"<h1 style='color: white; background-color: #333333; padding: 10px; border-radius: 10px;'>Lucros Totais</h1>", unsafe_allow_html=True)

        # Exibir lucros agrupados por categoria
    for categoria, lucros in lucros_por_categoria.items():
            st.markdown(f"### {categoria}")
            total_categoria = 0  # Para o total de cada categoria

            for lucro in lucros:
                st.write(f"**Nome:** {lucro['nome']}")
                st.write(f"**Valor:** R${lucro['valor']:.2f}")
                st.write(f"**Adicionado em:** {lucro['hora']}")
                st.write("---")
                total_categoria += lucro['valor']
                total_geral += lucro['valor']

            st.write(f"**Total da categoria {categoria}: R${total_categoria:.2f}**")
            st.write("---")

        
    st.write(f"**Total Geral de Lucros: R${total_geral:.2f}**")

lucros()