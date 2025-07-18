SELECT DISTINCT
    -- todas las columnas que ya tienes
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
    ea.estado_estudiante,
    pn.promedio_notas

FROM estudiante e
JOIN estudiante_carrera ec ON e.id_estudiante = ec.id_estudiante
JOIN carrera c ON ec.id_carrera = c.id_carrera
JOIN promedio_notas_por_estudiante pn 
  ON pn.id_estudiante = e.id_estudiante 
  AND pn.id_carrera = c.id_carrera
  AND pn.periodo_academico = ec.periodo_academico
JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
LEFT JOIN datos_salud ds ON e.id_estudiante = ds.id_estudiante
LEFT JOIN economia_estudiante ee ON e.id_estudiante = ee.id_estudiante
LEFT JOIN (
    SELECT DISTINCT ON (id_estudiante) * FROM familia
) f ON e.id_estudiante = f.id_estudiante
LEFT JOIN (
    SELECT DISTINCT ON (id_estudiante) * FROM vivienda
) v ON e.id_estudiante = v.id_estudiante

ORDER BY 
    e.ci_pasaporte,
    ec.periodo_academico;