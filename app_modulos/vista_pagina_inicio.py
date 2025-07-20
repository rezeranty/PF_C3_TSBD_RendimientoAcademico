import streamlit as st
from PIL import Image

from app_modulos.vista_utils import cargar_con_loader


@cargar_con_loader(min_duracion=0.3)
def pagina_inicio():
    
    try:
        logo = Image.open("app_modulos/img/logo_tec.png")

        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(logo, use_container_width=300)
    except FileNotFoundError:
        st.error("Logo no encontrado. Verifica que el archivo esté en app_modulos/img/logo_tec.png")

    st.markdown("""
    <style>
        .section-title {
            font-size: 42px;
            color: 
#071739;
            margin-bottom: 10px;
            text-align: center;
            font-weight: 700;
            animation: slideInLeft 0.8s ease-in-out;
        }

        .project-title {
            font-size: 24px;
            color: 
#071739;
            margin-bottom: 40px;
            text-align: center;
            font-weight: 600;
            line-height: 1.4;
            padding: 15px;
            background: rgba(255, 255, 255, 0.7);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        .team-section-title {
            font-size: 36px;
            color: 
#071739;
            margin: 40px 0 20px 0;
            text-align: center;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 30px 0;
        }

        .custom-button {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            padding: 12px 24px;
            background: #071739;
            color: white;
            text-decoration: none;
            border-radius: 25px;
            font-weight: 600;
            font-size: 16px;
            transition: all 0.3s ease;
            border: 2px solid #071739;
        }

        .custom-button:hover {
            background: white;
            color: #071739;
            text-decoration: none;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(7, 23, 57, 0.3);
        }

        .github-icon {
            width: 20px;
            height: 20px;
        }

        .home-icon {
            width: 20px;
            height: 20px;
        }

        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-50px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Tecnología Superior en Big Data</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='project-title'>
        ANÁLISIS Y PREDICCIÓN DEL RENDIMIENTO ACADÉMICO DE ESTUDIANTES DE LAS CARRERAS DEL INSTITUTO SUPERIOR TECNOLÓGICO DEL AZUAY DESDE EL PERIODO ACADÉMICO 2023-1P HASTA 2024-2P
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='button-container'>
        <a href='https://github.com/rezeranty/PF_C3_TSBD_RendimientoAcademico' target='_blank' class='custom-button'>
            <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                <path d='M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0024 12c0-6.63-5.37-12-12-12z'/>
            </svg>
            Repositorio
        </a>
        <a href='https://www.tecazuay.edu.ec/' target='_blank' class='custom-button'>
            <svg class='home-icon' viewBox='0 0 24 24' fill='currentColor'>
                <path d='M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z'/>
            </svg>
            Carrera
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='team-section-title'>realizado por</div>", unsafe_allow_html=True)

    st.markdown("""
    <style>
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 30px;
        margin-top: 20px;
    }

    .team-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        transition: all 0.3s ease;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        border: 1px solid rgba(7, 23, 57, 0.1);
    }

    .team-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }

    .profile-image {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        margin: 0 auto 20px;
        overflow: hidden;
        border: 4px solid #667eea;
        transition: all 0.3s ease;
        position: relative;
        background-color: #8fb3ff;
    }

    .team-card:hover .profile-image {
        transform: scale(1.1);
        border-color: #764ba2;
    }

    .member-name {
        font-size: 1.4rem;
        font-weight: bold;
        color: #071739;
        margin-bottom: 10px;
    }

    .github-info {
        background: linear-gradient(135deg, #333 0%, #555 100%);
        color: white;
        padding: 12px 20px;
        border-radius: 25px;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        text-decoration: none;
        margin: 10px 0;
    }

    .github-info:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .github-icon {
        width: 20px;
        height: 20px;
    }
    
    .floating-animation {
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }
    
    /* Animaciones para cada tarjeta */
    .delay-0 { animation-delay: 0s; }
    .delay-1 { animation-delay: 0.5s; }
    .delay-2 { animation-delay: 1s; }
    .delay-3 { animation-delay: 1.5s; }
    </style>
    """, unsafe_allow_html=True)
    
    with st.container():
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            <div class='team-card floating-animation delay-0'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Eduardo Mendieta</h3>
                <a href='https://github.com/edwmn01' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    edwmn01
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='team-card floating-animation delay-1'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Anthony Rosillo</h3>
                <a href='https://github.com/rezeranty' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    rezeranty
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class='team-card floating-animation delay-2'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Justin Escalante</h3>
                <a href='https://github.com/KYOUKO-002' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    KYOUKO-002
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class='team-card floating-animation delay-3'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Evelyn Criollo</h3>
                <a href='https://github.com/Nidddddddd' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    Nidddddddd
                </a>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)