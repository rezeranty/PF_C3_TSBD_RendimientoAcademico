import streamlit as st


def get_opcion_menu_principal():
    st.markdown("""
    <style>
    
        .css-1d391kg {
            background-color: rgba(255, 255, 255, 0.95) !important;
            border-right: 2px solid #071739;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
                    
        .sidebar-title {
            font-size: 24px;
            color: #071739;
            font-weight: 700;
            margin-bottom: 30px;
            text-align: center;
            padding: 20px 0;
            border-bottom: 2px solid #8fb3ff;
        }

        .sidebar-nav-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
            flex-grow: 1;
        }

        .sidebar-nav-item {
            display: block;
            width: 100%;
            padding: 15px 20px;
            margin: 8px 0;
            background-color: transparent;
            border: 2px solid #8fb3ff;
            border-radius: 10px;
            color: #071739;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s ease;
            cursor: pointer;
        }

        .sidebar-nav-item:hover {
            background-color: #8fb3ff;
            color: white;
            transform: translateX(5px);
        }

        .sidebar-nav-item.active {
            background-color: #071739;
            color: white;
            border-color: #071739;
        }

    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("<div class='sidebar-title'>Rendimiento Académico</div>", unsafe_allow_html=True)
        
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "Inicio"
        
        if st.button("🏠 INICIO", key="home", use_container_width=True):
            st.session_state.current_page = "Inicio"
        
        if st.button("📊 ESTADÍSTICAS", key="stats", use_container_width=True):
            st.session_state.current_page = "Estadisticas"
        
        if st.button("🔮 PREDICCIONES", key="predictions", use_container_width=True):
            st.session_state.current_page = "Predicciones"
        
        if st.button("📝 BLOG", key="blog", use_container_width=True):
            st.session_state.current_page = "Blog"
        
    return st.session_state.current_page