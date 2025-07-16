import streamlit as st


def pagina_inicio():

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

    st.markdown("<div class='section-title'>Bienvenido a Rendimiento Académico</div>", unsafe_allow_html=True)
    
    # --- SECCIÓN DE EQUIPO DE DESARROLLO ---
    st.markdown("<div class='section-title' style='margin-top: 20px;'>Equipo de Desarrollo</div>", unsafe_allow_html=True)
    
    # Añadir CSS específico para el equipo
    st.markdown("""
    <style>
    .team-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 30px;
        margin-top: 40px;
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

    .role {
        color: #666;
        font-size: 0.9rem;
        margin-top: 10px;
        font-style: italic;
    }

    .stats {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
        padding-top: 20px;
        border-top: 1px solid #eee;
    }

    .stat-item {
        text-align: center;
    }

    .stat-number {
        font-size: 1.2rem;
        font-weight: bold;
        color: #667eea;
    }

    .stat-label {
        font-size: 0.8rem;
        color: #666;
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
    
    # Grid de miembros del equipo
    with st.container():
        st.markdown("<div class='team-grid'>", unsafe_allow_html=True)
        
        # Miembro 1: Eduardo Mendieta
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            <div class='team-card floating-animation delay-0'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Eduardo Mendieta</h3>
                <div class='role'>Desarrollador Full Stack</div>
                <a href='https://github.com/edwmn01' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    edwmn01
                </a>
                <div class='stats'>
                    <div class='stat-item'>
                        <div class='stat-number'>25</div>
                        <div class='stat-label'>Commits</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>8</div>
                        <div class='stat-label'>Repos</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>12</div>
                        <div class='stat-label'>Issues</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Miembro 2: Anthony Rosillo
        with col2:
            st.markdown("""
            <div class='team-card floating-animation delay-1'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Anthony Rosillo</h3>
                <div class='role'>Backend Developer</div>
                <a href='https://github.com/rezeranty' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    rezeranty
                </a>
                <div class='stats'>
                    <div class='stat-item'>
                        <div class='stat-number'>32</div>
                        <div class='stat-label'>Commits</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>6</div>
                        <div class='stat-label'>Repos</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>9</div>
                        <div class='stat-label'>Issues</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Miembro 3: Justin Escalante
        with col3:
            st.markdown("""
            <div class='team-card floating-animation delay-2'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Justin Escalante</h3>
                <div class='role'>Frontend Developer</div>
                <a href='https://github.com/KYOUKO-002' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    KYOUKO-002
                </a>
                <div class='stats'>
                    <div class='stat-item'>
                        <div class='stat-number'>28</div>
                        <div class='stat-label'>Commits</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>11</div>
                        <div class='stat-label'>Repos</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>7</div>
                        <div class='stat-label'>Issues</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        # Miembro 4: Evelyn Criollo
        with col4:
            st.markdown("""
            <div class='team-card floating-animation delay-3'>
                <div class='profile-image'></div>
                <h3 class='member-name'>Evelyn Criollo</h3>
                <div class='role'>UI/UX Designer</div>
                <a href='https://github.com/Nidddddddd' class='github-info' target='_blank'>
                    <svg class='github-icon' viewBox='0 0 24 24' fill='currentColor'>
                        <path d='M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z'/>
                    </svg>
                    Nidddddddd
                </a>
                <div class='stats'>
                    <div class='stat-item'>
                        <div class='stat-number'>19</div>
                        <div class='stat-label'>Commits</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>5</div>
                        <div class='stat-label'>Repos</div>
                    </div>
                    <div class='stat-item'>
                        <div class='stat-number'>15</div>
                        <div class='stat-label'>Issues</div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)