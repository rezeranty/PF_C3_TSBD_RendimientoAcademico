CREATE DATABASE fichasnotasdb;
\c fichasnotasdb;

CREATE TABLE carrera (
    id_carrera SERIAL PRIMARY KEY,
    codigo_carrera VARCHAR(50),
    nombre_carrera VARCHAR(200),
    UNIQUE (codigo_carrera)
);

CREATE TABLE estudiante (
    id_estudiante SERIAL PRIMARY KEY,
    ci_pasaporte VARCHAR(20) UNIQUE,
    correo_tec VARCHAR(100),
    nombres VARCHAR(100),
    sexo VARCHAR(11),
    genero VARCHAR(20),
    estado_civil VARCHAR(30),
    num_hijos INT,
    etnia VARCHAR(50),
    fecha_nacimiento DATE,
    tipo_parroqui VARCHAR(50),
    ciudad VARCHAR(50),
    provincia VARCHAR(50),
    pais VARCHAR(50),
    celular VARCHAR(20),
    tiene_beca BOOLEAN,
    estudio_otra_carrera BOOLEAN,
    ocupacion_estudiante VARCHAR(100),
    persona_cubre_gastos VARCHAR(100),
    recibe_ayuda BOOLEAN
);

CREATE TABLE asignatura (
    id_asignatura SERIAL PRIMARY KEY,
    id_carrera INT REFERENCES carrera(id_carrera),
    nombre_asignatura VARCHAR(100),
    UNIQUE (nombre_asignatura)
);

CREATE TABLE estudiante_carrera (
    id_estudiante_carrera SERIAL PRIMARY KEY,
    id_carrera INT REFERENCES carrera(id_carrera),
    id_estudiante INT REFERENCES estudiante(id_estudiante),
    ciclo_carrera VARCHAR(20),
    periodo_academico VARCHAR(20),
    paralelo VARCHAR(11)
);

CREATE TABLE estudiante_asignatura (
    id_estudiante_carrera INT,
    id_asignatura INT,
    numero_matricula INT,
    porcentaje_asistencia DECIMAL(5,2),
    nota_final DECIMAL(5,2),
    estado_estudiante VARCHAR(50),
    estado_matricula VARCHAR(50),
    tipo_ingreso VARCHAR(50),
    PRIMARY KEY (id_estudiante_carrera, id_asignatura),
    FOREIGN KEY (id_estudiante_carrera) REFERENCES estudiante_carrera(id_estudiante_carrera),
    FOREIGN KEY (id_asignatura) REFERENCES asignatura(id_asignatura)
);

CREATE TABLE colegio_graduacion (
    id_colegio SERIAL PRIMARY KEY,
    id_estudiante INT UNIQUE REFERENCES estudiante(id_estudiante),
    nombre_colegio VARCHAR(100),
    tipo_colegio VARCHAR(50),
    titulo_bachiller VARCHAR(50),
    anio_graduacion INT
);

CREATE TABLE contacto_emergencia (
    id_contacto_emergencia SERIAL PRIMARY KEY,
    id_estudiante INT REFERENCES estudiante(id_estudiante),
    nombre_contacto VARCHAR(100),
    telefono_contacto VARCHAR(20)
);

CREATE TABLE datos_salud (
    id_datos_salud SERIAL PRIMARY KEY,
    id_estudiante INT REFERENCES estudiante(id_estudiante),
    tipo_sangre VARCHAR(11),
    semanas_embarazo INT,
    porcentaje_discapacidad DECIMAL(5,2),
    nombre_discapacidad VARCHAR(100),
    nombre_enfermedades TEXT,
    vacuna_covid VARCHAR(70),
    antecedentes_patologicos_fam TEXT,
    tiene_carnet_conadis BOOLEAN
);

CREATE TABLE economia_estudiante (
    id_economia SERIAL PRIMARY KEY,
    id_estudiante INT REFERENCES estudiante(id_estudiante),
    total_ingresos DECIMAL(10,2),
    total_egresos DECIMAL(10,2)
);

CREATE TABLE familia (
    id_familia SERIAL PRIMARY KEY,
    id_estudiante INT REFERENCES estudiante(id_estudiante),
    integrantes_familia TEXT,
    integrantes_aporte_economico TEXT,
    cabezas_familia TEXT
);

CREATE TABLE propiedades_extra (
    id_propiedades SERIAL PRIMARY KEY,
    id_estudiante INT REFERENCES estudiante(id_estudiante),
    num_propiedades INT,
    valor_propiedades DECIMAL(10,2),
    num_vehiculos INT,
    valor_vehiculos DECIMAL(10,2)
);

CREATE TABLE vivienda (
    id_vivienda SERIAL PRIMARY KEY,
    id_estudiante INT REFERENCES estudiante(id_estudiante),
    tipo_vivienda VARCHAR(100),
    condicion_vivienda VARCHAR(100),
    servicios_vivienda TEXT
);
