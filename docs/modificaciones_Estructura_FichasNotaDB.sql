DELETE FROM estudiante_asignatura
WHERE id_asignatura IN (
    SELECT id_asignatura FROM asignatura
    WHERE id_carrera IN (4, 24, 29)
);

DELETE FROM asignatura
WHERE id_carrera IN (4, 24, 29);