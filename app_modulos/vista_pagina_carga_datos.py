import streamlit as st
import os
import pandas as pd
from app_modulos.db_postgres_inserts import *
import numpy as np
from app_modulos.limpieza_datos import *
from app_modulos.db_postgres_consultas import (obtener_id_ci_estudiante, obtener_id_codigo_carrera, obtener_id_nombre_asignaturas, obtener_id_por_columnas_aux_estudiante_carrera, )

    

def migrar_estudiantes(df_estudiantes):
    
    df_estudiantes = df_estudiantes[["ci_pasaporte", "correo_tec","nombres", 
                                     "sexo","genero","estado_civil","num_hijos",
                                     "etnia","fecha_nacimiento","tipo_parroqui",
                                     "ciudad","provincia","pais","celular",
                                     "tiene_beca","estudio_otra_carrera",
                                     "ocupacion_estudiante","persona_cubre_gastos",
                                     "recibe_ayuda"]]
    df_estudiantes = df_estudiantes.replace({np.nan: None})
    crear_estudiantes(df_estudiantes)
    
def agregar_columnas_extras_ficha(df):

    df["id_estudiante"]=df["ci_pasaporte"].map(obtener_id_ci_estudiante())
    return df

def migrar_colegios():
    df_colegios = agregar_columnas_extras_ficha()
    df_colegios = df_colegios[["id_estudiante", "nombre_colegio", "tipo_colegio","titulo_bachiller","anio_graduacion"]]
    df_colegios = df_colegios.replace({np.nan: None})
    crear_estudiantes_colegio(df_colegios)



def migrar_propiedades_extras():
    df_propiedades = agregar_columnas_extras_ficha()
    df_propiedades = df_propiedades[["id_estudiante", "num_propiedades", "valor_propiedades", "num_vehiculos", "valor_vehiculos"]]                                
    df_propiedades = df_propiedades.replace({np.nan: None})
    crear_propiedades_extra(df_propiedades)


def migrar_economia():
    df_economia = agregar_columnas_extras_ficha()
    df_economia = df_economia[["id_estudiante", "total_ingresos", "total_egresos"]]                                
    df_economia = df_economia.replace({np.nan: None})
    crear_economia_estudiante(df_economia)


def migrar_contacto_emergencia():
    df_contacto_emergencia = agregar_columnas_extras_ficha()
    df_contacto_emergencia = df_contacto_emergencia[["id_estudiante", "nombre_contacto", "telefono_contacto"]]                                
    df_contacto_emergencia = df_contacto_emergencia.replace({np.nan: None})
    crear_contacto_emergencia(df_contacto_emergencia)


def migrar_datos_salud():
    df_datos_salud = agregar_columnas_extras_ficha()
    df_datos_salud = df_datos_salud[["id_estudiante", "tipo_sangre", "semanas_embarazo", "porcentaje_discapacidad", "nombre_discapacidad", 
        "nombre_enfermedades", "vacuna_covid", "antecedentes_patologicos_fam", "tiene_carnet_conadis"]]

    df_datos_salud = df_datos_salud.replace({np.nan: None})                                

    crear_datos_salud(df_datos_salud)


def migrar_familia():
    df_familia = agregar_columnas_extras_ficha()
    df_familia = df_familia[["id_estudiante", "integrantes_familia", "integrantes_aporte_economico", "cabezas_familia"]]

    df_familia = df_familia.replace({np.nan: None})

    crear_familia(df_familia)


def migrar_familia():
    df_familia = agregar_columnas_extras_ficha()
    df_familia = df_familia[["id_estudiante", "integrantes_familia", "integrantes_aporte_economico", "cabezas_familia"]]

    df_familia = df_familia.replace({np.nan: None})

    crear_familia(df_familia)


def migrar_vivienda():
    df_vivienda = agregar_columnas_extras_ficha()
    df_vivienda = df_vivienda[["id_estudiante", "tipo_vivienda", "condicion_vivienda", "servicios_vivienda"]]

    df_vivienda = df_vivienda.replace({np.nan: None})

    crear_vivienda(df_vivienda)


def migrar_carreras(df_carreras):
    df_carreras = df_carreras[["codigo_carrera", "nombre_carrera"]]
    df_carreras = df_carreras.replace({np.nan: None})
    crear_carreras(df_carreras)


def agregar_columnas_extras_nota(df):

    df["id_estudiante"]=df["ci_pasaporte"].map(obtener_id_ci_estudiante())
    df["id_carrera"]=df["codigo_carrera"].map(obtener_id_codigo_carrera())
    
    return df


def migrar_estudiantes_carreras():
    df_estudiantes_carreras = agregar_columnas_extras_nota()

    df_estudiantes_carreras = df_estudiantes_carreras[[
        "id_carrera", "id_estudiante", "ciclo_carrera", 
        "periodo_academico", "paralelo"
    ]]

    df_estudiantes_carreras = df_estudiantes_carreras.drop_duplicates(
        subset=["id_carrera", "id_estudiante", "periodo_academico"]
    )

    
    df_estudiantes_carreras = df_estudiantes_carreras.replace({np.nan: None})

    crear_estudiantes_carreras(df_estudiantes_carreras)
    

def migrar_asignaturas():
    df_asignaturas = agregar_columnas_extras_nota()

    df_asignaturas = df_asignaturas[[
        "id_carrera", "nombre_asignatura"
    ]]

    df_asignaturas = df_asignaturas.replace({np.nan: None})

    crear_asignaturas(df_asignaturas)



def migrar_estudiante_asignatura():
    df_estudiante_asignatura = agregar_columnas_extras_nota()

    df_estudiante_asignatura = df_estudiante_asignatura[[
        "id_carrera", "id_estudiante", "periodo_academico", "nombre_asignatura",
        "numero_matricula", "porcentaje_asistencia",
        "nota_final", "estado_estudiante", "estado_matricula", "tipo_ingreso"
    ]]

    df_estudiante_asignatura["id_carrera"]= df_estudiante_asignatura["id_carrera"].fillna("0").astype(int)
    df_estudiante_asignatura["id_estudiante"]= df_estudiante_asignatura["id_estudiante"].fillna("0").astype(int)


    df_estudiante_asignatura["aux_estudiante_carrera"] = (
        df_estudiante_asignatura["id_carrera"].astype(str) + "-" +
        df_estudiante_asignatura["id_estudiante"].astype(str) + "-" +
        df_estudiante_asignatura["periodo_academico"].astype(str)
    )

    
    df_estudiante_asignatura["id_asignatura"] = df_estudiante_asignatura["nombre_asignatura"].map(obtener_id_nombre_asignaturas())

    df_estudiante_asignatura["id_estudiante_carrera"] = df_estudiante_asignatura["aux_estudiante_carrera"].map(obtener_id_por_columnas_aux_estudiante_carrera())

    df_estudiante_asignatura["id_estudiante_carrera"] = df_estudiante_asignatura["id_estudiante_carrera"].fillna("0").astype(int)

    df_estudiante_asignatura = df_estudiante_asignatura.drop(
        columns=["id_carrera", "id_estudiante", "periodo_academico", "nombre_asignatura"]
    )

    df_estudiante_asignatura = df_estudiante_asignatura.replace({np.nan: None})
    crear_estudiantes_asignaturas(df_estudiante_asignatura)







def pagina_carga_datos():
    st.title("📂 Descargar plantillas de datos")

    ruta_notas = r"C:/Users/dt_bs/Escritorio/Tareass/Proyecto/PF_C3_TSBD_RendimientoAcademico/app_modulos/data/plantilla_notas.xlsx"
    ruta_fichas = r"C:/Users/dt_bs/Escritorio/Tareass/Proyecto/PF_C3_TSBD_RendimientoAcademico/app_modulos/data/plantilla_fichas.xlsx"

    if os.path.exists(ruta_notas):
        with open(ruta_notas, "rb") as f:
            contenido_notas = f.read()

        if st.download_button(
            label=" Descargar plantilla de NOTAS",
            data=contenido_notas,
            file_name="plantilla_notas.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            st.success(" Plantilla de NOTAS descargada exitosamente.")
    else:
        st.error(" No se encontró el archivo 'plantilla_notas.xlsx'.")

    if os.path.exists(ruta_fichas):
        with open(ruta_fichas, "rb") as f:
            contenido_fichas = f.read()

        if st.download_button(
            label=" Descargar plantilla de FICHAS",
            data=contenido_fichas,
            file_name="plantilla_fichas.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        ):
            st.success(" Plantilla de FICHAS descargada exitosamente.")
    else:
        st.error(" No se encontró el archivo 'plantilla_fichas.xlsx'.")







# Lista de columnas esperadas
nombres_columnas_notas = [
    'periodo_academico', 'paralelo', 'ci_pasaporte', 'nombres', 'carrera',
    'ciclo_carrera', 'nombre_asignatura', 'numero_matricula',
    'porcentaje_asistencia', 'nota_final', 'estado_estudiante',
    'estado_matricula', 'tipo_ingreso'
]

st.title("Visor de archivo Excel NOTAS     📊")

# Subir archivo
archivo_excel = st.file_uploader("Sube tu archivo Excel", type=["xlsx"])

if archivo_excel is not None:
    try:
        # Leer el archivo Excel
        df = pd.read_excel(archivo_excel)
        
        # Verificar columnas
        columnas_archivo = set(df.columns)
        columnas_esperadas = set(nombres_columnas_notas)

        if columnas_archivo == columnas_esperadas:
            st.success("✅ El archivo contiene todas las columnas requeridas.")
        else:
            st.warning("⚠️ Las columnas del archivo no coinciden con las requeridas.")
            columnas_faltantes = columnas_esperadas - columnas_archivo
            columnas_sobrantes = columnas_archivo - columnas_esperadas

            if columnas_faltantes:
                st.error(f"❌ Columnas faltantes: {list(columnas_faltantes)}")
            if columnas_sobrantes:
                st.info(f"ℹ️ Columnas adicionales (no requeridas): {list(columnas_sobrantes)}")

        # Mostrar vista previa del archivo
        st.subheader("Vista previa de los datos:")
        st.dataframe(df)

        # Mostrar info básica
        st.write("Número de filas:", df.shape[0])
        st.write("Número de columnas:", df.shape[1])

    except Exception as e:
        st.error(f"❌ Error al leer el archivo: {e}")
else:
    st.info("📁 Por favor, sube un archivo Excel para visualizarlo.")








# Lista de columnas esperadas para fichas
nombres_columnas_fichas = [
    'ci_pasaporte', 'correo_tec', 'PrimerNombre', 'SegunNombre', 'PrimerApellido',
    'SegunApellido', 'sexo', 'genero', 'estado_civil', 'num_hijos', 'etnia',
    'fecha_nacimiento', 'tipo_parroqui', 'ciudad', 'provincia', 'pais',
    'celular', 'tiene_beca', 'estudio_otra_carrera', 'ocupacion_estudiante',
    'persona_cubre_gastos', 'recibe_ayuda', 'nombre_carrera', 'periodo_academico',
    'nombre_colegio', 'tipo_colegio', 'titulo_bachiller', 'anio_graduacion',
    'num_propiedades', 'valor_propiedades', 'num_vehiculos', 'valor_vehiculos',
    'total_ingresos', 'total_egresos', 'nombre_contacto', 'telefono_contacto',
    'tipo_sangre', 'semanas_embarazo', 'porcentaje_discapacidad',
    'nombre_discapacidad', 'nombre_enfermedades', 'vacuna_covid',
    'antecedentes_patologicos_fam', 'integrantes_familia',
    'integrantes_aporte_economico', 'cabezas_familia', 'tipo_vivienda',
    'condicion_vivienda', 'servicios_vivienda', 'tiene_carnet_conadis'
]

st.title("Visor de archivo Excel  Fichas 🗂️")

# Subir archivo
archivo_fichas = st.file_uploader("Sube tu archivo Excel de fichas", type=["xlsx"])

if archivo_fichas is not None:

    try:
        # Leer el archivo Excel
        df_fichas = pd.read_excel(archivo_fichas)
        
        # Verificar columnas
        columnas_archivo = set(df_fichas.columns)
        columnas_esperadas = set(nombres_columnas_fichas)

        if columnas_archivo == columnas_esperadas:
            st.success(" El archivo contiene todas las columnas requeridas.")
            df_fichas= limpiar_fichas (df_fichas)
            btn_cargar_datos_fichas=st.button("Migrar datos")
            if btn_cargar_datos_fichas: 
                migrar_estudiantes(df_fichas)
        else:
            st.warning(" Las columnas del archivo no coinciden con las requeridas.")
            columnas_faltantes = columnas_esperadas - columnas_archivo
            columnas_sobrantes = columnas_archivo - columnas_esperadas

            if columnas_faltantes:
                st.error(f" Columnas faltantes: {list(columnas_faltantes)}")
            if columnas_sobrantes:
                st.info(f"ℹ Columnas adicionales (no requeridas): {list(columnas_sobrantes)}")

        # Mostrar vista previa del archivo
        st.subheader("Vista previa de los datos:")
        st.dataframe(df_fichas)

        # Mostrar info básica
        st.write("Número de filas:", df_fichas.shape[0])
        st.write("Número de columnas:", df_fichas.shape[1])

    except Exception as e:
        st.error(f" Error al leer el archivo: {e}")
else:
    st.info(" Por favor, sube un archivo Excel de fichas para visualizarlo.")




