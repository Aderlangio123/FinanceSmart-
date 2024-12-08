import streamlit as st
import base64
from datetime import datetime  # Importando para pegar a data e hora atual
from collections import defaultdict  # Para agrupar as despesas por categoria

def verificar_autenticacao():
    if "email" not in st.session_state or "nome_de_usuario" not in st.session_state or "senha" not in st.session_state:
        st.write("Você precisa se cadastrar primeiro para acessar esta página.")
        st.write("Por favor, vá até a página de cadastro para continuar.")
        if st.button("ir para cadastro"):
            st.switch_page("pages/cadastro.py")
        return False 
    return True 

def despesas_total():
    if not verificar_autenticacao(): 
        return 
    with open("strong.css") as css:
                st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

    nome_usuario = st.session_state.get("nome_de_usuario", "Cliente")  
    
    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    image_path = "img/fundo_despesatotal.jpg" 

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

    st.markdown(f'<div class="titulo">Despesas Atuais de {nome_usuario} </div>', unsafe_allow_html=True)
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
                border: 4px solid green;
            }
        </style>
    """, unsafe_allow_html=True)

    if "despesas" in st.session_state and len(st.session_state.despesas) > 0:
        # Agrupar as despesas por categoria
        despesas_por_categoria = defaultdict(list)
        for despesa in st.session_state.despesas:
            despesas_por_categoria[despesa['categoria']].append(despesa)
        
        total_geral = 0  # Para o total geral de todas as despesas

        # Exibir as despesas agrupadas por categoria
        for categoria, despesas in despesas_por_categoria.items():
            st.markdown(f"### {categoria}")
            total_categoria = 0  # Para o total de cada categoria

            for despesa in despesas:
                st.write(f"Despesa: {despesa['nome']}")
                st.write(f"Valor: R${despesa['valor']:.2f}")
                st.write(f"Adicionada em: {despesa['hora']}")
                st.write("---")
                total_categoria += despesa['valor']
                total_geral += despesa['valor']

            st.write(f"**Total da categoria {categoria}: R${total_categoria:.2f}**")
            st.write("---")

        st.write(f"**Total Geral de Despesas: R${total_geral:.2f}**")
    else:
        st.warning("Você não cadastrou nenhum gasto")

despesas_total()
