import plotly.graph_objects as go

from app_modulos.db_postgres_consultas import (
    estudiantes_por_sexo, estudiantes_por_genero, estudiantes_por_estado_civil,
    estudiantes_por_tipo_parroquia, estudiantes_por_tiene_beca,
    estudiantes_por_ocupacion, distribucion_edades
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
    data = estudiantes_por_genero(id_carrera, None if periodo_academico == "TODOS" else periodo_academico)
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
    conteo = estudiantes_por_estado_civil(id_carrera, None if periodo_academico == "TODOS" else periodo_academico)
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
    conteo = estudiantes_por_tipo_parroquia(id_carrera, None if periodo_academico == "TODOS" else periodo_academico)
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
    conteo = estudiantes_por_tiene_beca(id_carrera, None if periodo_academico == "TODOS" else periodo_academico)
    if not conteo:
        return None

    etiquetas = {"True": "Tiene Beca", "False": "No Tiene Beca", "None": "Sin dato"}
    labels = [etiquetas.get(k, k) for k in conteo.keys()]
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

    fig.update_layout(estilo_layout(
        f"Distribución según Tiene Beca"
    ))
    return fig


def grafica_ocupacion_estudiante(id_carrera=None, periodo_academico=None):
    conteo = estudiantes_por_ocupacion(id_carrera, None if periodo_academico == "TODOS" else periodo_academico)
    if not conteo:
        return None

    fig = go.Figure(data=[
        go.Pie(
            labels=list(conteo.keys()),
            values=list(conteo.values()),
            hole=0.3,
            textposition='inside',
            textinfo='percent+label',
            marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA'])
        )
    ])

    fig.update_layout(estilo_layout(
        f"Distribución por Ocupación"
    ))
    return fig


def grafica_distribucion_edades(id_carrera=None, periodo_academico=None):
    edades = distribucion_edades(id_carrera, None if periodo_academico == "TODOS" else periodo_academico)
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


