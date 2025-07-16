import streamlit as st

def configuracion_inicial():
    st.set_page_config(
        page_title="Rendimiento Académico",
        page_icon="app_modulos/img/icono_app.png",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown("""
    <style>
                
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&display=swap');

        header {visibility: hidden;}
                
        .stApp {
            background-color: #dadada!important;
            font-family: 'Outfit', sans-serif;
        }
                
    </style>
    """, unsafe_allow_html=True)

