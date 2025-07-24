import numpy as np
import pandas as pd

import pandas as pd
import numpy as np

def limpiar_notas(df_notas):
    # 1. Convertir 'ci_pasaporte' a string y rellenar con ceros (preservando nulos)
    def convertir_ci(val):
        if pd.isna(val):
            return None  # o np.nan si prefieres
        return str(val).zfill(10)

    df_notas["ci_pasaporte"] = df_notas["ci_pasaporte"].apply(convertir_ci)

    # 2. Separar código y nombre de carrera
    if "carrera" in df_notas.columns:
        split_columnas = df_notas["carrera"].astype(str).str.split("-", n=-1)
        df_notas["nombre_carrera"] = split_columnas.str[-1].str.strip().str.upper()
        df_notas["codigo_carrera"] = split_columnas.str[:-1].str.join("-").str.strip().str.upper()
        df_notas.drop(columns=["carrera"], inplace=True)

    # 3. Normalizar strings
    columnas_str = df_notas.select_dtypes(include=["object", "string"]).columns
    for col in columnas_str:
        df_notas[col] = df_notas[col].astype(str)
        df_notas[col] = df_notas[col].str.strip().str.upper()
        df_notas[col] = df_notas[col].replace(
            to_replace=r"^\s*(nan|NaN|NAN|null|None)\s*$",
            value="DESCONOCIDO",
            regex=True
        ).fillna("DESCONOCIDO")

    # 4. Rellenar numéricos
    columnas_num = df_notas.select_dtypes(include=["number"]).columns
    df_notas[columnas_num] = df_notas[columnas_num].fillna(0)

    # 5. Renombrar columnas si existen
    if "asignatura" in df_notas.columns:
        df_notas.rename(columns={"asignatura": "nombre_asignatura"}, inplace=True)

    # 6. Verificación de nulos
    print("🔍 Valores nulos por columna (notas):")
    print(df_notas.isnull().sum().sort_values(ascending=False))

    return df_notas


def limpiar_fichas(df_fichas):
    def convertir_ci(val):
        if pd.isna(val):
            return None
        return str(val).zfill(10)

    df_fichas["ci_pasaporte"] = df_fichas["ci_pasaporte"].apply(convertir_ci)
    df_fichas["telefono_contacto"] = df_fichas["telefono_contacto"].apply(convertir_ci)

    # Convertir explícitamente a str antes de la concatenación
    df_fichas["nombres"] = (
        df_fichas["PrimerNombre"].fillna("").astype(str) + " " +
        df_fichas["SegunNombre"].fillna("").astype(str) + " " +
        df_fichas["PrimerApellido"].fillna("").astype(str) + " " +
        df_fichas["SegunApellido"].fillna("").astype(str)
    ).str.strip()

    df_fichas.drop(columns=["PrimerNombre", "SegunNombre", "PrimerApellido", "SegunApellido"], inplace=True)

    for col in df_fichas.select_dtypes(include=["object", "string"]).columns:
        if col != "correo_tec" and col != "codigo_carrera":
            df_fichas[col] = df_fichas[col].astype(str).str.strip().str.upper()
            df_fichas[col] = df_fichas[col].str.replace(".", "", regex=False)

    columnas_enteras = ["num_hijos", "anio_graduacion", "num_propiedades", "num_vehiculos", "semanas_embarazo"]
    columnas_flotantes = ["valor_propiedades", "valor_vehiculos", "total_ingresos", "total_egresos", "porcentaje_discapacidad"]
    columnas_booleanas = ["tiene_beca", "estudio_otra_carrera", "recibe_ayuda", "tiene_carnet_conadis"]

    for col in columnas_enteras:
        if col in df_fichas.columns:
            df_fichas[col] = df_fichas[col].astype(str).str.replace(r"[^\d]", "", regex=True)
            df_fichas[col] = df_fichas[col].replace("", np.nan).fillna(0).astype(int)

    for col in columnas_flotantes:
        if col in df_fichas.columns:
            df_fichas[col] = df_fichas[col].astype(str).str.replace(r"[^\d.]", "", regex=True)
            df_fichas[col] = df_fichas[col].replace("", np.nan).fillna(0).astype(float)

    for col in columnas_booleanas:
        if col in df_fichas.columns:
            df_fichas[col] = df_fichas[col].astype(str).str.strip().str.upper().replace({"SÍ": True, "SI": True, "NO": False})
            df_fichas[col] = df_fichas[col].fillna(False)

    columnas_str = df_fichas.select_dtypes(include=["object", "string"]).columns
    df_fichas[columnas_str] = df_fichas[columnas_str].replace(
        to_replace=r"^\s*(nan|NaN|NAN|null|None)\s*$",
        value="DESCONOCIDO",
        regex=True
    ).fillna("DESCONOCIDO")
    
    if "codigo_carrera" in df_fichas.columns:
        df_fichas["codigo_carrera"] = df_fichas["codigo_carrera"].fillna(np.nan)

    columnas_num = df_fichas.select_dtypes(include=["number"]).columns
    df_fichas[columnas_num] = df_fichas[columnas_num].fillna(0)

    print("🔍 Valores nulos por columna:")
    print(df_fichas.isnull().sum().sort_values(ascending=False))
    print(df_fichas.sample(5))

    return df_fichas
