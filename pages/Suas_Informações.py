import streamlit as st
import base64
from PIL import Image

def verificarsenha(senha):
    senha = str(senha).strip()  # Remove espaços em branco no início e no final
    if len(senha) < 8:
        st.error("A senha deve conter no mínimo 8 caracteres não vazios!")
        return False
    return True

with open("inf.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)
with open("buttoninf.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

st.markdown("""
            <style>
                .header {
                        font-size: 36px;
                        font-weight: bold;
                        color: #4CAF50;  # Cor verde
                        text-align: center;
                        padding: 20px;
                        background-color: #f4f4f9;
                        border-radius: 10px;
                        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
                        }
                    </style>
                """, unsafe_allow_html=True)

st.markdown("""
    <style>
        .info-text {
            font-size: 30px;
            color: black;  
            text-align: center;
            font-weight: normal;
            padding: 10px;
            background-color: white;
            border-radius: 5px;
            margin-top: 20px;
            border: 4px solid black;
        }
    </style>
""", unsafe_allow_html=True)

def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

image_path = "img/suasinf (1).jpg"
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

def exibir_informacoes():
    if "email" not in st.session_state or "nome_de_usuario" not in st.session_state or "senha" not in st.session_state:
        st.markdown('<div class="header">Por favor, faça seu cadastro para acessar suas informações.</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-text">Clique abaixo para realizar o cadastro.</div>', unsafe_allow_html=True)
        if st.button("Clique aqui"):
            st.switch_page("pages/cadastro.py")
    else:
        email = st.session_state.get("email")
        nome_de_usuario = st.session_state.get("nome_de_usuario")
        senha = st.session_state.get("senha")
        foto = st.session_state.get("foto_perfil")  

        st.header("Foto de Perfil:")
        if foto is not None:
            st.markdown(
                f"""
                <div style="text-align: center;">
                    <img src="data:image/jpeg;base64,{base64.b64encode(foto).decode('utf-8')}" 
                        alt="Foto de Perfil" 
                        style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover; border: 4px solid #4CAF50;">
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("Deseja alterar sua foto?")
        else:
            st.warning("Nenhuma foto de perfil foi carregada. Você pode adicionar uma agora.")

        nova_foto = st.file_uploader("Envie ou altere sua foto de perfil:", type=["jpg", "jpeg", "png"])
        if nova_foto:
            st.session_state.foto_perfil = nova_foto.read()
            st.session_state.nova_foto_carregada = True 

        if st.session_state.get("nova_foto_carregada"):
            if st.button("ATUALIZAR"):
                st.session_state.nova_foto_carregada = False

        st.header("Informações do seu cadastro:")

        st.subheader("Email:")
        st.write(email)

        st.subheader("Nome de Usuário:")
        st.write(nome_de_usuario)

        st.subheader("Senha:")
        senha_mostrada = st.checkbox("Mostrar senha", value=False)

        if senha_mostrada:
            st.write(senha)
        else:
            st.write("**********")

        if "atualizado" not in st.session_state:
            st.session_state.atualizado = False

        if "em_alteracao" not in st.session_state:
            st.session_state.em_alteracao = False

        if not st.session_state.em_alteracao:
            st.header("Deseja alterar suas informações?")
            mudanca = st.selectbox("Selecione uma opção: (clique 2 vezes)", ["Não", "Sim"])

            if mudanca == "Sim":
                st.session_state.em_alteracao = True
        else:
            st.header("Digite suas novas informações:")
            novo_nome = st.text_input("Novo nome de usuário:")
            nova_senha = st.text_input("Nova senha:", type="password")
            
            if st.button("ALTERAR (clique 2 vezes)"):
                if novo_nome and nova_senha:
                    if verificarsenha(nova_senha): 
                        st.session_state.nome_de_usuario = novo_nome
                        st.session_state.senha = nova_senha
                        st.session_state.atualizado = True
                        st.session_state.em_alteracao = False
                        st.success("Suas informações foram atualizadas com sucesso!")
                    else:
                        st.warning("A senha não atende aos critérios. Tente novamente.")
                else:
                    st.warning("Por favor, preencha todos os campos.")

            if st.session_state.atualizado and not st.session_state.em_alteracao:
                st.info("Suas informações já foram atualizadas.")

if __name__ == "__main__":
    exibir_informacoes()
