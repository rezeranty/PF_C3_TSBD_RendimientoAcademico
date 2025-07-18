CREATE OR REPLACE VIEW promedio_notas_por_estudiante AS
SELECT 
    ec.id_estudiante,
    ec.id_carrera,
    ec.periodo_academico,
    ROUND(AVG(ea.nota_final), 2) AS promedio_notas
FROM estudiante_carrera ec
JOIN estudiante_asignatura ea ON ec.id_estudiante_carrera = ea.id_estudiante_carrera
GROUP BY
    ec.id_estudiante,
    ec.id_carrera,
    ec.periodo_academico;