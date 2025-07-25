import streamlit as st


import streamlit as st
import modulos.graficas_estadisticas as ge
from modulos.db_postgres_consultas import obtener_carreras, obtener_periodos_academicos, total_estudiantes


def pagina_estadisticas():
    st.markdown(
        """
        <style>
            .section-title {
                font-size: 42px;
                color: #071739;
                text-align: center;
                font-weight: 700;
            }

            .sub-section-title {
                font-size: 24px;
                color: #071739;
                margin-top: 40px;
                margin-bottom: 40px;
                text-align: center;
                font-weight: 600;
                padding: 15px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown("<div class='section-title' style='margin-top: -80px;'>Estadísticas Académicas</div>", unsafe_allow_html=True)

    
    filtro_carrera, filtro_periodo, carreras_ids = agregar_filtros()

    with st.spinner("Cargando gráficos estadísticos..."):
        agregar_graficas_estadisticas(filtro_carrera, filtro_periodo, carreras_ids)


def agregar_filtros():
    f1_c1, f1_c2, f1_c3 = st.columns([1, 2, 4])

    with f1_c1:
        st.markdown(
            """
            <div class='sub-section-title'>
                 FILTROS
            </div>
            """,
            unsafe_allow_html=True
        )

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

    return filtro_carrera, filtro_periodo, carreras_ids


def agregar_graficas_estadisticas(filtro_carrera, filtro_periodo, carreras_ids):
    carrera_id = None if filtro_carrera == "TODAS" else carreras_ids[filtro_carrera]
    periodo = None if filtro_periodo == "TODOS" else filtro_periodo

    total_estudiantes_activos = total_estudiantes(carrera_id, periodo)

    # FILA N°2 ----------------------------------------------------------------------------------------------
    st.markdown(
    """
        <div class='sub-section-title'>
            DATOS GENERAL
        </div>
    """,unsafe_allow_html=True
    )

    f2_c1, f2_c2, f2_c3 = st.columns([1, 1, 1])
    with f2_c1:
        st.markdown(f"""
        <div style="font-size:16px; color:#000080; font-weight:bold; margin-bottom:25px;">
            Periodo Académico:
            <div style="font-size:16px; color:#000000;"> {filtro_periodo}</div>
        </div>
        """, unsafe_allow_html=True)

    with f2_c2:
        st.markdown(f"""
        <div style="font-size:16px; color:#000080; font-weight:bold; margin-bottom:25px;">
            Carrera:
            <div style="font-size:16px; color:#000000;"> {filtro_carrera}</div>
        </div>
        """, unsafe_allow_html=True)

    with f2_c3:
        st.markdown(f"""
        <div style="font-size:16px; color:#000080; font-weight:bold; margin-bottom:25px;">
            Estudiantes Activos:
            <div style="font-size:16px; color:#000000;"> {total_estudiantes_activos}</div>
        </div>
        """, unsafe_allow_html=True)

    # FILA N°3 ----------------------------------------------------------------------------------------------
    st.markdown(
    """
        <div class='sub-section-title'>
            DATOS DEMOGRÁFICOS
        </div>
    """,unsafe_allow_html=True
    )

    f3_c1, f3_c2, f3_c3 = st.columns([1, 1, 1])
    with f3_c1:
        st.plotly_chart(ge.grafica_estudiantes_sexo(carrera_id, periodo), use_container_width=True)
    with f3_c2:
        st.plotly_chart(ge.grafica_genero(carrera_id, periodo), use_container_width=True)
    with f3_c3:
        st.plotly_chart(ge.grafica_estado_civil(carrera_id, periodo), use_container_width=True)

    # FILA N°4 ----------------------------------------------------------------------------------------------

    f4_c1, f4_c2, f4_c3 = st.columns([1, 1, 1])
    with f4_c2:
        st.plotly_chart(ge.grafica_distribucion_edades(carrera_id, periodo), use_container_width=True)

        

    # FILA N°5 ----------------------------------------------------------------------------------------------
    st.markdown(
    """
        <div class='sub-section-title'>
            DATOS SOCIOECONÓMICOS
        </div>
    """,unsafe_allow_html=True
    )

    f5_c1, f5_c2, f5_c3 = st.columns([1, 1, 1])
    with f5_c1:
        st.plotly_chart(ge.grafica_tipo_parroquia(carrera_id, periodo), use_container_width=True)
    with f5_c2:
        st.plotly_chart(ge.grafica_condicion_vivienda(carrera_id, periodo), use_container_width=True)
    with f5_c3:
        st.plotly_chart(ge.grafica_tiene_beca(carrera_id, periodo), use_container_width=True)

                
    # FILA N°6: ----------------------------------------------------------------------------------------------
    f6_c1, f6_c2 = st.columns([1, 1])
    with f6_c1:
        st.plotly_chart(ge.grafica_ocupacion_estudiante(carrera_id, periodo), use_container_width=True)
    with f6_c2:
        st.plotly_chart(ge.grafica_tipo_colegio(carrera_id, periodo), use_container_width=True) 

    if filtro_carrera == "TODAS" and filtro_periodo == "TODOS":
        f7_c1, f7_c2 = st.columns([1, 1])
        with f7_c1:
            st.plotly_chart(ge.grafica_cabeza_familia(), use_container_width=True)
        with f7_c2:
            st.plotly_chart(ge.grafica_aporte_economico(), use_container_width=True) 

    # FILA N°7: ----------------------------------------------------------------------------------------------
    st.markdown(
    """
        <div class='sub-section-title'>
            DATOS ACADÉMICOS
        </div>
    """,unsafe_allow_html=True
    )
    
    f8_c1, f8_c2, f8_c3 = st.columns([1, 1, 1])
    with f8_c1:
        st.plotly_chart(ge.grafica_estado_estudiante(carrera_id, periodo), use_container_width=True)
    with f8_c2:
        st.plotly_chart(ge.grafica_porcentaje_asistencia_promedio(carrera_id, periodo), use_container_width=True) 
    with f8_c3:
        st.plotly_chart(ge.grafica_frecuencia_numero_matricula(carrera_id, periodo), use_container_width=True)
    

