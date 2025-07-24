from modulos.db_conexiones import cliente_postgresql


def migrar_info_a_tablas_fichas(df_archivo_fichas):
    # Filtrar solo las columnas necesarias
    df_estudiantes = df_archivo_fichas[[
        "ci_pasaporte", "correo_tec", "nombres", "sexo", "genero", "estado_civil", 
        "num_hijos", "etnia", "fecha_nacimiento", "tipo_parroquia", "ciudad", 
        "provincia", "pais", "celular", "tiene_beca", "estudio_otra_carrera", 
        "ocupacion_estudiante", "persona_cubre_gastos", "recibe_ayuda"
    ]]
    
    # Obtener los 'ci_pasaporte' que no existen en la base de datos
    ci_pasaporte_no_existentes = obtener_ci_no_existentes(df_estudiantes["ci_pasaporte"].unique().tolist())
    
    # Filtrar el DataFrame para obtener solo las filas con 'ci_pasaporte' no existentes
    df_estudiantes = df_estudiantes[df_estudiantes["ci_pasaporte"].isin(ci_pasaporte_no_existentes)]
    
    # Insertar los estudiantes en la base de datos
    insertar_estudiantes(df_estudiantes)



def migrar_info_a_tablas_notas(df_archivo_notas):
    pass


def insertar_estudiantes(df):
    conn = cliente_postgresql()
    
    columnas = list(df.columns)
    valores = [tuple(row) for row in df.to_numpy()]
    
    placeholders = ", ".join(["%s"] * len(columnas))
    columnas_str = ", ".join(columnas)
    
    sql = f"INSERT INTO estudiante ({columnas_str}) VALUES ({placeholders})"
    
    try:
        with conn.cursor() as cur:
            cur.executemany(sql, valores)
        conn.commit()
        print("✅ Datos insertados correctamente en la tabla 'estudiante'.")
    except Exception as e:
        conn.rollback()
        print(f"❌ Error al insertar los datos: {e}")
    finally:
        conn.close()


def obtener_ci_no_existentes(ci_list):
    conn = cliente_postgresql()

    ci_tuple = tuple(ci_list)
    
    if len(ci_tuple) == 0:
        return []

    sql = "SELECT ci_pasaporte FROM estudiante WHERE ci_pasaporte IN %s"
    
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (ci_tuple,))
            existentes = {row[0] for row in cur.fetchall()}  
            
        no_existentes = [ci for ci in ci_list if ci not in existentes]
        return no_existentes

    except Exception as e:
        print(f"❌ Error al verificar CI: {e}")
        return []
    
    finally:
        conn.close()


def obtener_id_estudiantes(ci_list):

    conn = cliente_postgresql()

    ci_tuple = tuple(ci_list)
    
    if len(ci_tuple) == 0:
        return {}

    sql = "SELECT ci_pasaporte, id_estudiante FROM estudiante WHERE ci_pasaporte IN %s"
    
    try:
        with conn.cursor() as cur:
            cur.execute(sql, (ci_tuple,))
            resultados = cur.fetchall()
        
        ci_id_dict = {row[0]: row[1] for row in resultados}
        
        return ci_id_dict

    except Exception as e:
        print(f"❌ Error al obtener los ID de los estudiantes: {e}")
        return {}
    
    finally:
        conn.close()
