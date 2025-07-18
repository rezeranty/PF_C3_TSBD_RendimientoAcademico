import streamlit as st

from app_modulos.db_postgres_consultas import obtener_carreras, obtener_periodos_academicos, obtener_total_estudiantes_activos


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
    f1_col1, f1_col2, f1_col3, = st.columns([1, 2, 5])

    info_carreras = []
    carrera_seleccionada, periodo_seleccionado = "", ""

    st.markdown("""
        <style>
        .stSelectbox label {
            color: #000000 !important;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)
    
    with f1_col1:
        st.markdown("""
                    <p style='color: #000000; font-size: 18px; margin-bottom: 20px;'>FILTROS</p>
        """, unsafe_allow_html=True)

    with f1_col2:
        periodos_academicos = [i[0] for i in obtener_periodos_academicos()]
        periodos_academicos.insert(0, 'Todos')
        periodo_seleccionado = st.selectbox(label="Periodo Académico:", options=periodos_academicos)

    with f1_col3:
        info_carreras = obtener_carreras() if periodo_seleccionado == 'Todos' else obtener_carreras(periodo_academico=periodo_seleccionado)
        info_carreras = {f"{i[1]} | {i[2]}": i[0] for i in info_carreras}
        nombres_carreras = list(info_carreras.keys())
        nombres_carreras.insert(0, 'Todas')
        carrera_seleccionada = st.selectbox(label="Carrera:" ,options=nombres_carreras)
    
    # FILA N°2: ----------------------------------------------------------------------------------------------
    st.markdown(f"""
                    <p style='color: #000000; font-size: 18px; margin-bottom: 20px;'>GENERAL: 📆 Periodo Académico: {periodo_seleccionado} 🎓 Carrera: {carrera_seleccionada}</p>
        """, unsafe_allow_html=True)
    
    id_carrera = info_carreras.get(carrera_seleccionada) if carrera_seleccionada != 'Todas' else None
    periodo = periodo_seleccionado if periodo_seleccionado != 'Todos' else None
    st.markdown(f"""
                    <p style='color: #000000; font-size: 15px; margin-bottom: 20px;'>Total estudiantes activos: {obtener_total_estudiantes_activos(id_carrera=id_carrera, periodo=periodo)}</p>
        """, unsafe_allow_html=True)
