import numpy as np
import pandas as pd

import pandas as pd
import numpy as np

def limpiar_notas(df_notas):
    # 1. Convertir 'ci_pasaporte' a string y rellenar con ceros (preservando nulos)
    df_notas["ci_pasaporte"] = df_notas["ci_pasaporte"].apply(lambda x: str(x).zfill(10) if pd.notnull(x) else None)

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
    # 1. Componer 'nombres' ANTES de convertir todo a string
    df_fichas["nombres"] = (
        df_fichas["PrimerNombre"].fillna("") + " " +
        df_fichas["SegunNombre"].fillna("") + " " +
        df_fichas["PrimerApellido"].fillna("") + " " +
        df_fichas["SegunApellido"].fillna("")
    ).str.strip()

    # 2. Eliminar las columnas originales de nombres
    df_fichas.drop(columns=["PrimerNombre", "SegunNombre", "PrimerApellido", "SegunApellido"], inplace=True)

    # 3. Convertir columnas clave a string (respetando nulos)
    df_fichas["ci_pasaporte"] = df_fichas["ci_pasaporte"].apply(lambda x: str(x).zfill(10) if pd.notnull(x) else None)
    df_fichas["telefono_contacto"] = df_fichas["telefono_contacto"].apply(lambda x: str(x).zfill(10) if pd.notnull(x) else None)

    # 4. Convertir todo a string SOLO después de hacer las conversiones numéricas/booleanas
    # (lo haces más abajo, está bien evitarlo al inicio)

    # 5. Limpiar texto: strip, upper, eliminar puntos
    for col in df_fichas.select_dtypes(include=["object", "string"]).columns:
        if col != "correo_tec":
            df_fichas[col] = df_fichas[col].astype(str).str.strip().str.upper()
            df_fichas[col] = df_fichas[col].str.replace(".", "", regex=False)
    
    # 6. Tipos definidos
    columnas_enteras = ["num_hijos", "anio_graduacion", "num_propiedades", "num_vehiculos", "semanas_embarazo"]
    columnas_flotantes = ["valor_propiedades", "valor_vehiculos", "total_ingresos", "total_egresos", "porcentaje_discapacidad"]
    columnas_booleanas = ["tiene_beca", "estudio_otra_carrera", "recibe_ayuda", "tiene_carnet_conadis"]

    # 7. Limpiar enteros
    for col in columnas_enteras:
        if col in df_fichas.columns:
            df_fichas[col] = df_fichas[col].astype(str).str.replace(r"[^\d]", "", regex=True)
            df_fichas[col] = df_fichas[col].replace("", np.nan).fillna(0).astype(int)

    # 8. Limpiar flotantes
    for col in columnas_flotantes:
        if col in df_fichas.columns:
            df_fichas[col] = df_fichas[col].astype(str).str.replace(r"[^\d.]", "", regex=True)
            df_fichas[col] = df_fichas[col].replace("", np.nan).fillna(0).astype(float)

    # 9. Convertir booleanos
    for col in columnas_booleanas:
        if col in df_fichas.columns:
            df_fichas[col] = df_fichas[col].astype(str).str.strip().str.upper().replace({"SÍ": True, "SI": True, "NO": False})
            df_fichas[col] = df_fichas[col].fillna(False)

    # 10. Reemplazar nulos por 'DESCONOCIDO' en strings
    columnas_str = df_fichas.select_dtypes(include=["object", "string"]).columns
    df_fichas[columnas_str] = df_fichas[columnas_str].replace(
        to_replace=r"^\s*(nan|NaN|NAN|null|None)\s*$",
        value="DESCONOCIDO",
        regex=True
    ).fillna("DESCONOCIDO")

    # 11. Asegurar que columnas numéricas no tengan NaNs
    columnas_num = df_fichas.select_dtypes(include=["number"]).columns
    df_fichas[columnas_num] = df_fichas[columnas_num].fillna(0)

    # 12. Verificación final de nulos
    print("🔍 Valores nulos por columna:")
    print(df_fichas.isnull().sum().sort_values(ascending=False))

    return df_fichas
