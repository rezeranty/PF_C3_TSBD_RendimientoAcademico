import streamlit as st
from db_conexion import cliente_postgresql
import plotly.graph_objects as go
import pandas as pd
from collections import Counter
from collections import Counter, defaultdict

import plotly.express as px


import psycopg2

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


def grafica_distribucion_edades(id_carrera=None, periodo_academico=None, nombre_carrera=None):
    edades = distribucion_edades(id_carrera, periodo_academico)

    if not edades:
        return None

    fig = go.Figure(data=[
        go.Histogram(
            x=edades,
            nbinsx=20,
            marker=dict(color='#636EFA'),
        )
    ])

    fig.update_layout(
        title=f"Distribución de Edad<br>Carrera: {nombre_carrera}<br>Periodo: {periodo_academico}",
        xaxis_title="Edad",
        yaxis_title="Número de Estudiantes",
        bargap=0.1,
    )

    return fig

# TIPO COLEGIO
def estudiantes_por_tipo_colegio(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
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

def grafica_tipo_colegio(id_carrera=None, periodo_academico=None, nombre_carrera=None):
    datos = estudiantes_por_tipo_colegio(id_carrera, periodo_academico)

    if not datos:
        return None

    fig = go.Figure(data=[
        go.Bar(
            x=list(datos.keys()),
            y=list(datos.values()),
            marker_color='indigo'
        )
    ])

    fig.update_layout(
        title=f"Tipo de Colegio de Procedencia<br>Carrera: {nombre_carrera}<br>Periodo: {periodo_academico}",
        xaxis_title="Tipo de Colegio",
        yaxis_title="Número de Estudiantes",
        xaxis_tickangle=-45
    )

    return fig


# TIENE BECA
def estudiantes_con_beca(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
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
def grafica_tiene_beca(id_carrera=None, periodo_academico=None, nombre_carrera=None):
    datos = estudiantes_con_beca(id_carrera, periodo_academico)

    if not datos:
        return None

    fig = go.Figure(data=[
        go.Bar(
            x=list(datos.keys()),
            y=list(datos.values()),
            marker_color='teal'
        )
    ])

    fig.update_layout(
        title=f"Distribución de Estudiantes según Beca<br>Carrera: {nombre_carrera}<br>Periodo: {periodo_academico}",
        xaxis_title="Estado de Beca",
        yaxis_title="Número de Estudiantes",
        xaxis_tickangle=-20
    )

    return fig


# OCUPACIÓN ESTUDIANTE
def ocupacion_estudiante_frecuencia(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
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

def grafica_ocupacion_estudiante(id_carrera=None, periodo_academico=None, nombre_carrera=None):
    datos = ocupacion_estudiante_frecuencia(id_carrera, periodo_academico)

    if not datos:
        return None

    fig = go.Figure(data=[
        go.Bar(
            x=list(datos.keys()),
            y=list(datos.values()),
            marker_color='indigo'
        )
    ])

    fig.update_layout(
        title=f"Ocupación de los Estudiantes<br>Carrera: {nombre_carrera}<br>Periodo: {periodo_academico}",
        xaxis_title="Ocupación",
        yaxis_title="Número de Estudiantes",
        xaxis_tickangle=-20
    )

    return fig

# CONDICION VIVIENDA
def condicion_vivienda_frecuencia(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
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

def grafica_condicion_vivienda(id_carrera=None, periodo_academico=None, nombre_carrera=None):
    datos = condicion_vivienda_frecuencia(id_carrera, periodo_academico)

    if not datos:
        st.warning("No hay datos para mostrar en la gráfica de Condición de Vivienda.")
        return None

    fig = go.Figure(data=[
        go.Bar(
            x=list(datos.keys()),
            y=list(datos.values()),
            marker_color='crimson'
        )
    ])

    fig.update_layout(
        title=f"Condición de Vivienda de los Estudiantes<br>Carrera: {nombre_carrera}<br>Periodo: {periodo_academico}",
        xaxis_title="Condición de Vivienda",
        yaxis_title="Número de Estudiantes",
        xaxis_tickangle=-20
    )

    return fig


# ECONOMÍA ESTUDIANTE
def ingresos_egresos_por_carrera_periodo(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()

    sql = """
        SELECT 
            SUM(economia.total_ingresos) AS suma_ingresos,
            SUM(economia.total_egresos) AS suma_egresos
        FROM economia_estudiante economia
        INNER JOIN estudiante e ON economia.id_estudiante = e.id_estudiante
        INNER JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
        WHERE 1=1
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
        if resultado:
            return {"Ingresos": resultado[0] or 0, "Egresos": resultado[1] or 0}
        else:
            return {"Ingresos": 0, "Egresos": 0}
    except Exception as e:
        print("Error en la consulta:", e)
        return {"Ingresos": 0, "Egresos": 0}
    finally:
        cursor.close()
        cliente.close()


def grafica_ingresos_vs_egresos(id_carrera=None, periodo_academico=None, nombre_carrera=None):
    datos = ingresos_egresos_por_carrera_periodo(id_carrera, periodo_academico)

    if not datos or (datos["Ingresos"] == 0 and datos["Egresos"] == 0):
        st.warning("No se encontraron datos de ingresos y egresos para los filtros seleccionados.")
        return None

    fig = go.Figure(data=[
        go.Bar(
            name="Ingresos",
            x=["Ingresos"],
            y=[datos["Ingresos"]],
            marker_color='green'
        ),
        go.Bar(
            name="Egresos",
            x=["Egresos"],
            y=[datos["Egresos"]],
            marker_color='red'
        )
    ])

    fig.update_layout(
        title=f"Ingresos vs Egresos Totales<br>Carrera: {nombre_carrera}<br>Periodo: {periodo_academico}",
        yaxis_title="Monto (USD)",
        xaxis_title="Concepto",
        barmode='group'
    )

    return fig



# NUMERO MATRICULA
def frecuencia_numero_matricula(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
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


def grafica_frecuencia_numero_matricula(id_carrera=None, periodo_academico=None, nombre_carrera=None):
    datos = frecuencia_numero_matricula(id_carrera, periodo_academico)

    if not datos:
        st.warning("No se encontraron datos de número de matrícula para los filtros seleccionados.")
        return None

    fig = go.Figure(data=[
        go.Bar(
            x=list(datos.keys()),
            y=list(datos.values()),
            marker_color='orange'
        )
    ])

    fig.update_layout(
        title=f"Frecuencia de Número de Matrículas por Estudiante<br>Carrera: {nombre_carrera}<br>Periodo: {periodo_academico}",
        xaxis_title="Número de Matrículas (Veces que repitió materia)",
        yaxis_title="Número de Estudiantes",
        xaxis=dict(tickmode='linear'),
        bargap=0.2
    )

    return fig


# PORCENTAJE ASISTENCIA
def porcentaje_asistencia_promedio(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
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


def grafica_porcentaje_asistencia_promedio(id_carrera=None, periodo_academico=None, nombre_carrera=None):
    datos = porcentaje_asistencia_promedio(id_carrera, periodo_academico)

    if not datos:
        st.warning("No se encontraron datos válidos de porcentaje de asistencia para los filtros seleccionados.")
        return None

    fig = go.Figure(data=[
        go.Histogram(
            x=datos,
            nbinsx=20,
            marker=dict(color='mediumseagreen'),
        )
    ])

    fig.update_layout(
        title=f"Distribución del Porcentaje Promedio de Asistencia<br>Carrera: {nombre_carrera}, Periodo: {periodo_academico}",
        xaxis_title="Porcentaje Promedio de Asistencia",
        yaxis_title="Número de Estudiantes",
        bargap=0.1,
    )

    return fig


# ESTADO ESTUDIANTE
def estado_estudiante_frecuencia(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
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

    # Los filtros ya aplicados en la CTE, no los repetimos acá

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



def grafica_estado_estudiante(id_carrera=None, periodo_academico=None, nombre_carrera=None):
    datos = estado_estudiante_frecuencia(id_carrera, periodo_academico)

    if not datos:
        return None

    fig = go.Figure(data=[
        go.Bar(
            x=list(datos.keys()),
            y=list(datos.values()),
            marker_color='mediumseagreen'
        )
    ])

    fig.update_layout(
        title=f"Estado Académico de los Estudiantes<br>Carrera: {nombre_carrera}<br>Periodo: {periodo_academico}",
        xaxis_title="Estado Estudiante",
        yaxis_title="Número de Estudiantes",
        xaxis_tickangle=-20
    )

    return fig




def main():

    st.plotly_chart(gr())
    
    
main()