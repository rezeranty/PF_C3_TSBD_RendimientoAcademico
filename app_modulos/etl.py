import pandas as pd

import os
import psycopg2
from datetime import datetime


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

from db_conexion import cliente_postgresql, cliente_mongodb


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ======================================== POSTGRESQL ========================================
def migrar_carreras():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    df = pd.read_json(os.path.join(BASE_DIR, "data", "carrera.json"))
    datos = list(df.itertuples(index=False, name=None))

    sql = """
    CREATE TABLE IF NOT EXISTS carrera (
        id_carrera SERIAL PRIMARY KEY,
        codigo_carrera VARCHAR(50),
        nombre_carrera VARCHAR(200),
        UNIQUE (codigo_carrera)
    );
    """
    cursor.execute(sql)
    cliente.commit()
    
    sql = """
    INSERT INTO carrera (id_carrera, codigo_carrera, nombre_carrera)
    VALUES (%s, %s, %s)
    """

    try:
        cursor.executemany(sql, datos)
        cliente.commit()
        print("Datos insertados correctamente.")

    except psycopg2.IntegrityError as e:
        cliente.rollback()
        print("Error de integridad:", e)

    finally:
        cursor.close()
        cliente.close()


def resetear_estudiantes():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        cursor.execute("TRUNCATE TABLE estudiante RESTART IDENTITY CASCADE;")
        cliente.commit()
        print("Tabla 'estudiante' vaciada y contador de ID reiniciado.")
    except Exception as e:
        cliente.rollback()
        print("Error al resetear la tabla 'estudiante':", e)
    finally:
        cursor.close()
        cliente.close()


def convertir_a_fecha(valor):
    try:
        if pd.isna(valor) or valor in ("NaT", "", None):
            return None
        return pd.to_datetime(valor).date()
    except Exception:
        return None


def migrar_estudiantes():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "estudiante.json")
        df = pd.read_json(path_json)

        df["fecha_nacimiento"] = df["fecha_nacimiento"].apply(convertir_a_fecha)

        boolean_fields = ["tiene_beca", "estudio_otra_carrera", "recibe_ayuda"]
        for campo in boolean_fields:
            if campo in df.columns:
                df[campo] = df[campo].astype(bool)

        df = df.where(pd.notnull(df), None)
        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS estudiante (
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
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO estudiante (
            id_estudiante, ci_pasaporte, correo_tec, nombres, sexo, genero,
            estado_civil, num_hijos, etnia, fecha_nacimiento, tipo_parroqui,
            ciudad, provincia, pais, celular, tiene_beca, estudio_otra_carrera,
            ocupacion_estudiante, persona_cubre_gastos, recibe_ayuda
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        datos_validos = [fila for fila in datos if len(fila) == 20]

        if len(datos_validos) < len(datos):
            print(f"Se descartaron {len(datos) - len(datos_validos)} filas por formato inválido.")

        cursor.executemany(insert_sql, datos_validos)
        cliente.commit()
        print("Datos de estudiantes insertados correctamente.")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de estudiantes:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_asignaturas():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "asignatura.json")
        df = pd.read_json(path_json)

        df = df.where(pd.notnull(df), None)

        columnas_esperadas = ["id_asignatura", "id_carrera", "nombre_asignatura"]
        if not all(col in df.columns for col in columnas_esperadas):
            raise ValueError("El archivo JSON de asignaturas no tiene todas las columnas necesarias.")

        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS asignatura (
            id_asignatura SERIAL PRIMARY KEY,
            id_carrera INT REFERENCES carrera(id_carrera),
            nombre_asignatura VARCHAR(100),
            UNIQUE (nombre_asignatura)
        );
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO asignatura (id_asignatura, id_carrera, nombre_asignatura)
        VALUES (%s, %s, %s)
        """

        datos_validos = [fila for fila in datos if len(fila) == 3]

        if len(datos_validos) < len(datos):
            print(f"Se descartaron {len(datos) - len(datos_validos)} filas por formato inválido.")

        cursor.executemany(insert_sql, datos_validos)
        cliente.commit()
        print("Datos de asignaturas insertados correctamente.")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de asignaturas:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_estudiantes_carrera():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "estudiante_carrera.json")
        df = pd.read_json(path_json)
        df = df.where(pd.notnull(df), None)
        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS estudiante_carrera (
            id_estudiante_carrera SERIAL PRIMARY KEY,
            id_carrera INT REFERENCES carrera(id_carrera),
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            ciclo_carrera VARCHAR(20),
            periodo_academico VARCHAR(20),
            paralelo VARCHAR(11)
        );
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO estudiante_carrera (
            id_estudiante_carrera, id_carrera, id_estudiante,
            ciclo_carrera, periodo_academico, paralelo
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id_estudiante_carrera) DO NOTHING
        """

        total = len(datos)
        insertados = 0
        descartados = 0

        for i, fila in enumerate(datos, start=1):
            try:
                cursor.execute(insert_sql, fila)
                cliente.commit()
                insertados += 1
            except psycopg2.IntegrityError:
                cliente.rollback()
                descartados += 1
            print(f"Procesado {i}/{total}")

        print(f"Insertados: {insertados}, descartados por error: {descartados}")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de estudiante_carrera:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_estudiante_asignatura():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "estudiante_asignatura.json")
        df = pd.read_json(path_json)
        df = df.where(pd.notnull(df), None)
        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS estudiante_asignatura (
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
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO estudiante_asignatura (
            id_estudiante_carrera, id_asignatura, numero_matricula,
            porcentaje_asistencia, nota_final, estado_estudiante,
            estado_matricula, tipo_ingreso
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id_estudiante_carrera, id_asignatura) DO NOTHING
        """

        total = len(datos)
        insertados = 0
        descartados = 0

        for i, fila in enumerate(datos, start=1):
            try:
                cursor.execute(insert_sql, fila)
                cliente.commit()
                insertados += 1
            except psycopg2.IntegrityError:
                cliente.rollback()
                descartados += 1
            print(f"Procesado {i}/{total}")

        print(f"Insertados: {insertados}, descartados por error: {descartados}")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de estudiante_asignatura:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_colegio_graduacion():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "colegio_graduacion.json")
        df = pd.read_json(path_json)
        df = df.where(pd.notnull(df), None)
        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS colegio_graduacion (
            id_colegio SERIAL PRIMARY KEY,
            id_estudiante INT UNIQUE REFERENCES estudiante(id_estudiante),
            nombre_colegio VARCHAR(100),
            tipo_colegio VARCHAR(50),
            titulo_bachiller VARCHAR(50),
            anio_graduacion INT
        );
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO colegio_graduacion (
            id_colegio, id_estudiante, nombre_colegio, tipo_colegio,
            titulo_bachiller, anio_graduacion
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT (id_estudiante) DO NOTHING
        """

        total = len(datos)
        insertados = 0
        descartados = 0

        for i, fila in enumerate(datos, start=1):
            try:
                cursor.execute(insert_sql, fila)
                cliente.commit()
                insertados += 1
            except psycopg2.IntegrityError:
                cliente.rollback()
                descartados += 1
            print(f"Procesado {i}/{total}")

        print(f"Insertados: {insertados}, descartados por error: {descartados}")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de colegio_graduacion:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_contacto_emergencia():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "contacto_emergencia.json")
        df = pd.read_json(path_json)
        df = df.where(pd.notnull(df), None)
        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS contacto_emergencia (
            id_contacto_emergencia SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            nombre_contacto VARCHAR(100),
            telefono_contacto VARCHAR(20)
        );
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO contacto_emergencia (
            id_contacto_emergencia, id_estudiante, nombre_contacto, telefono_contacto
        )
        VALUES (%s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """

        total = len(datos)
        insertados = 0
        descartados = 0

        for i, fila in enumerate(datos, start=1):
            try:
                cursor.execute(insert_sql, fila)
                cliente.commit()
                insertados += 1
            except psycopg2.IntegrityError:
                cliente.rollback()
                descartados += 1
            print(f"Procesado {i}/{total}")

        print(f"Insertados: {insertados}, descartados por error: {descartados}")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de contacto_emergencia:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_datos_salud():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "datos_salud.json")
        df = pd.read_json(path_json)
        df = df.where(pd.notnull(df), None)

        # Convertir 0/1 a booleano si aplica
        if "tiene_carnet_conadis" in df.columns:
            df["tiene_carnet_conadis"] = df["tiene_carnet_conadis"].apply(lambda x: bool(x) if x is not None else None)

        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS datos_salud (
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
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO datos_salud (
            id_datos_salud, id_estudiante, tipo_sangre, semanas_embarazo,
            porcentaje_discapacidad, nombre_discapacidad, nombre_enfermedades,
            vacuna_covid, antecedentes_patologicos_fam, tiene_carnet_conadis
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """

        total = len(datos)
        insertados = 0
        descartados = 0

        for i, fila in enumerate(datos, start=1):
            try:
                cursor.execute(insert_sql, fila)
                cliente.commit()
                insertados += 1
            except psycopg2.IntegrityError:
                cliente.rollback()
                descartados += 1
            print(f"Procesado {i}/{total}")

        print(f"Insertados: {insertados}, descartados por error: {descartados}")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de datos_salud:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_economia_estudiante():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "economia_estudiante.json")
        df = pd.read_json(path_json)
        df = df.where(pd.notnull(df), None)
        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS economia_estudiante (
            id_economia SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            total_ingresos DECIMAL(10,2),
            total_egresos DECIMAL(10,2)
        );
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO economia_estudiante (
            id_economia, id_estudiante, total_ingresos, total_egresos
        )
        VALUES (%s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """

        total = len(datos)
        insertados = 0
        descartados = 0

        for i, fila in enumerate(datos, start=1):
            try:
                cursor.execute(insert_sql, fila)
                cliente.commit()
                insertados += 1
            except psycopg2.IntegrityError:
                cliente.rollback()
                descartados += 1
            print(f"Procesado {i}/{total}")

        print(f"Insertados: {insertados}, descartados por error: {descartados}")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de economia_estudiante:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_familia():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "familia.json")
        df = pd.read_json(path_json)
        df = df.where(pd.notnull(df), None)
        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS familia (
            id_familia SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            integrantes_familia TEXT,
            integrantes_aporte_economico TEXT,
            cabezas_familia TEXT
        );
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO familia (
            id_familia, id_estudiante,
            integrantes_familia, integrantes_aporte_economico, cabezas_familia
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """

        total = len(datos)
        insertados = 0
        descartados = 0

        for i, fila in enumerate(datos, start=1):
            try:
                cursor.execute(insert_sql, fila)
                cliente.commit()
                insertados += 1
            except psycopg2.IntegrityError:
                cliente.rollback()
                descartados += 1
            print(f"Procesado {i}/{total}")

        print(f"Insertados: {insertados}, descartados por error: {descartados}")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de familia:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_propiedades_extra():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "propiedades_extra.json")
        df = pd.read_json(path_json)
        df = df.where(pd.notnull(df), None)
        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS propiedades_extra (
            id_propiedades SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            num_propiedades INT,
            valor_propiedades DECIMAL(10,2),
            num_vehiculos INT,
            valor_vehiculos DECIMAL(10,2)
        );
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO propiedades_extra (
            id_propiedades, id_estudiante,
            num_propiedades, valor_propiedades,
            num_vehiculos, valor_vehiculos
        )
        VALUES (%s, %s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """

        total = len(datos)
        insertados = 0
        descartados = 0

        for i, fila in enumerate(datos, start=1):
            try:
                cursor.execute(insert_sql, fila)
                cliente.commit()
                insertados += 1
            except psycopg2.IntegrityError:
                cliente.rollback()
                descartados += 1
            print(f"Procesado {i}/{total}")

        print(f"Insertados: {insertados}, descartados por error: {descartados}")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de propiedades_extra:", e)

    finally:
        cursor.close()
        cliente.close()


def migrar_vivienda():
    cliente = cliente_postgresql()
    cursor = cliente.cursor()

    try:
        path_json = os.path.join(BASE_DIR, "data", "vivienda.json")
        df = pd.read_json(path_json)
        df = df.where(pd.notnull(df), None)
        datos = list(df.itertuples(index=False, name=None))

        crear_tabla_sql = """
        CREATE TABLE IF NOT EXISTS vivienda (
            id_vivienda SERIAL PRIMARY KEY,
            id_estudiante INT REFERENCES estudiante(id_estudiante),
            tipo_vivienda VARCHAR(100),
            condicion_vivienda VARCHAR(100),
            servicios_vivienda TEXT
        );
        """
        cursor.execute(crear_tabla_sql)
        cliente.commit()

        insert_sql = """
        INSERT INTO vivienda (
            id_vivienda, id_estudiante,
            tipo_vivienda, condicion_vivienda, servicios_vivienda
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT DO NOTHING
        """

        total = len(datos)
        insertados = 0
        descartados = 0

        for i, fila in enumerate(datos, start=1):
            try:
                cursor.execute(insert_sql, fila)
                cliente.commit()
                insertados += 1
            except psycopg2.IntegrityError:
                cliente.rollback()
                descartados += 1
            print(f"Procesado {i}/{total}")

        print(f"Insertados: {insertados}, descartados por error: {descartados}")

    except Exception as e:
        cliente.rollback()
        print("Error durante la migración de vivienda:", e)

    finally:
        cursor.close()
        cliente.close()


# ======================================== MONGODB ========================================
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