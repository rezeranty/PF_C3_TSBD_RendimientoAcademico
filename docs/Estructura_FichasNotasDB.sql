# Estructura de base de datos Postgresdb:

DROP DATABASE IF EXISTS fichasnotasdb;
CREATE DATABASE fichasnotasdb
    WITH ENCODING='UTF8'
    LC_COLLATE='es_ES.UTF-8'
    LC_CTYPE='es_ES.UTF-8'
    TEMPLATE=template0;

\c fichasnotasdb


DROP TABLE IF EXISTS estudiante CASCADE;
CREATE TABLE estudiante (
    id_estudiante SERIAL PRIMARY KEY,
    ci_pasaporte character varying(20),
    correo_tec character varying(100),
    nombres character varying(100),
    sexo character varying(11),
    genero character varying(20),
    estado_civil character varying(30),
    num_hijos integer,
    etnia character varying(50),
    fecha_nacimiento date,
    tipo_parroqui character varying(50),
    ciudad character varying(50),
    provincia character varying(50),
    pais character varying(50),
    celular character varying(20),
    tiene_beca boolean,
    estudio_otra_carrera boolean,
    ocupacion_estudiante character varying(100),
    persona_cubre_gastos character varying(100),
    recibe_ayuda boolean
);


DROP TABLE IF EXISTS contacto_emergencia CASCADE;
CREATE TABLE contacto_emergencia (
    id_contacto_emergencia SERIAL PRIMARY KEY,
    id_estudiante integer,
    nombre_contacto character varying(100),
    telefono_contacto character varying(20),
    CONSTRAINT fk1_contacto_emergencia FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante)
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS datos_salud CASCADE;
CREATE TABLE datos_salud (
    id_datos_salud SERIAL PRIMARY KEY,
    id_estudiante integer,
    tipo_sangre character varying(11),
    semanas_embarazo integer,
    porcentaje_discapacidad numeric(5,2),
    nombre_discapacidad character varying(100),
    nombre_enfermedades text,
    vacuna_covid character varying(70),
    antecedentes_patologicos_fam text,
    tiene_carnet_conadis boolean,
    CONSTRAINT fk1_datos_salud FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante)
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS propiedades_extra CASCADE;
CREATE TABLE propiedades_extra (
    id_propiedades SERIAL PRIMARY KEY,
    id_estudiante integer,
    num_propiedades integer,
    valor_propiedades numeric(10,2),
    num_vehiculos integer,
    valor_vehiculos numeric(10,2),
    CONSTRAINT fk1_propiedades_extra FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante)
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS familia CASCADE;
CREATE TABLE familia (
    id_familia SERIAL PRIMARY KEY,
    id_estudiante integer,
    integrantes_familia text,
    integrantes_aporte_economico text,
    cabezas_familia text,
    CONSTRAINT fk1_familia FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante)
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS colegio_graduacion CASCADE;
CREATE TABLE colegio_graduacion (
    id_colegio SERIAL PRIMARY KEY,
    id_estudiante integer,
    nombre_colegio character varying(100),
    tipo_colegio character varying(50),
    titulo_bachiller character varying(50),
    anio_graduacion integer,
    CONSTRAINT fk1_colegio_graduacion FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante)
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS vivienda CASCADE;
CREATE TABLE vivienda (
    id_vivienda SERIAL PRIMARY KEY,
    id_estudiante integer,
    tipo_vivienda character varying(100),
    condicion_vivienda character varying(100),
    servicios_vivienda text,
    CONSTRAINT fk1_vivienda FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante)
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS economia_estudiante CASCADE;
CREATE TABLE economia_estudiante (
    id_economia SERIAL PRIMARY KEY,
    id_estudiante integer,
    total_ingresos numeric(10,2),
    total_egresos numeric(10,2),
    CONSTRAINT fk1_economia_estudiante FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante)
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS carrera CASCADE;
CREATE TABLE carrera (
    id_carrera SERIAL PRIMARY KEY,
    codigo_carrera character varying(50),
    nombre_carrera character varying(200)
);


DROP TABLE IF EXISTS estudiante_carrera CASCADE;
CREATE TABLE estudiante_carrera (
    id_estudiante_carrera SERIAL PRIMARY KEY,
    id_carrera integer,
    id_estudiante integer,
    ciclo_carrera character varying(20),
    periodo_academico character varying(20),
    paralelo character varying(11),
    CONSTRAINT fk1_estudiante_carrera FOREIGN KEY (id_carrera)
        REFERENCES carrera(id_carrera)
        ON DELETE CASCADE,
    CONSTRAINT fk2_estudiante_carrera FOREIGN KEY (id_estudiante)
        REFERENCES estudiante(id_estudiante)
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS asignatura CASCADE;
CREATE TABLE asignatura (
    id_asignatura SERIAL PRIMARY KEY,
    id_carrera integer,
    nombre_asignatura character varying(100),
    CONSTRAINT fk1_asignatura FOREIGN KEY (id_carrera)
        REFERENCES carrera(id_carrera)
        ON DELETE CASCADE
);


DROP TABLE IF EXISTS estudiante_asignatura CASCADE;
CREATE TABLE estudiante_asignatura (
    id_estudiante_carrera integer NOT NULL,
    id_asignatura integer NOT NULL,
    numero_matricula integer, -- Número de veces que ha cursado la materia.
    porcentaje_asistencia numeric(5,2),
    nota_final numeric(5,2),
    estado_estudiante character varying(50),
    estado_matricula character varying(50),
    tipo_ingreso character varying(50)
    PRIMARY KEY(id_estudiante_carrera, id_asignatura),
    CONSTRAINT fk1_estudiante_asignatura FOREIGN KEY (id_estudiante_carrera)
        REFERENCES estudiante_carrera(id_estudiante_carrera)
        ON DELETE CASCADE,
    CONSTRAINT fk2_estudiante_asignatura FOREIGN KEY (id_asignatura)
        REFERENCES asignatura(id_asignatura)
        ON DELETE CASCADE
);


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