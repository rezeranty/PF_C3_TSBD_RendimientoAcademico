import streamlit as st


def pagina_blog():

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
    
    st.markdown("<div class='section-title'>Blog Académico</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Artículos y recursos sobre educación y análisis de datos</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; text-align: center; margin-bottom: 20px;'>📝 Artículos Recientes</h3>
        </div>
        """, unsafe_allow_html=True)
        st.success("📖 Cómo interpretar las métricas académicas")
        st.info("🔍 Análisis de tendencias educativas 2024")
        st.warning("💡 Mejores prácticas en evaluación estudiantil")
    
    with col2:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; text-align: center; margin-bottom: 20px;'>🎯 Recursos</h3>
        </div>
        """, unsafe_allow_html=True)
        st.success("📊 Guías de análisis de datos")
        st.info("🔧 Herramientas recomendadas")
        st.warning("📚 Bibliografía especializada")