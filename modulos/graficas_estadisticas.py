import plotly.graph_objects as go
import pandas as pd
import plotly.express as px


from modulos.db_postgres_consultas import (
    estudiantes_por_sexo, estudiantes_por_genero, estudiantes_por_estado_civil,
    estudiantes_por_tipo_parroquia, estudiantes_por_tiene_beca,
    estudiantes_por_ocupacion, distribucion_edades, estudiantes_por_tipo_colegio,condicion_vivienda_frecuencia,
    frecuencia_numero_matricula, porcentaje_asistencia_promedio,
    estado_estudiante_frecuencia, estudiantes_cabeza_familia,estudiantes_aporte_economico
)


def estilo_layout(titulo):
    return dict(
        title={
            'text': titulo,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16}
        },
        margin=dict(t=40, b=40, l=20, r=20),
        height=350
    )


def grafica_estudiantes_sexo(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_sexo(id_carrera, periodo_academico)
    if not conteo:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])
        )
    ])
    fig.update_layout(estilo_layout(
        f"Distribución por Sexo"
    ))
    return fig


def grafica_genero(id_carrera=None, periodo_academico=None):
    data = estudiantes_por_genero(id_carrera, periodo_academico)
    if not data:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(data.keys()),
            values=list(data.values()),
            hole=0.3,
            textposition='inside',
            textinfo='percent+label'
        )
    ])
    fig.update_layout(estilo_layout(
        f"Distribución por Género"
    ))
    return fig


def grafica_estado_civil(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_estado_civil(id_carrera, periodo_academico)
    if not conteo:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])
        )
    ])
    fig.update_layout(estilo_layout(
        f"Distribución por Estado Civil"
    ))
    return fig


def grafica_tipo_parroquia(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_tipo_parroquia(id_carrera, periodo_academico)
    if not conteo:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])
        )
    ])
    fig.update_layout(estilo_layout(
        f"Distribución por Tipo de Parroquia"
    ))
    return fig


def grafica_tiene_beca(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_tiene_beca(id_carrera, periodo_academico)
    if not conteo:
        return None

    etiquetas = {
        True: "Tiene Beca",
        False: "No Tiene Beca",
        None: "Sin dato"
    }

    labels = [etiquetas.get(k, str(k)) for k in conteo.keys()]
    values = list(conteo.values())

    fig = go.Figure(data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=0.3,
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#00CC96', '#EF553B', '#AB63FA'])
        )
    ])

    fig.update_layout(estilo_layout("Distribución según Tiene Beca"))
    return fig


def grafica_ocupacion_estudiante(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_ocupacion(id_carrera, periodo_academico)
    if not conteo:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3, 
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])
        )
    ])

    fig.update_layout(estilo_layout(
        "Distribución por Ocupación del Estudiante"
    ))
    return fig


def grafica_distribucion_edades(id_carrera=None, periodo_academico=None):
    edades = distribucion_edades(id_carrera, periodo_academico)
    if not edades:
        return None

    fig = go.Figure(data=[
        go.Histogram(
            x=edades,
            nbinsx=20,
            marker=dict(color='#636EFA')
        )
    ])

    fig.update_layout(
        title={
            'text': f"Distribución de Edad",
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16}
        },
        xaxis_title="Edad",
        yaxis_title="Número de Estudiantes",
        bargap=0.1,
        margin=dict(t=40, b=40, l=20, r=20),
        height=350
    )

    return fig


def grafica_frecuencia_numero_matricula(id_carrera=None, periodo_academico=None):
    datos = frecuencia_numero_matricula(id_carrera, periodo_academico)

    if not datos:
        return None

    fig = go.Figure(data=[go.Pie(
        labels=list(datos.keys()),
        values=list(datos.values()),
        hole=0.4,  
        marker=dict(colors=['#ffb84d', '#ffa31a', '#e69500', '#cc8400', '#b37400']), 
        textinfo='percent+label'
    )])

    fig.update_layout(
        title="Frecuencia de Número de Matrículas por Estudiante"
    )

    return fig


def grafica_porcentaje_asistencia_promedio(id_carrera=None, periodo_academico=None):
    datos = porcentaje_asistencia_promedio(id_carrera, periodo_academico)

    if not datos:
        return None

    df = pd.Series(datos)
    bins = [0, 50, 60, 70, 80, 90, 100]
    labels = ['0-49%', '50-59%', '60-69%', '70-79%', '80-89%', '90-100%']
    grupos = pd.cut(df, bins=bins, labels=labels, include_lowest=True)
    conteo = grupos.value_counts().sort_index()

    fig = go.Figure(data=[go.Pie(
        labels=conteo.index,
        values=conteo.values,
        hole=0.4,
        marker=dict(colors=px.colors.sequential.Greens),
        textinfo='percent+label'
    )])

    fig.update_layout(
        title="Distribución del Porcentaje Promedio de Asistencia (Agrupada)"
    )

    return fig


def grafica_estado_estudiante(id_carrera=None, periodo_academico=None): 
    datos = estado_estudiante_frecuencia(id_carrera, periodo_academico)

    if not datos:
        return None

    fig = go.Figure(data=[go.Pie(
        labels=list(datos.keys()),
        values=list(datos.values()),
        hole=0.4,  
        marker=dict(colors=['mediumseagreen', 'lightgreen', 'darkseagreen', 'seagreen']), 
        textinfo='percent+label'  
    )])

    fig.update_layout(
        title="Estado Académico de los Estudiantes"
    )

    return fig


def grafica_condicion_vivienda(id_carrera=None, periodo_academico=None):
    datos = condicion_vivienda_frecuencia(id_carrera, periodo_academico)

    if not datos:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(datos.keys()),
            values=list(datos.values()),
            hole=0.3,
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A'])
        )
    ])

    fig.update_layout(estilo_layout(
        "Condición de Vivienda de los Estudiantes"
    ))

    return fig


def grafica_tipo_colegio(id_carrera=None, periodo_academico=None):
    datos = estudiantes_por_tipo_colegio(id_carrera, periodo_academico)

    if not datos:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(datos.keys()),
            values=list(datos.values()),
            hole=0.3,
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#19D3F3', '#FF6692', '#B6E880', '#FF97FF', '#FECB52'])
        )
    ])

    fig.update_layout(estilo_layout(
        "Tipo de Colegio de Procedencia"
    ))

    return fig


def grafica_cabeza_familia():
    conteo = estudiantes_cabeza_familia()
    if not conteo:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#00CC96', '#EF553B'])
        )
    ])
    fig.update_layout(
        title={
            'text': 'Proporción Total de Estudiantes como Cabezas de Familia',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16}
        },
        height=350,
        margin=dict(t=40, b=40, l=20, r=20)
    )
    return fig


def grafica_aporte_economico():
    conteo = estudiantes_aporte_economico()
    if not conteo:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#636EFA', '#FFA15A'])
        )
    ])
    fig.update_layout(
        title={
            'text': 'Proporción Total de Estudiantes que Aportan Económicamente',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16}
        },
        height=350,
        margin=dict(t=40, b=40, l=20, r=20)
    )
    return fig

