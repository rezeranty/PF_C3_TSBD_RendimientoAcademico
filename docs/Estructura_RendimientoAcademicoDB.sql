--
-- PostgreSQL database dump
--

-- Dumped from database version 16.9 (Ubuntu 16.9-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.9 (Ubuntu 16.9-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: asignatura; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.asignatura (
    id_asignatura integer NOT NULL,
    id_carrera integer,
    nombre_asignatura character varying(100)
);


ALTER TABLE public.asignatura OWNER TO tsbd_s3;

--
-- Name: asignatura_id_asignatura_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.asignatura_id_asignatura_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.asignatura_id_asignatura_seq OWNER TO tsbd_s3;

--
-- Name: asignatura_id_asignatura_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.asignatura_id_asignatura_seq OWNED BY public.asignatura.id_asignatura;


--
-- Name: carrera; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.carrera (
    id_carrera integer NOT NULL,
    codigo_carrera character varying(50),
    nombre_carrera character varying(200)
);


ALTER TABLE public.carrera OWNER TO tsbd_s3;

--
-- Name: carrera_id_carrera_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.carrera_id_carrera_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.carrera_id_carrera_seq OWNER TO tsbd_s3;

--
-- Name: carrera_id_carrera_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.carrera_id_carrera_seq OWNED BY public.carrera.id_carrera;


--
-- Name: colegio_graduacion; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.colegio_graduacion (
    id_colegio integer NOT NULL,
    id_estudiante integer,
    nombre_colegio character varying(100),
    tipo_colegio character varying(50),
    titulo_bachiller character varying(50),
    anio_graduacion integer
);


ALTER TABLE public.colegio_graduacion OWNER TO tsbd_s3;

--
-- Name: colegio_graduacion_id_colegio_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.colegio_graduacion_id_colegio_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.colegio_graduacion_id_colegio_seq OWNER TO tsbd_s3;

--
-- Name: colegio_graduacion_id_colegio_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.colegio_graduacion_id_colegio_seq OWNED BY public.colegio_graduacion.id_colegio;


--
-- Name: contacto_emergencia; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.contacto_emergencia (
    id_contacto_emergencia integer NOT NULL,
    id_estudiante integer,
    nombre_contacto character varying(100),
    telefono_contacto character varying(20)
);


ALTER TABLE public.contacto_emergencia OWNER TO tsbd_s3;

--
-- Name: contacto_emergencia_id_contacto_emergencia_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.contacto_emergencia_id_contacto_emergencia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.contacto_emergencia_id_contacto_emergencia_seq OWNER TO tsbd_s3;

--
-- Name: contacto_emergencia_id_contacto_emergencia_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.contacto_emergencia_id_contacto_emergencia_seq OWNED BY public.contacto_emergencia.id_contacto_emergencia;


--
-- Name: datos_salud; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.datos_salud (
    id_datos_salud integer NOT NULL,
    id_estudiante integer,
    tipo_sangre character varying(11),
    semanas_embarazo integer,
    porcentaje_discapacidad numeric(5,2),
    nombre_discapacidad character varying(100),
    nombre_enfermedades text,
    vacuna_covid character varying(70),
    antecedentes_patologicos_fam text,
    tiene_carnet_conadis boolean
);


ALTER TABLE public.datos_salud OWNER TO tsbd_s3;

--
-- Name: datos_salud_id_datos_salud_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.datos_salud_id_datos_salud_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.datos_salud_id_datos_salud_seq OWNER TO tsbd_s3;

--
-- Name: datos_salud_id_datos_salud_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.datos_salud_id_datos_salud_seq OWNED BY public.datos_salud.id_datos_salud;


--
-- Name: economia_estudiante; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.economia_estudiante (
    id_economia integer NOT NULL,
    id_estudiante integer,
    total_ingresos numeric(10,2),
    total_egresos numeric(10,2)
);


ALTER TABLE public.economia_estudiante OWNER TO tsbd_s3;

--
-- Name: economia_estudiante_id_economia_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.economia_estudiante_id_economia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.economia_estudiante_id_economia_seq OWNER TO tsbd_s3;

--
-- Name: economia_estudiante_id_economia_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.economia_estudiante_id_economia_seq OWNED BY public.economia_estudiante.id_economia;


--
-- Name: estudiante; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.estudiante (
    id_estudiante integer NOT NULL,
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


ALTER TABLE public.estudiante OWNER TO tsbd_s3;

--
-- Name: estudiante_asignatura; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.estudiante_asignatura (
    id_estudiante_carrera integer NOT NULL,
    id_asignatura integer NOT NULL,
    numero_matricula integer,
    porcentaje_asistencia numeric(5,2),
    nota_final numeric(5,2),
    estado_estudiante character varying(50),
    estado_matricula character varying(50),
    tipo_ingreso character varying(50)
);


ALTER TABLE public.estudiante_asignatura OWNER TO tsbd_s3;

--
-- Name: estudiante_carrera; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.estudiante_carrera (
    id_estudiante_carrera integer NOT NULL,
    id_carrera integer,
    id_estudiante integer,
    ciclo_carrera character varying(20),
    periodo_academico character varying(20),
    paralelo character varying(11)
);


ALTER TABLE public.estudiante_carrera OWNER TO tsbd_s3;

--
-- Name: estudiante_carrera_id_estudiante_carrera_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.estudiante_carrera_id_estudiante_carrera_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.estudiante_carrera_id_estudiante_carrera_seq OWNER TO tsbd_s3;

--
-- Name: estudiante_carrera_id_estudiante_carrera_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.estudiante_carrera_id_estudiante_carrera_seq OWNED BY public.estudiante_carrera.id_estudiante_carrera;


--
-- Name: estudiante_id_estudiante_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.estudiante_id_estudiante_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.estudiante_id_estudiante_seq OWNER TO tsbd_s3;

--
-- Name: estudiante_id_estudiante_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.estudiante_id_estudiante_seq OWNED BY public.estudiante.id_estudiante;


--
-- Name: familia; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.familia (
    id_familia integer NOT NULL,
    id_estudiante integer,
    integrantes_familia text,
    integrantes_aporte_economico text,
    cabezas_familia text
);


ALTER TABLE public.familia OWNER TO tsbd_s3;

--
-- Name: familia_id_familia_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.familia_id_familia_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.familia_id_familia_seq OWNER TO tsbd_s3;

--
-- Name: familia_id_familia_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.familia_id_familia_seq OWNED BY public.familia.id_familia;


--
-- Name: propiedades_extra; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.propiedades_extra (
    id_propiedades integer NOT NULL,
    id_estudiante integer,
    num_propiedades integer,
    valor_propiedades numeric(10,2),
    num_vehiculos integer,
    valor_vehiculos numeric(10,2)
);


ALTER TABLE public.propiedades_extra OWNER TO tsbd_s3;

--
-- Name: propiedades_extra_id_propiedades_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.propiedades_extra_id_propiedades_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.propiedades_extra_id_propiedades_seq OWNER TO tsbd_s3;

--
-- Name: propiedades_extra_id_propiedades_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.propiedades_extra_id_propiedades_seq OWNED BY public.propiedades_extra.id_propiedades;


--
-- Name: vivienda; Type: TABLE; Schema: public; Owner: tsbd_s3
--

CREATE TABLE public.vivienda (
    id_vivienda integer NOT NULL,
    id_estudiante integer,
    tipo_vivienda character varying(100),
    condicion_vivienda character varying(100),
    servicios_vivienda text
);


ALTER TABLE public.vivienda OWNER TO tsbd_s3;

--
-- Name: vivienda_id_vivienda_seq; Type: SEQUENCE; Schema: public; Owner: tsbd_s3
--

CREATE SEQUENCE public.vivienda_id_vivienda_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vivienda_id_vivienda_seq OWNER TO tsbd_s3;

--
-- Name: vivienda_id_vivienda_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: tsbd_s3
--

ALTER SEQUENCE public.vivienda_id_vivienda_seq OWNED BY public.vivienda.id_vivienda;


--
-- Name: asignatura id_asignatura; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.asignatura ALTER COLUMN id_asignatura SET DEFAULT nextval('public.asignatura_id_asignatura_seq'::regclass);


--
-- Name: carrera id_carrera; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.carrera ALTER COLUMN id_carrera SET DEFAULT nextval('public.carrera_id_carrera_seq'::regclass);


--
-- Name: colegio_graduacion id_colegio; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.colegio_graduacion ALTER COLUMN id_colegio SET DEFAULT nextval('public.colegio_graduacion_id_colegio_seq'::regclass);


--
-- Name: contacto_emergencia id_contacto_emergencia; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.contacto_emergencia ALTER COLUMN id_contacto_emergencia SET DEFAULT nextval('public.contacto_emergencia_id_contacto_emergencia_seq'::regclass);


--
-- Name: datos_salud id_datos_salud; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.datos_salud ALTER COLUMN id_datos_salud SET DEFAULT nextval('public.datos_salud_id_datos_salud_seq'::regclass);


--
-- Name: economia_estudiante id_economia; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.economia_estudiante ALTER COLUMN id_economia SET DEFAULT nextval('public.economia_estudiante_id_economia_seq'::regclass);


--
-- Name: estudiante id_estudiante; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante ALTER COLUMN id_estudiante SET DEFAULT nextval('public.estudiante_id_estudiante_seq'::regclass);


--
-- Name: estudiante_carrera id_estudiante_carrera; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante_carrera ALTER COLUMN id_estudiante_carrera SET DEFAULT nextval('public.estudiante_carrera_id_estudiante_carrera_seq'::regclass);


--
-- Name: familia id_familia; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.familia ALTER COLUMN id_familia SET DEFAULT nextval('public.familia_id_familia_seq'::regclass);


--
-- Name: propiedades_extra id_propiedades; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.propiedades_extra ALTER COLUMN id_propiedades SET DEFAULT nextval('public.propiedades_extra_id_propiedades_seq'::regclass);


--
-- Name: vivienda id_vivienda; Type: DEFAULT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.vivienda ALTER COLUMN id_vivienda SET DEFAULT nextval('public.vivienda_id_vivienda_seq'::regclass);


--
-- Name: asignatura asignatura_nombre_asignatura_key; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT asignatura_nombre_asignatura_key UNIQUE (nombre_asignatura);


--
-- Name: asignatura asignatura_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT asignatura_pkey PRIMARY KEY (id_asignatura);


--
-- Name: carrera carrera_codigo_carrera_key; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.carrera
    ADD CONSTRAINT carrera_codigo_carrera_key UNIQUE (codigo_carrera);


--
-- Name: carrera carrera_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.carrera
    ADD CONSTRAINT carrera_pkey PRIMARY KEY (id_carrera);


--
-- Name: colegio_graduacion colegio_graduacion_id_estudiante_key; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.colegio_graduacion
    ADD CONSTRAINT colegio_graduacion_id_estudiante_key UNIQUE (id_estudiante);


--
-- Name: colegio_graduacion colegio_graduacion_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.colegio_graduacion
    ADD CONSTRAINT colegio_graduacion_pkey PRIMARY KEY (id_colegio);


--
-- Name: contacto_emergencia contacto_emergencia_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.contacto_emergencia
    ADD CONSTRAINT contacto_emergencia_pkey PRIMARY KEY (id_contacto_emergencia);


--
-- Name: datos_salud datos_salud_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.datos_salud
    ADD CONSTRAINT datos_salud_pkey PRIMARY KEY (id_datos_salud);


--
-- Name: economia_estudiante economia_estudiante_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.economia_estudiante
    ADD CONSTRAINT economia_estudiante_pkey PRIMARY KEY (id_economia);


--
-- Name: estudiante_asignatura estudiante_asignatura_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante_asignatura
    ADD CONSTRAINT estudiante_asignatura_pkey PRIMARY KEY (id_estudiante_carrera, id_asignatura);


--
-- Name: estudiante_carrera estudiante_carrera_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante_carrera
    ADD CONSTRAINT estudiante_carrera_pkey PRIMARY KEY (id_estudiante_carrera);


--
-- Name: estudiante estudiante_ci_pasaporte_key; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante
    ADD CONSTRAINT estudiante_ci_pasaporte_key UNIQUE (ci_pasaporte);


--
-- Name: estudiante estudiante_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante
    ADD CONSTRAINT estudiante_pkey PRIMARY KEY (id_estudiante);


--
-- Name: familia familia_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.familia
    ADD CONSTRAINT familia_pkey PRIMARY KEY (id_familia);


--
-- Name: propiedades_extra propiedades_extra_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.propiedades_extra
    ADD CONSTRAINT propiedades_extra_pkey PRIMARY KEY (id_propiedades);


--
-- Name: vivienda vivienda_pkey; Type: CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.vivienda
    ADD CONSTRAINT vivienda_pkey PRIMARY KEY (id_vivienda);


--
-- Name: asignatura asignatura_id_carrera_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT asignatura_id_carrera_fkey FOREIGN KEY (id_carrera) REFERENCES public.carrera(id_carrera);


--
-- Name: colegio_graduacion colegio_graduacion_id_estudiante_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.colegio_graduacion
    ADD CONSTRAINT colegio_graduacion_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(id_estudiante);


--
-- Name: contacto_emergencia contacto_emergencia_id_estudiante_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.contacto_emergencia
    ADD CONSTRAINT contacto_emergencia_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(id_estudiante);


--
-- Name: datos_salud datos_salud_id_estudiante_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.datos_salud
    ADD CONSTRAINT datos_salud_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(id_estudiante);


--
-- Name: economia_estudiante economia_estudiante_id_estudiante_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.economia_estudiante
    ADD CONSTRAINT economia_estudiante_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(id_estudiante);


--
-- Name: estudiante_asignatura estudiante_asignatura_id_asignatura_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante_asignatura
    ADD CONSTRAINT estudiante_asignatura_id_asignatura_fkey FOREIGN KEY (id_asignatura) REFERENCES public.asignatura(id_asignatura);


--
-- Name: estudiante_asignatura estudiante_asignatura_id_estudiante_carrera_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante_asignatura
    ADD CONSTRAINT estudiante_asignatura_id_estudiante_carrera_fkey FOREIGN KEY (id_estudiante_carrera) REFERENCES public.estudiante_carrera(id_estudiante_carrera);


--
-- Name: estudiante_carrera estudiante_carrera_id_carrera_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante_carrera
    ADD CONSTRAINT estudiante_carrera_id_carrera_fkey FOREIGN KEY (id_carrera) REFERENCES public.carrera(id_carrera);


--
-- Name: estudiante_carrera estudiante_carrera_id_estudiante_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.estudiante_carrera
    ADD CONSTRAINT estudiante_carrera_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(id_estudiante);


--
-- Name: familia familia_id_estudiante_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.familia
    ADD CONSTRAINT familia_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(id_estudiante);


--
-- Name: propiedades_extra propiedades_extra_id_estudiante_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.propiedades_extra
    ADD CONSTRAINT propiedades_extra_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(id_estudiante);


--
-- Name: vivienda vivienda_id_estudiante_fkey; Type: FK CONSTRAINT; Schema: public; Owner: tsbd_s3
--

ALTER TABLE ONLY public.vivienda
    ADD CONSTRAINT vivienda_id_estudiante_fkey FOREIGN KEY (id_estudiante) REFERENCES public.estudiante(id_estudiante);


--
-- PostgreSQL database dump complete
--

