import os
import json
import psycopg2
import pandas as pd
from db_conexion import cliente_postgresql

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def crear_tablas_postgresql():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    # Crear tabla de estudiantes
    cursor.execute("""
        DROP TABLE IF EXISTS carrera CASCADE;
        CREATE TABLE carrera (
            id_carrera SERIAL PRIMARY KEY,
            codigo_carrera VARCHAR(50),
            nombre_carrera VARCHAR(250),
            UNIQUE (codigo_carrera)
        );

        DROP TABLE IF EXISTS estudiante CASCADE;
        CREATE TABLE estudiante (
            id_estudiante SERIAL PRIMARY KEY,
            ci_pasaporte VARCHAR(40) UNIQUE,
            correo_tec VARCHAR(200),
            nombres VARCHAR(200),
            sexo VARCHAR(20),
            genero VARCHAR(50),
            estado_civil VARCHAR(50),
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

        DROP TABLE IF EXISTS asignatura CASCADE;
        CREATE TABLE asignatura (
            id_asignatura SERIAL PRIMARY KEY,
            id_carrera INT REFERENCES carrera(id_carrera),
            nombre_asignatura VARCHAR(200),
            UNIQUE (nombre_asignatura)
        );

        DROP TABLE IF EXISTS estudiante_carrera CASCADE;
        CREATE TABLE estudiante_carrera (
            id_estudiante_carrera SERIAL PRIMARY KEY,
            id_carrera INT REFERENCES carrera(id_carrera),
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            ciclo_carrera VARCHAR(30),
            periodo_academico VARCHAR(30),
            paralelo VARCHAR(11)
        );

        DROP TABLE IF EXISTS estudiante_asignatura  CASCADE;
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

        DROP TABLE IF EXISTS colegio_graduacion CASCADE;
        CREATE TABLE colegio_graduacion (
            id_colegio SERIAL PRIMARY KEY,
            id_estudiante INT UNIQUE REFERENCES estudiante(id_estudiante),
            nombre_colegio VARCHAR(200),
            tipo_colegio VARCHAR(80),
            titulo_bachiller VARCHAR(100),
            anio_graduacion INT
        );

        DROP TABLE IF EXISTS contacto_emergencia CASCADE;
        CREATE TABLE contacto_emergencia (
            id_contacto_emergencia SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            nombre_contacto VARCHAR(200),
            telefono_contacto VARCHAR(50)
        );

        DROP TABLE IF EXISTS datos_salud CASCADE;
        CREATE TABLE datos_salud (
            id_datos_salud SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            tipo_sangre VARCHAR(20),
            semanas_embarazo INT,
            porcentaje_discapacidad DECIMAL(5,2),
            nombre_discapacidad VARCHAR(200),
            nombre_enfermedades TEXT,
            vacuna_covid VARCHAR(100),
            antecedentes_patologicos_fam TEXT,
            tiene_carnet_conadis BOOLEAN
        );

        DROP TABLE IF EXISTS economia_estudiante CASCADE;
        CREATE TABLE economia_estudiante (
            id_economia SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            total_ingresos DECIMAL(10,2),
            total_egresos DECIMAL(10,2)
        );

        DROP TABLE IF EXISTS familia CASCADE;
        CREATE TABLE familia (
            id_familia SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            integrantes_familia TEXT,
            integrantes_aporte_economico TEXT,
            cabezas_familia TEXT
        );

        DROP TABLE IF EXISTS propiedades_extra CASCADE;
        CREATE TABLE propiedades_extra (
            id_propiedades SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            num_propiedades INT,
            valor_propiedades DECIMAL(10,2),
            num_vehiculos INT,
            valor_vehiculos DECIMAL(10,2)
        );

        DROP TABLE IF EXISTS vivienda CASCADE;
        CREATE TABLE vivienda (
            id_vivienda SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            tipo_vivienda VARCHAR(200),
            condicion_vivienda VARCHAR(200),
            servicios_vivienda TEXT
        );
            """)

    cliente.commit()
    cursor.close()
    cliente.close()

    print("Tablas creadas exitosamente en PostgreSQL.")
    
def eliminar_tablas_postgresql():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    # Crear tabla de estudiantes
    cursor.execute("""
        DROP TABLE IF EXISTS carrera CASCADE;

        DROP TABLE IF EXISTS estudiante CASCADE;
       

        DROP TABLE IF EXISTS asignatura CASCADE;


        DROP TABLE IF EXISTS estudiante_carrera CASCADE;


        DROP TABLE IF EXISTS estudiante_asignatura  CASCADE;
      

        DROP TABLE IF EXISTS colegio_graduacion CASCADE;
      
        DROP TABLE IF EXISTS contacto_emergencia CASCADE;
      
        DROP TABLE IF EXISTS datos_salud CASCADE;
       
        DROP TABLE IF EXISTS economia_estudiante CASCADE;
       

        DROP TABLE IF EXISTS familia CASCADE;
       

        DROP TABLE IF EXISTS propiedades_extra CASCADE;

        DROP TABLE IF EXISTS vivienda CASCADE;
      """)

    cliente.commit()
    cursor.close()
    cliente.close()

    print("Tablas eliminadas exitosamente en PostgreSQL.")




def migrar_datos_json_a_postgresql(): 
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    json_folder = os.path.join(BASE_DIR, "data")

    tablas_campos = {
        "carrera": ["id_carrera", "codigo_carrera", "nombre_carrera"],
        "estudiante": ["id_estudiante", "ci_pasaporte", "correo_tec", "nombres", "sexo", "genero", "estado_civil",
                    "num_hijos", "etnia", "fecha_nacimiento", "tipo_parroqui", "ciudad", "provincia", "pais",
                    "celular", "tiene_beca", "estudio_otra_carrera", "ocupacion_estudiante",
                    "persona_cubre_gastos", "recibe_ayuda"],
        "asignatura": ["id_asignatura", "id_carrera", "nombre_asignatura"],
        "estudiante_carrera": ["id_estudiante_carrera", "id_carrera", "id_estudiante", "ciclo_carrera",
                            "periodo_academico", "paralelo"],
        "estudiante_asignatura": ["id_estudiante_carrera", "id_asignatura", "numero_matricula", "porcentaje_asistencia",
                                "nota_final", "estado_estudiante", "estado_matricula", "tipo_ingreso"],
        "colegio_graduacion": ["id_colegio", "id_estudiante", "nombre_colegio", "tipo_colegio", "titulo_bachiller",
                            "anio_graduacion"],
        "contacto_emergencia": ["id_contacto_emergencia", "id_estudiante", "nombre_contacto", "telefono_contacto"],
        "datos_salud": ["id_datos_salud", "id_estudiante", "tipo_sangre", "semanas_embarazo", "porcentaje_discapacidad",
                        "nombre_discapacidad", "nombre_enfermedades", "vacuna_covid", "antecedentes_patologicos_fam",
                        "tiene_carnet_conadis"],
        "economia_estudiante": ["id_economia", "id_estudiante", "total_ingresos", "total_egresos"],
        "familia": ["id_familia", "id_estudiante", "integrantes_familia", "integrantes_aporte_economico",
                    "cabezas_familia"],
        "propiedades_extra": ["id_propiedades", "id_estudiante", "num_propiedades", "valor_propiedades",
                            "num_vehiculos", "valor_vehiculos"],
        "vivienda": ["id_vivienda", "id_estudiante", "tipo_vivienda", "condicion_vivienda", "servicios_vivienda"]
    }

    # Campos que deben convertirse explícitamente a booleanos
    campos_booleanos = {
        "estudiante": ["tiene_beca", "estudio_otra_carrera", "recibe_ayuda"],
        "datos_salud": ["tiene_carnet_conadis"]
    }

    def insertar_tabla(nombre_tabla, campos, registros):
        columnas = ', '.join(campos)
        placeholders = ', '.join(['%s'] * len(campos))
        query = f"""
            INSERT INTO {nombre_tabla} ({columnas})
            VALUES ({placeholders})
            ON CONFLICT DO NOTHING
        """
        for registro in registros:
            valores = [registro.get(c) for c in campos]

            # Convertir booleanos si aplica
            if nombre_tabla in campos_booleanos:
                for i, campo in enumerate(campos):
                    if campo in campos_booleanos[nombre_tabla]:
                        if valores[i] in [0, 1]:
                            valores[i] = bool(valores[i])

            try:
                cursor.execute(query, valores)
            except Exception as e:
                cliente.rollback()  # Limpia la transacción fallida
                print(f"⚠️ Error en '{nombre_tabla}': {e}\nRegistro: {registro}")

    for tabla in tablas_campos:
        archivo_json = os.path.join(json_folder, f"{tabla}.json")
        if not os.path.exists(archivo_json):
            print(f"📁 Archivo no encontrado: {archivo_json}")
            continue

        with open(archivo_json, 'r', encoding='utf-8') as f:
            registros = json.load(f)

        print(f"📥 Insertando {len(registros)} registros en '{tabla}'...")
        insertar_tabla(tabla, tablas_campos[tabla], registros)

    cursor.close()
    cliente.close()
    print("\n✅ Migración finalizada correctamente.")



#crear_tablas_postgresql()
#migrar_datos_json_a_postgresql()
eliminar_tablas_postgresql()