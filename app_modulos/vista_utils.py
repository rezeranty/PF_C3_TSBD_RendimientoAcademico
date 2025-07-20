import streamlit as st
import time

def cargar_con_loader(min_duracion=0.5):
    def decorador(func):
        def wrapper(*args, **kwargs):
            placeholder = st.empty()

            with placeholder.container():
                st.markdown(
                    """
                    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
                        <div style="text-align: center;">
                            <div class="loader" style="
                                border: 8px solid #f3f3f3;
                                border-top: 8px solid #3498db;
                                border-radius: 50%;
                                width: 60px;
                                height: 60px;
                                animation: spin 1s linear infinite;
                                margin: auto;
                            "></div>
                            <p style="color:#071739;font-weight:bold;">Cargando...</p>
                        </div>
                    </div>

                    <style>
                    @keyframes spin {
                        0% { transform: rotate(0deg); }
                        100% { transform: rotate(360deg); }
                    }
                    </style>
                    """,
                    unsafe_allow_html=True
                )

            tiempo_inicio = time.time()
            resultado = func(*args, **kwargs)
            tiempo_total = time.time() - tiempo_inicio

            tiempo_restante = min_duracion - tiempo_total
            if tiempo_restante > 0:
                time.sleep(tiempo_restante)

            placeholder.empty()
            return resultado

        return wrapper
    return decorador