import streamlit as st


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
    st.markdown("<div class='section-subtitle'>Análisis detallado del rendimiento estudiantil</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; margin-bottom: 20px;'>📈 Análisis de Rendimiento</h3>
            <p style='color: #071739; opacity: 0.8; margin-bottom: 20px;'>
                Visualizaciones detalladas del desempeño académico, tendencias de calificaciones
                y análisis comparativo por materias y períodos.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h4 style='color: #071739;'>Métricas Clave</h4>
            <p style='color: #071739; opacity: 0.8;'>
                Promedio General<br>
                Materias Aprobadas<br>
                Asistencia<br>
                Tendencias<br>
                Comparativas
            </p>
        </div>
        """, unsafe_allow_html=True)