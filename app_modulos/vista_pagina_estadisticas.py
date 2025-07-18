import streamlit as st

from app_modulos.db_postgres_consultas import obtener_carreras, obtener_periodos_academicos


def pagina_estadisticas():

    st.markdown("""
    <style>
        
        .section-title {
            font-size: 42px;
            color: #071739;
            margin-bottom: 30px;
            text-align: center;
            font-weight: 700;
            animation: slideInLeft 0.8s ease-in-out;
        }

        .section-subtitle {
            font-size: 18px;
            color: #071739;
            margin-bottom: 40px;
            text-align: center;
            opacity: 0.8;
            animation: fadeIn 1s ease-in-out;
        }

    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='section-title'>Estadísticas Académicas</div>", unsafe_allow_html=True)
    
    agregar_graficas_estadisticas()


def agregar_graficas_estadisticas():

    # FILA N°1: ----------------------------------------------------------------------------------------------
    f1_c1, f1_c2, f1_c3, f1_c4 = st.columns([1, 2, 4, 2])

    with f1_c1:
        st.markdown("""
        <div style="font-size:20px; color:#000080; font-weight:bold;">
            FILTROS
        </div>
        """, unsafe_allow_html=True)

    with f1_c2:
        periodos_academicos = [i[0] for i in obtener_periodos_academicos()]
        periodos_academicos.insert(0, "TODOS")
        filtro_periodo = st.selectbox(label="Periodo Académico:", options=periodos_academicos)

    with f1_c3:
        carreras_ids = obtener_carreras()
        carreras_ids = {f"{i[1]} - {i[2]}": i[0] for i in carreras_ids}
        carreras = list(carreras_ids.keys())
        carreras.insert(0, "TODAS")
        filtro_carrera = st.selectbox(label="Carrera:", options=carreras)

    with f1_c4:
        btn_buscar = st.button("Estadísticas")

