import pandas as pd
from db_conexion import cliente_mongodb, cliente_postgresql


def obtener_datos_prediccion():
    query = """
    SELECT DISTINCT
        e.id_estudiante,
        e.ci_pasaporte,
        e.nombres,
        c.id_carrera,
        c.nombre_carrera,
        ec.periodo_academico,
        e.num_hijos,
        e.tipo_parroqui,
        e.ocupacion_estudiante,
        ds.semanas_embarazo,
        ds.porcentaje_discapacidad,
        ds.nombre_enfermedades,
        ds.tiene_carnet_conadis,
        ee.total_ingresos,
        ee.total_egresos,
        f.integrantes_aporte_economico,
        f.cabezas_familia,
        v.condicion_vivienda,
        ea.numero_matricula,
        ea.porcentaje_asistencia,
        ea.estado_estudiante
    FROM estudiante e
    JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
    JOIN carrera c ON ec.id_carrera = c.id_carrera
    JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
    LEFT JOIN datos_salud ds ON e.id_estudiante = ds.id_estudiante
    LEFT JOIN economia_estudiante ee ON e.id_estudiante = ee.id_estudiante
    LEFT JOIN (
        SELECT DISTINCT ON (id_estudiante) * FROM familia
    ) f ON e.id_estudiante = f.id_estudiante
    LEFT JOIN (
        SELECT DISTINCT ON (id_estudiante) * FROM vivienda
    ) v ON e.id_estudiante = v.id_estudiante
    WHERE ec.periodo_academico = '2025-1P'
    ORDER BY e.ci_pasaporte, ec.periodo_academico;
    """

    cliente= cliente_postgresql()
    df = pd.read_sql_query(query, cliente)
    cliente.close()

    df.to_excel("datos_prediccion.xlsx", index=False)
 

def migrar_predicciones_mongodb():
    cliente = cliente_mongodb()
    if cliente:
        db = cliente["fichasnotasdb"]

        archivos = {
            "resultados_modelo1_simple.xlsx": pd.read_excel("/content/resultados_modelo1_simple.xlsx"),
            "resultados_modelo2_dropout.xlsx": pd.read_excel("/content/resultados_modelo2_dropout.xlsx"),
            "resultados_modelo3_batchnorm.xlsx": pd.read_excel("/content/resultados_modelo3_batchnorm.xlsx")
        }

        for nombre_archivo, df in archivos.items():
            nombre_coleccion = nombre_archivo.replace(".xlsx", "")
            coleccion = db[nombre_coleccion]
            
            datos = df.to_dict(orient='records')

            if datos:
                coleccion.insert_many(datos)
                print(f"Insertados {len(datos)} documentos en la colección '{nombre_coleccion}'.")
            else:
                print(f"El DataFrame '{nombre_archivo}' está vacío, no se insertó nada.")