import streamlit as st
import pandas as pd
import os

from modulos.limpieza_datos import limpiar_fichas, limpiar_notas
from modulos.migracion_datos import migrar_info_a_tablas_fichas, migrar_info_a_tablas_notas


def pagina_carga_datos():
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

    st.markdown("<div class='section-title' style='margin-top: -80px;'>Cargar Nuevos Datos</div>", unsafe_allow_html=True)

    # ======================= PLANTILLAS =======================
    st.markdown(
        """
        <div class='sub-section-title'>
            Descargar Plantillas
        </div>
        """,
        unsafe_allow_html=True
    )

    descargar_plantillas()

    # ======================= TABS PARA FICHAS Y NOTAS =======================
    st.markdown(
            """
            <div class='sub-section-title'>
                Cargar datos de Fichas Socioeconómicas y Notas de estudiantes
            </div>
            """,
            unsafe_allow_html=True
        )
    
    tabs = st.tabs(["📋 Fichas Socioeconómicas", "📝 Notas Estudiantes"])

    with tabs[0]:
        cargar_nuevos_datos_fichas()

    with tabs[1]:
        cargar_nuevos_datos_notas()


def descargar_plantillas():
    ruta_fichas = "modulos/data/plantilla_fichas.xlsx"
    ruta_notas = "modulos/data/plantilla_notas.xlsx"

    col1, col2, col3, col4  = st.columns([1, 2, 2, 1])

    with col2:
        if os.path.exists(ruta_fichas):
            with open(ruta_fichas, "rb") as file_fichas:
                if st.download_button(
                    label="📥 Descargar plantilla de fichas",
                    data=file_fichas,
                    file_name="plantilla_fichas.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key="descarga_fichas"
                ):
                    st.success("✅ Descarga exitosa: plantilla_fichas.xlsx")
        else:
            st.error("❌ No se encontró el archivo plantilla_fichas.xlsx")

    with col3:
        if os.path.exists(ruta_notas):
            with open(ruta_notas, "rb") as file_notas:
                if st.download_button(
                    label="📥 Descargar plantilla de notas",
                    data=file_notas,
                    file_name="plantilla_notas.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                    key="descarga_notas"
                ):
                    st.success("✅ Descarga exitosa: plantilla_notas.xlsx")
        else:
            st.error("❌ No se encontró el archivo plantilla_notas.xlsx")


def cargar_nuevos_datos_fichas():
    nombres_columnas_fichas = [
        'ci_pasaporte', 'correo_tec', 'PrimerNombre', 'SegunNombre', 'PrimerApellido',
        'SegunApellido', 'sexo', 'genero', 'estado_civil', 'num_hijos', 'etnia',
        'fecha_nacimiento', 'tipo_parroquia', 'ciudad', 'provincia', 'pais',
        'celular', 'tiene_beca', 'estudio_otra_carrera', 'ocupacion_estudiante',
        'persona_cubre_gastos', 'recibe_ayuda', 'nombre_carrera', 'periodo_academico',
        'nombre_colegio', 'tipo_colegio', 'titulo_bachiller', 'anio_graduacion',
        'num_propiedades', 'valor_propiedades', 'num_vehiculos', 'valor_vehiculos',
        'total_ingresos', 'total_egresos', 'nombre_contacto', 'telefono_contacto',
        'tipo_sangre', 'semanas_embarazo', 'porcentaje_discapacidad',
        'nombre_discapacidad', 'nombre_enfermedades', 'vacuna_covid',
        'antecedentes_patologicos_fam', 'integrantes_familia',
        'integrantes_aporte_economico', 'cabezas_familia', 'tipo_vivienda',
        'condicion_vivienda', 'servicios_vivienda', 'tiene_carnet_conadis', 'codigo_carrera'
    ]
    
    uploaded_file_fichas = st.file_uploader(
        "Selecciona un archivo Excel de Fichas(.xls o .xlsx)",
        type=["xls", "xlsx"]
    )
    if uploaded_file_fichas is not None:
        try:
            df_fichas = pd.read_excel(uploaded_file_fichas, engine='openpyxl')
            st.success("Archivo cargado correctamente:")
            st.dataframe(df_fichas)

            columnas_archivo = set(df_fichas.columns.str.strip())
            columnas_esperadas = set(nombres_columnas_fichas)

            if columnas_archivo == columnas_esperadas:
                btn_subir_info_fichas = st.button("Subir información Fichas")
                if btn_subir_info_fichas:
                    try:
                        df_fichas = limpiar_fichas(df_fichas)
                        migrar_info_a_tablas_fichas(df_fichas)
                    except Exception as e:
                        st.warning("❌ Existen errores en el contenido de los archivos.")
                        print(str(e))
            else:
                st.warning("❌ Las columnas del archivo no coinciden con las requeridas, por favor, descargue la plantilla de fichas.")
        except Exception as e:
            st.error(f"Error al leer el archivo!")
            print(f"Error al leer el archivo: {e}")


def cargar_nuevos_datos_notas():
    nombres_columnas_notas = [
        'periodo_academico', 'paralelo', 'ci_pasaporte', 'nombres', 'codigo_carrera', 'nombre_carrera'
        'ciclo_carrera', 'nombre_asignatura', 'numero_matricula',
        'porcentaje_asistencia', 'nota_final', 'estado_estudiante',
        'estado_matricula', 'tipo_ingreso'
    ]
    
    uploaded_file_notas = st.file_uploader(
        "Selecciona un archivo Excel de Notas(.xls o .xlsx)",
        type=["xls", "xlsx"]
    )
    if uploaded_file_notas is not None:
        try:
            df_notas = pd.read_excel(uploaded_file_notas)
            st.success("Archivo cargado correctamente:")
            st.dataframe(df_notas)

            columnas_archivo = set(df_notas.columns.str.strip())
            columnas_esperadas = set(nombres_columnas_notas)

            if columnas_archivo == columnas_esperadas:
                btn_subir_info_notas = st.button("Subir información Notas")
                if btn_subir_info_notas:
                    try:
                        df_notas = limpiar_notas(df_notas)
                        #migrar_datos(df_notas==df_notas)
                    except Exception as e:
                        st.warning("❌ Existen errores en el contenido de los archivos.")
                        st.error(str(e))
            else:
                st.warning("❌ Las columnas del archivo no coinciden con las requeridas, por favor, descargue la plantilla de Notas.")
        except Exception as e:
            st.error(f"Error al leer el archivo: {e}")
