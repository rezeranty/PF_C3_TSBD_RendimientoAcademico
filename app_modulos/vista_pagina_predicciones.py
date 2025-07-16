import streamlit as st


def pagina_predicciones():

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
    
    st.markdown("<div class='section-title'>Predicciones Académicas</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-subtitle'>Modelos predictivos para el rendimiento estudiantil</div>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <div class='card'>
            <h3 style='color: #071739; margin-bottom: 20px;'>🔮 Modelos Predictivos</h3>
            <p style='color: #071739; opacity: 0.8; margin-bottom: 20px;'>
                Algoritmos avanzados de machine learning para predecir el rendimiento académico
                futuro basado en datos históricos y patrones de comportamiento.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='card' style='text-align: center;'>
            <h4 style='color: #071739;'>Algoritmos</h4>
            <p style='color: #071739; opacity: 0.8;'>
                Regresión Lineal<br>
                Random Forest<br>
                Neural Networks<br>
                SVM<br>
                Time Series
            </p>
        </div>
        """, unsafe_allow_html=True)