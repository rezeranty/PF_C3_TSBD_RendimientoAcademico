import streamlit as st

from app_modulos.db_postgres_consultas import obtener_carreras, obtener_periodos_academicos, total_estudiantes
import app_modulos.graficas_estadisticas as ge


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

    if btn_buscar:

        with st.spinner("Cargando estadísticas..."):
            
            total_estudiantes_activos = total_estudiantes(None if filtro_carrera == "TODAS" else carreras_ids[filtro_carrera],
                                                        None if filtro_periodo == "TODOS" else filtro_periodo)
            
            # FILA N°2: ----------------------------------------------------------------------------------------------
            st.markdown("""
                <div style="font-size:20px; color:#000080; font-weight:bold; margin:25px 0;">
                    GENERAL
                </div>
                """, unsafe_allow_html=True)
            
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
                <div style="font-size:16px; color:#000080; font-weight:bold;">
                    Carrera:
                    <div style="font-size:16px; color:#000000;"> {filtro_carrera}</div>
                </div>
                """, unsafe_allow_html=True)

            with f2_c3:
                st.markdown(f"""
                <div style="font-size:16px; color:#000080; font-weight:bold;">
                    Estudiantes Activos:
                    <div style="font-size:16px; color:#000000;"> {total_estudiantes_activos}</div>
                </div>
                """, unsafe_allow_html=True)
            
             # FILA N°3: ----------------------------------------------------------------------------------------------
            f3_c1, f3_c2, f3_c3 = st.columns([1, 1, 1])
            
            with f3_c1:
                st.plotly_chart(ge.grafica_estudiantes_sexo(None if filtro_carrera == "TODAS" else carreras_ids[filtro_carrera],
                                                            None if filtro_periodo == "TODOS" else filtro_periodo), use_container_width=True)

            with f3_c2:
                st.plotly_chart(ge.grafica_genero(None if filtro_carrera == "TODAS" else carreras_ids[filtro_carrera],
                                                  None if filtro_periodo == "TODOS" else filtro_periodo), use_container_width=True)

            with f3_c3:
                st.plotly_chart(ge.grafica_estado_civil(None if filtro_carrera == "TODAS" else carreras_ids[filtro_carrera],
                                                        None if filtro_periodo == "TODOS" else filtro_periodo), use_container_width=True)

            # FILA N°4: ----------------------------------------------------------------------------------------------
            f4_c1, f4_c2, f4_c3 = st.columns([1, 1, 1])
            
            with f4_c1:
                st.plotly_chart(ge.grafica_ocupacion_estudiante(None if filtro_carrera == "TODAS" else carreras_ids[filtro_carrera],
                                                                None if filtro_periodo == "TODOS" else filtro_periodo), use_container_width=True)

            with f4_c2:
                st.plotly_chart(ge.grafica_tipo_parroquia(None if filtro_carrera == "TODAS" else carreras_ids[filtro_carrera],
                                                  None if filtro_periodo == "TODOS" else filtro_periodo), use_container_width=True)

            with f4_c3:
                st.plotly_chart(ge.grafica_tiene_beca(None if filtro_carrera == "TODAS" else carreras_ids[filtro_carrera],
                                                        None if filtro_periodo == "TODOS" else filtro_periodo), use_container_width=True)
            
            # FILA N°4: ----------------------------------------------------------------------------------------------
            f5_c1, f5_c2, f5_c3 = st.columns([1, 1, 1])
            
            with f5_c1:
                st.plotly_chart(ge.grafica_distribucion_edades(None if filtro_carrera == "TODAS" else carreras_ids[filtro_carrera],
                                                                None if filtro_periodo == "TODOS" else filtro_periodo), use_container_width=True)

            with f5_c2:
                pass

            with f5_c3:
                pass