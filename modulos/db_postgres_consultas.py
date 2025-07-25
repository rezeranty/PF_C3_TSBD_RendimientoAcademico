from modulos.db_conexiones import cliente_postgresql
 
from psycopg2.extras import RealDictCursor

def obtener_carreras(periodo_academico=None):
    try:
        cliente = cliente_postgresql()
        cursor = cliente.cursor()

        if periodo_academico:
            sql = """
                SELECT DISTINCT c.id_carrera, c.codigo_carrera, c.nombre_carrera
                FROM carrera c
                JOIN estudiante_carrera ec ON c.id_carrera = ec.id_carrera
                WHERE ec.periodo_academico = %s
                ORDER BY c.nombre_carrera ASC
            """
            cursor.execute(sql, (periodo_academico,))
        else:
            sql = "SELECT * FROM carrera ORDER BY nombre_carrera ASC"
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
        cliente = cliente_postgresql()
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
    cliente = cliente_postgresql()
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
    cliente = cliente_postgresql()
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
    cliente = cliente_postgresql()
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
    cliente = cliente_postgresql()
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
    cliente = cliente_postgresql()
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
    cliente = cliente_postgresql()
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
    cliente = cliente_postgresql()
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
    cliente = cliente_postgresql()
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


def estudiantes_por_tipo_colegio(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    sql = """
        SELECT 
            UPPER(TRIM(cg.tipo_colegio)) AS tipo_colegio,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM 
            colegio_graduacion cg
        INNER JOIN estudiante e ON cg.id_estudiante = e.id_estudiante
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE cg.tipo_colegio IS NOT NULL
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY tipo_colegio ORDER BY tipo_colegio"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {tipo: total for tipo, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def estudiantes_con_beca(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    sql = """
        SELECT 
            CASE 
                WHEN e.tiene_beca = TRUE THEN 'Con Beca'
                WHEN e.tiene_beca = FALSE THEN 'Sin Beca'
                ELSE 'No Especificado'
            END AS beca_estado,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM estudiante e
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE e.tiene_beca IS NOT NULL
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY beca_estado ORDER BY beca_estado"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {estado: total for estado, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def ocupacion_estudiante_frecuencia(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    sql = """
        SELECT 
            e.ocupacion_estudiante,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM estudiante e
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE e.ocupacion_estudiante IS NOT NULL AND e.ocupacion_estudiante <> ''
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY e.ocupacion_estudiante ORDER BY total_estudiantes DESC"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {ocupacion: total for ocupacion, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def condicion_vivienda_frecuencia(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    sql = """
        SELECT 
            v.condicion_vivienda,
            COUNT(DISTINCT e.ci_pasaporte) AS total_estudiantes
        FROM vivienda v
        INNER JOIN estudiante e ON v.id_estudiante = e.id_estudiante
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        INNER JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE v.condicion_vivienda IS NOT NULL AND v.condicion_vivienda <> ''
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY v.condicion_vivienda ORDER BY total_estudiantes DESC"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {condicion: total for condicion, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close() 


def frecuencia_numero_matricula(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    sql = """
        SELECT 
            ea.numero_matricula,
            COUNT(DISTINCT ec.id_estudiante) AS total_estudiantes
        FROM estudiante_asignatura ea
        INNER JOIN estudiante_carrera ec ON ea.id_estudiante_carrera = ec.id_estudiante_carrera
        WHERE ea.numero_matricula IS NOT NULL
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY ea.numero_matricula ORDER BY ea.numero_matricula"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {numero_matricula: total for numero_matricula, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def porcentaje_asistencia_promedio(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    sql = """
        SELECT 
            ec.id_estudiante_carrera,
            AVG(ea.porcentaje_asistencia) AS porcentaje_asistencia_promedio
        FROM estudiante_carrera ec
        JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
        WHERE ea.porcentaje_asistencia IS NOT NULL
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += " GROUP BY ec.id_estudiante_carrera"

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        # Extraemos solo los valores promedio
        porcentajes = [row[1] for row in resultados]
        return porcentajes
    except Exception as e:
        print("Error en la consulta:", e)
        return []
    finally:
        cursor.close()
        cliente.close()


def estado_estudiante_frecuencia(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    sql = """
    WITH estados_por_estudiante AS (
        SELECT
            ec.id_estudiante,
            ea.estado_estudiante,
            COUNT(*) AS veces
        FROM estudiante_asignatura ea
        INNER JOIN estudiante_carrera ec ON ea.id_estudiante_carrera = ec.id_estudiante_carrera
        WHERE ea.estado_estudiante IS NOT NULL AND ea.estado_estudiante <> ''
    """

    params = []

    if id_carrera is not None:
        sql += " AND ec.id_carrera = %s"
        params.append(id_carrera)

    if periodo_academico is not None:
        sql += " AND ec.periodo_academico = %s"
        params.append(periodo_academico)

    sql += """
        GROUP BY ec.id_estudiante, ea.estado_estudiante
    ),
    estado_global AS (
        SELECT
            id_estudiante,
            estado_estudiante
        FROM (
            SELECT
                id_estudiante,
                estado_estudiante,
                ROW_NUMBER() OVER (PARTITION BY id_estudiante ORDER BY veces DESC) AS rn
            FROM estados_por_estudiante
        ) sub
        WHERE rn = 1
    )
    SELECT
        eg.estado_estudiante,
        COUNT(*) AS total_estudiantes
    FROM estado_global eg
    WHERE 1=1
    """
    sql += """
    GROUP BY eg.estado_estudiante
    ORDER BY total_estudiantes DESC
    """

    try:
        cursor.execute(sql, tuple(params))
        resultados = cursor.fetchall()
        return {estado: total for estado, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def estudiantes_cabeza_familia():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    sql = """
        SELECT
            COUNT(*) FILTER (WHERE UPPER(cabezas_familia) LIKE '%ESTUDIANTE%') AS con_estudiante,
            COUNT(*) FILTER (WHERE UPPER(cabezas_familia) NOT LIKE '%ESTUDIANTE%') AS sin_estudiante
        FROM familia;
    """

    try:
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado is None or len(resultado) < 2:
            return {}
        return {
            'Cabeza de Familia (Estudiante)': resultado[0],
            'No Cabeza de Familia': resultado[1]
        }
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()


def estudiantes_aporte_economico():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    sql = """
        SELECT
            COUNT(*) FILTER (WHERE UPPER(integrantes_aporte_economico) LIKE '%ESTUDIANTE%') AS con_estudiante,
            COUNT(*) FILTER (WHERE UPPER(integrantes_aporte_economico) NOT LIKE '%ESTUDIANTE%') AS sin_estudiante
        FROM familia;
    """

    try:
        cursor.execute(sql)
        resultado = cursor.fetchone()
        if resultado is None or len(resultado) < 2:
            return {}
        return {
            'Estudiante Aporta': resultado[0],
            'No Aporta': resultado[1]
        }
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()

