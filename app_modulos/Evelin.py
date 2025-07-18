import streamlit as st
from db_conexion import cliente_postgresql
import plotly.graph_objects as go
from collections import Counter
import pandas as pd


import psycopg2

def total_estudiantes(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")  # Asegúrate que esta función te retorne una conexión psycopg2 válida
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
    cliente = cliente_postgresql("nube")  # Debe devolver conexión psycopg2 válida
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
        # Convertir a diccionario {sexo: total_estudiantes}
        return {sexo: total for sexo, total in resultados}
    except Exception as e:
        print("Error en la consulta:", e)
        return {}
    finally:
        cursor.close()
        cliente.close()




def estudiantes_por_sexo(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")  # Tu función que retorna conexión psycopg2
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

def grafica_estudiantes_sexo(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_sexo(id_carrera=id_carrera, periodo_academico=periodo_academico)
    if not conteo:
        st.warning("No se encontraron datos para los filtros seleccionados.")
        return
    
    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,  # Si quieres un donut, quita o ajusta este parámetro
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])
        )
    ])
    fig.update_layout(
        title=f"Distribución de Estudiantes por Sexo - Carrera {id_carrera}, Periodo {periodo_academico}",
    )
    st.plotly_chart(fig)




# GENERO

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
        st.error(f"Error en la consulta: {e}")
        return {}
    finally:
        cursor.close()
        cliente.close()

def grafica_genero(id_carrera=None, periodo_academico=None):
    data = estudiantes_por_genero(id_carrera, periodo_academico)
    if not data:
        st.warning("No se encontraron datos para los filtros seleccionados.")
        return
    
    st.write("Datos para gráfico:", data)  # DEBUG: muestra datos para confirmar
    
    fig = go.Figure(data=[
        go.Pie(
            labels=list(data.keys()),
            values=list(data.values()),
            hole=0.3
        )
    ])
    fig.update_layout(
        title=f"Distribución de Estudiantes por Género - Carrera {id_carrera}, Periodo {periodo_academico}"
    )
    st.plotly_chart(fig)




# ESTADO CIVIL

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
        st.error(f"Error en la consulta: {e}")
        return {}
    finally:
        cursor.close()
        cliente.close()

def grafica_estado_civil(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_estado_civil(id_carrera, periodo_academico)
    if not conteo:
        st.warning("No se encontraron datos para los filtros seleccionados.")
        return
    
    st.write("Datos para gráfica:", conteo)  # Para verificar datos en Streamlit
    
    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])
        )
    ])
    fig.update_layout(
        title=f"Distribución de Estudiantes por Estado Civil - Carrera {id_carrera}, Periodo {periodo_academico}",
    )
    st.plotly_chart(fig)


# TIPO_PARROQUI

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

def grafica_tipo_parroquia(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_tipo_parroquia(id_carrera, periodo_academico)
    if not conteo:
        st.warning("No se encontraron datos para los filtros seleccionados.")
        return

    st.write("Datos para gráfica:", conteo)  # Para verificar datos en Streamlit
    
    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])
        )
    ])
    fig.update_layout(
        title=f"Distribución de Estudiantes por Tipo de Parroquia - Carrera {id_carrera}, Periodo {periodo_academico}"
    )
    st.plotly_chart(fig)



# TIENE_BECA

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


def grafica_tiene_beca(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_tiene_beca(id_carrera, periodo_academico)
    if not conteo:
        st.warning("No se encontraron datos para los filtros seleccionados.")
        return

    # Mapear True/False a etiquetas más amigables
    etiquetas = {"True": "Tiene Beca", "False": "No Tiene Beca", "None": "Sin dato"}
    labels = [etiquetas.get(k, k) for k in conteo.keys()]
    values = list(conteo.values())

    fig = go.Figure(data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=0.3,
            marker=dict(colors=['#00CC96', '#EF553B', '#AB63FA'])
        )
    ])

    fig.update_layout(
        title=f"Distribución de Estudiantes según Tiene Beca - Carrera {id_carrera}, Periodo {periodo_academico}"
    )

    st.plotly_chart(fig)


# OCUPACION_ESTUDIANTE

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

def grafica_ocupacion_estudiante(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_ocupacion(id_carrera, periodo_academico)
    if not conteo:
        st.warning("No se encontraron datos para los filtros seleccionados.")
        return

    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA'])
        )
    ])

    fig.update_layout(
        title=f"Distribución de Estudiantes por Ocupación - Carrera {id_carrera}, Periodo {periodo_academico}"
    )

    st.plotly_chart(fig)


# FECHA NACIMIENTO
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


def grafica_distribucion_edades(id_carrera=None, periodo_academico=None):
    edades = distribucion_edades(id_carrera, periodo_academico)

    if not edades:
        st.warning("No se encontraron datos válidos de edad para los filtros seleccionados.")
        return

    fig = go.Figure(data=[
        go.Histogram(
            x=edades,
            nbinsx=20,
            marker=dict(color='#636EFA'),
        )
    ])

    fig.update_layout(
        title=f"Distribución de Edad de Estudiantes - Carrera {id_carrera}, Periodo {periodo_academico}",
        xaxis_title="Edad",
        yaxis_title="Número de Estudiantes",
        bargap=0.1,
    )

    st.plotly_chart(fig)



# NOTAS FINALES

def obtener_promedios_con_nombre(id_carrera=None, periodo_academico=None):
    cliente = cliente_postgresql("nube")
    cursor = cliente.cursor()
    sql = """
        SELECT e.nombre_completo, p.promedio_notas
        FROM promedio_notas_por_estudiante p
        JOIN estudiante e ON p.id_estudiante = e.id_estudiante
        WHERE 1=1
    """
    params = []
    if id_carrera:
        sql += " AND p.id_carrera = %s"
        params.append(id_carrera)
    if periodo_academico:
        sql += " AND p.periodo_academico = %s"
        params.append(periodo_academico)
    try:
        cursor.execute(sql, tuple(params))
        return pd.DataFrame(cursor.fetchall(), columns=["Estudiante", "Promedio"])
    except Exception as e:
        st.error(f"Error al obtener promedios: {e}")
        return pd.DataFrame()
    finally:
        cursor.close()
        cliente.close()

def grafica_promedios_por_estudiante(id_carrera=None, periodo_academico=None):
    df = obtener_promedios_con_nombre(id_carrera, periodo_academico)
    if df.empty:
        st.warning("No hay datos de promedios por estudiante.")
        return
    fig = px.bar(df, x="Estudiante", y="Promedio", text="Promedio",
                 title="Promedio de Notas por Estudiante",
                 labels={"Estudiante": "Nombre del Estudiante", "Promedio": "Promedio de Notas"})
    fig.update_traces(textposition="outside")
    fig.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig)









# Ejemplo de uso en Streamlit
def main():
    st.title("")

    
    grafica_promedios_por_estudiante()
    
    


main()

# REVISAR SEXO DE ESTUDIANTES

