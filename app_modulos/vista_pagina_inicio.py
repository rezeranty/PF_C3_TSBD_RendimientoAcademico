import streamlit as st
from PIL import Image
import base64

def get_image_base64(path):
    """Convierte una imagen local a una cadena Base64 para incrustarla en HTML."""
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except FileNotFoundError:
        st.error(f"Error: La imagen no se encontró en la ruta: {path}")
        return "" 

def pagina_inicio():
    try:
        logo = Image.open("app_modulos/img/logo_tec.png")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(logo, use_container_width=True)
    except FileNotFoundError:
        st.error("Logo no encontrado. Verifica que el archivo esté en app_modulos/img/logo_tec.png")

    st.markdown("""
    <style>
        .main {
            padding-top: 20px;
            padding-bottom: 20px;
        }
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .section-title {
            font-size: 42px;
            color: #071739;
            margin-bottom: 10px;
            text-align: center;
            font-weight: 700;
            animation: slideInLeft 0.8s ease-in-out;
        }
        .project-title {
            font-size: 24px;
            color: #071739;
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
            color: #071739;
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
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(7, 23, 57, 0.3);
        }
        .github-icon { width: 20px; height: 20px; }
        .home-icon { width: 20px; height: 20px; }

        /* --- TARJETAS CON ANIMACIÓN CONSTANTE --- */
        .team-card {
            width: 260px;
            height: 380px;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            padding: 30px;
            text-align: center;
            transition: transform 0.4s ease, box-shadow 0.4s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            border: 1px solid rgba(7, 23, 57, 0.1);
            opacity: 0;
            animation: fadeInUp 0.8s ease forwards, floatCard 3s ease-in-out infinite;
            margin-left: auto;
            margin-right: auto;
        }
        /* Animación flotante constante */
        @keyframes floatCard {
            0%   { transform: translateY(0px); }
            50%  { transform: translateY(-8px); }
            100% { transform: translateY(0px); }
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
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .profile-image img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
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

        /* Animación de entrada */
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(40px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .delay-0 { animation-delay: 0s; }
        .delay-1 { animation-delay: 0.3s; }
        .delay-2 { animation-delay: 0.6s; }
        .delay-3 { animation-delay: 0.9s; }
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
                <path d='M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 
                8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235
                -3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695
                -.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23
                1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605
                -2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 
                1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 
                3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405
                c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18
                .765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 
                5.925.435.375.81 1.095.81 2.22 0 1.605-.015 
                2.895-.015 3.3 0 .315.225.69.825.57A12.02 
                12.02 0 0024 12c0-6.63-5.37-12-12-12z'/>
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

    st.markdown("<div class='team-section-title'>REALIZADO POR</div>", unsafe_allow_html=True)

    eduardo_img = get_image_base64("app_modulos/img/Eduardo Mendieta.jpg")
    anthony_img = get_image_base64("app_modulos/img/Anthony Rosillo.jpg")
    justin_img = get_image_base64("app_modulos/img/Justin Escalante.jpg")
    evelyn_img = get_image_base64("app_modulos/img/Evelyn Criollo.jpg")

    team_members_data = [
        ("Eduardo Mendieta", "edwmn01", eduardo_img, "delay-0"),
        ("Anthony Rosillo", "rezeranty", anthony_img, "delay-1"),
        ("Justin Escalante", "KYOUKO-002", justin_img, "delay-2"),
        ("Evelyn Criollo", "Nidddddddd", evelyn_img, "delay-3")
    ]

    cols_display = st.columns(len(team_members_data)) 

    for i, (name, github, img, delay) in enumerate(team_members_data):
        with cols_display[i]:
            st.markdown(f"""
            <div class='team-card {delay}'>
                <div class='profile-image'>
                    <img src='data:image/jpg;base64,{img}' 
                         alt='{name}'
                         style='width:100%; height:100%; object-fit:cover; border-radius:50%;'/>
                </div>
                <h3 class='member-name'>{name}</h3>
                <a href='https://github.com/{github}' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 
                        8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235
                        -3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695
                        -.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23
                        1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605
                        -2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 
                        1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 
                        3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405
                        c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18
                        .765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 
                        5.925.435.375.81 1.095.81 2.22 0 1.605-.015 
                        2.895-.015 3.3 0 .315.225.69.825.57A12.02 
                        12.02 0 0024 12c0-6.63-5.37-12-12-12z'/>
                    </svg>
                    {github}
                </a>
            </div>
            """, unsafe_allow_html=True)
