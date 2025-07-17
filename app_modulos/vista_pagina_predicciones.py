import streamlit as st

def pagina_predicciones():
    st.markdown("""
    <style>
        .section-title {
            font-size: 36px;
            color: #071739;
            margin-bottom: 40px;
            text-align: center;
            font-weight: 700;
            font-family: 'Segoe UI', sans-serif;
            animation: fadeInDown 1s ease-in-out;
        }

        .button-container {
            display: flex;
            justify-content: center;
            margin-top: 30px;
            animation: slideInUp 1s ease-out;
        }

        .custom-button {
            display: flex;
            align-items: center;
            gap: 10px;
            background: linear-gradient(135deg, #2f2f2f, #1e1e1e); /* Gris oscuro a casi negro */
            color: #0366d6; /* Azul tipo GitHub */
            padding: 12px 24px;
            border-radius: 30px; /* Estilo píldora */
            text-decoration: none;
            font-weight: 600;
            font-size: 16px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.25);
            transition: all 0.3s ease;
        }

        .custom-button:hover {
            box-shadow: 0 6px 14px rgba(0, 0, 0, 0.35);
            transform: scale(1.05);
            background: linear-gradient(135deg, #3a3a3a, #252525);
        }

        .colab-icon {
            width: 20px;
            height: 20px;
            fill: #0366d6; /* Azul GitHub */
        }

        @keyframes fadeInDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='section-title'>Predicciones del rendimiento académico de los estudiantes basado en fichas socioeconómicas</div>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class='button-container'>
        <a href='https://colab.research.google.com/drive/1IhIQOiITatqcMH9rR8XEJxE6EcHa9WUH?authuser=3#scrollTo=YQ2WABXA2ivq' 
           target='_blank' class='custom-button'>
            <svg class='colab-icon' viewBox='0 0 24 24'>
                <path d='M12 2a10 10 0 00-7.546 16.57l-2.387 2.387a1 1 0 001.414 1.414l2.387-2.387A10 10 0 1012 2z'/>
            </svg>
            Colab
        </a>
    </div>
    """, unsafe_allow_html=True)
