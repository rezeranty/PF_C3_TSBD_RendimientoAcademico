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


def total_estudiantes(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()

    sql = """
        SELECT 
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM 
            estudiante e 
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE ea.estado_matricula NOT IN ('RETIRADO', 'DESERTOR')
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    try:
        cursor.execute(sql, tuple(params))
        resultado = cursor.fetchone()
        return resultado[0] if resultado else 0
    except Exception as e:
        print("Error en la consulta:", e)
        return None
    finally:
        cursor.close()
        cliente.close()


def estudiantes_por_sexo(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()

    sql = """
        SELECT 
            e.sexo,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM 
            estudiante e 
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE 1=1
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY e.sexo ORDER BY e.sexo"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()

        return {sexo: total for sexo, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def estudiantes_por_genero(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()

    sql = """
        SELECT 
            e.genero,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM 
            estudiante e 
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE 1=1
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY e.genero ORDER BY e.genero"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {genero: total for genero, total in resultados}
    except Exception as e:
        print(f"Error en la consulta: {e}")
        return {}
    finally:
        cursor.close()
        cliente.close()


def estudiantes_por_estado_civil(id_carrera=None, periodo_academico=None): 
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()

    sql = """
        SELECT 
            e.estado_civil,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM 
            estudiante e 
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE 1=1
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY e.estado_civil ORDER BY e.estado_civil"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {estado_civil: total for estado_civil, total in resultados}
    except Exception as e:
        print(f"Error en la consulta: {e}")
        return {}
    finally:
        cursor.close()
        cliente.close()


def estudiantes_por_tipo_parroquia(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()

    sql = """
        SELECT 
            e.tipo_parroqui,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM 
            estudiante e 
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE 1=1
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY e.tipo_parroqui ORDER BY e.tipo_parroqui"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {tipo_parroqui: total for tipo_parroqui, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def estudiantes_por_tiene_beca(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()

    sql = """
        SELECT 
            e.tiene_beca,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM 
            estudiante e
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE 1=1
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY e.tiene_beca ORDER BY e.tiene_beca"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {str(tiene_beca): total for tiene_beca, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def estudiantes_por_ocupacion(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()

    sql = """
        SELECT 
            LOWER(TRIM(e.ocupacion_estudiante)) AS ocupacion,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM 
            estudiante e
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE 1=1
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY ocupacion ORDER BY ocupacion"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {ocupacion.title(): total for ocupacion, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def distribucion_edades(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()

    sql = """
        SELECT DISTINCT 
            e.ci_pasaporte,
            DATE_PART('year', AGE(CURRENT_DATE, e.fecha_nacimiento))::int AS edad
        FROM 
            estudiante e
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE e.fecha_nacimiento IS NOT NULL
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        edades = [edad for _, edad in resultados]
        return edades
    except Exception as e:
        print("Error en la consulta:", e)
        return []
    finally:
        cursor.close()
        cliente.close()