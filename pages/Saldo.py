import streamlit as st
import base64

def verificar_autenticacao():
     if "email" not in st.session_state or "nome_de_usuario" not in st.session_state or "senha" not in st.session_state:
         st.write("Você precisa se cadastrar primeiro para acessar esta página.")
         st.write("Por favor, vá até a página de cadastro para continuar.")
         if st.button("ir para cadastro"):
             st.switch_page("pages/cadastro.py")
         return False 
     return True 

st.sidebar.image("img/logo-empresa.png")

def saldo_total():
    if not verificar_autenticacao(): 
        return 

    if "despesas" not in st.session_state:
        st.session_state.despesas = [] 

    if "lucros" not in st.session_state:
        st.session_state.lucros = []

    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')

    image_path = "img/saldoimagem.jpg"

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

    total_lucros = 0
    total_despesas = 0
    nome_usuario = st.session_state.get("nome_de_usuario", "Cliente")  

    if "lucros" in st.session_state and len(st.session_state.lucros) > 0:
        total_lucros = sum(lucro['valor'] for lucro in st.session_state.lucros)

    if "despesas" in st.session_state and len(st.session_state.despesas) > 0:
        total_despesas = sum(despesa['valor'] for despesa in st.session_state.despesas)

    saldo = total_lucros - total_despesas

    # Encontrar a categoria com o maior gasto
    categorias_gastos = {}
    for despesa in st.session_state.despesas:
        categoria = despesa['categoria']
        categorias_gastos[categoria] = categorias_gastos.get(categoria, 0) + despesa['valor']

    # Identificar a categoria com o maior gasto
    categoria_maior_gasto = max(categorias_gastos, key=categorias_gastos.get, default=None)
    valor_maior_gasto = categorias_gastos.get(categoria_maior_gasto, 0)

    # Encontrar a categoria com o maior lucro
    categorias_lucros = {}
    for lucro in st.session_state.lucros:
        categoria = lucro['categoria']
        categorias_lucros[categoria] = categorias_lucros.get(categoria, 0) + lucro['valor']

    # Identificar a categoria com o maior lucro
    categoria_maior_lucro = max(categorias_lucros, key=categorias_lucros.get, default=None)
    valor_maior_lucro = categorias_lucros.get(categoria_maior_lucro, 0)

    st.markdown(f'<div class="titulo">Saldo Total de {nome_usuario} </div>', unsafe_allow_html=True)
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
        </style>
    """, unsafe_allow_html=True)

    st.write(f"**Total de Lucros: R${total_lucros:.2f}**")
    st.write(f"**Total de Despesas: R${total_despesas:.2f}**")
    st.write(f"**Saldo Total: R${saldo:.2f}**")

    if saldo < 0:
        st.error(f"Atenção, {nome_usuario}: Seu saldo está negativo! Tome cuidado!!")
    elif saldo == 0:
        st.info(f"Olá, {nome_usuario}: Seu saldo está zerado.")
    else:
        st.success(f"Parabéns, {nome_usuario}: Seu saldo está positivo! Continue assim!")

    # Exibir aviso para a categoria com maior gasto
    if categoria_maior_gasto:
        st.warning(f"Atenção: A categoria com o maior gasto é '{categoria_maior_gasto}' com um total de R${valor_maior_gasto:.2f}. Avalie se é possível reduzir essa despesa.")

    # Exibir aviso para a categoria com maior lucro
    if categoria_maior_lucro:
        st.success(f"Parabéns: A categoria com o maior lucro é '{categoria_maior_lucro}' com um total de R${valor_maior_lucro:.2f}.")


saldo_total()
