from app_modulos.db_conexion import cliente_postgresql

def obtener_carreras(periodo_academico=None):
    try:
        cliente = cliente_postgresql('nube')
        cursor = cliente.cursor()

        if periodo_academico:
            sql = """
                SELECT DISTINCT c.id_carrera, c.codigo_carrera, c.nombre_carrera
                FROM carrera c
                JOIN estudiante_carrera ec ON c.id_carrera = ec.id_carrera
                WHERE ec.periodo_academico = %s
            """
            cursor.execute(sql, (periodo_academico,))
        else:
            sql = "SELECT * FROM carrera"
            cursor.execute(sql)

        carreras = cursor.fetchall()
        return carreras

    except Exception as e:
        print(f"Error al obtener carreras: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if cliente:
            cliente.close()


def obtener_periodos_academicos():
    try:
        cliente = cliente_postgresql('nube')
        cursor = cliente.cursor()

        sql = "SELECT DISTINCT periodo_academico FROM estudiante_carrera ORDER BY periodo_academico ASC"
        cursor.execute(sql)
        periodos = cursor.fetchall()

        return periodos
    except Exception as e:
        print(f"Error al obtener periodos: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if cliente:
            cliente.close()