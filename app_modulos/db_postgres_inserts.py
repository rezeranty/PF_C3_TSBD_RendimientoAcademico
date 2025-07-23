from app_modulos.db_conexion import cliente_postgresql
#Cambiar todo a funciones de postrgres, se usa la librería psycopg2-binary 


def crear_estudiantes(df_estudiantes):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "ci_pasaporte", "correo_tec", "nombres", "sexo", "genero", "estado_civil",
        "num_hijos", "etnia", "fecha_nacimiento", "tipo_parroqui", "ciudad",
        "provincia", "pais", "celular", "tiene_beca", "estudio_otra_carrera",
        "ocupacion_estudiante", "persona_cubre_gastos", "recibe_ayuda"
    ]

    sql = f"""
    INSERT INTO estudiante ({','.join(columnas)}) 
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_estudiantes[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de estudiantes: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


# Puedes repetir el mismo patrón para las demás funciones

def crear_estudiantes_colegio(df_colegios):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_estudiante", "nombre_colegio", "tipo_colegio", "titulo_bachiller", "anio_graduacion"
    ]

    sql = f"""
    INSERT INTO colegio_graduacion ({','.join(columnas)}) 
    VALUES ({','.join(['%s'] * len(columnas))}) 
    ON CONFLICT DO NOTHING;
    """
    valores = df_colegios[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de colegios: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_propiedades_extra(df_propiedades):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_estudiante", "num_propiedades", "valor_propiedades", "num_vehiculos", "valor_vehiculos"
    ]

    sql = f"""
    INSERT INTO propiedades_extra ({','.join(columnas)}) 
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_propiedades[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de propiedades: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_economia_estudiante(df_economia):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_estudiante", "total_ingresos", "total_egresos"
    ]

    sql = f"""
    INSERT INTO economia_estudiante ({','.join(columnas)})
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_economia[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de economia: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_contacto_emergencia(df_contacto_emergencia):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_estudiante", "nombre_contacto", "telefono_contacto"
    ]

    sql = f"""
    INSERT INTO contacto_emergencia ({','.join(columnas)})
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_contacto_emergencia[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de contacto emergencia: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_datos_salud(df_datos_salud):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_estudiante", "tipo_sangre", "semanas_embarazo", "porcentaje_discapacidad", "nombre_discapacidad", 
        "nombre_enfermedades", "vacuna_covid", "antecedentes_patologicos_fam", "tiene_carnet_conadis"
    ]

    sql = f"""
    INSERT INTO datos_salud ({','.join(columnas)})
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_datos_salud[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de salud: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_familia(df_familia):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_estudiante", "integrantes_familia", "integrantes_aporte_economico", "cabezas_familia"
    ]

    sql = f"""
    INSERT INTO familia ({','.join(columnas)})
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_familia[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de familia: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_vivienda(df_vivienda):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_estudiante", "tipo_vivienda", "condicion_vivienda", "servicios_vivienda"
    ]

    sql = f"""
    INSERT INTO vivienda ({','.join(columnas)})
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_vivienda[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de vivienda: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_carreras(df_carreras):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "codigo_carrera", "nombre_carrera"
    ]

    sql = f"""
    INSERT INTO carrera ({','.join(columnas)})
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_carreras[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de carrera: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_estudiantes_carreras(df_carreras):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_carrera", "id_estudiante", "ciclo_carrera", "periodo_academico", "paralelo"
    ]

    sql = f"""
    INSERT INTO estudiante_carrera ({','.join(columnas)})
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_carreras[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de estudiante_carrera: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_asignaturas(df_asignaturas):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_carrera", "nombre_asignatura"
    ]

    sql = f"""
    INSERT INTO asignatura ({','.join(columnas)})
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_asignaturas[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de asignatura: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()


def crear_estudiantes_asignaturas(df_estudiantes_asignaturas):
    cliente = cliente_postgresql('nube')
    cursor = cliente.cursor()

    columnas = [
        "id_estudiante_carrera", "id_asignatura", "numero_matricula", "porcentaje_asistencia",
        "nota_final", "estado_estudiante", "estado_matricula", "tipo_ingreso"
    ]

    sql = f"""
    INSERT INTO estudiante_asignatura ({','.join(columnas)})
    VALUES ({','.join(['%s'] * len(columnas))})
    ON CONFLICT DO NOTHING;
    """
    valores = df_estudiantes_asignaturas[columnas].values.tolist()
    try:
        cursor.executemany(sql, valores)
        cliente.commit()
    except Exception as e:
        print(f"Error al insertar datos de estudiante_asignatura: {e}")
        cliente.rollback()
    finally:
        cursor.close()
        cliente.close()
