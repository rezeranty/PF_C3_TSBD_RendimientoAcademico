import streamlit as st
from db_conexion import cliente_postgresql
import plotly.graph_objects as go
import pandas as pd


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




def main():

    st.plotly_chart(grafica_distribucion_edades)
    
    
main()