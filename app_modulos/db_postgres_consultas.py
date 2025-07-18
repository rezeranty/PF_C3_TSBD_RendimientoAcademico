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


import psycopg2

def obtener_total_estudiantes_activos(id_carrera=None, periodo=None):
    try:
        cliente = cliente_postgresql('nube')
        cursor = cliente.cursor()

        # Base query
        sql = """
            SELECT COUNT(DISTINCT ec.id_estudiante)
            FROM estudiante_carrera ec
            JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
            WHERE ea.estado_estudiante != 'RETIRADO'
        """

        filtros = []
        valores = []

        if id_carrera:
            filtros.append("ec.id_carrera = %s")
            valores.append(id_carrera)
        
        if periodo:
            filtros.append("ec.periodo_academico = %s")
            valores.append(periodo)

        # Agregar condiciones dinámicamente
        if filtros:
            sql += " AND " + " AND ".join(filtros)

        cursor.execute(sql, tuple(valores))
        total = cursor.fetchone()[0]

        return total

    except Exception as e:
        print(f"Error al obtener el total de estudiantes activos: {e}")
        return 0
    finally:
        if cursor:
            cursor.close()
        if cliente:
            cliente.close()

