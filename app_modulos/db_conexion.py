import psycopg2
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

postgres_url_nube_db = os.getenv("DB_POSTGRESQL_RENDER_URL")

postgres_host_local = os.getenv("DB_POSTGRESQL_LOCAL_HOST")
postgres_db_local = os.getenv("DB_POSTGRESQL_LOCAL_DB")
postgres_user_local = os.getenv("DB_POSTGRESQL_LOCAL_USER")
postgres_pass_local = os.getenv("DB_POSTGRESQL_LOCAL_PASS")
postgres_port_local = os.getenv("DB_POSTGRESQL_LOCAL_PORT")

mongo_url_nube_db = os.getenv("DB_MONGODB_ATLAS_URL")


def cliente_postgresql(host=None):
    if host and host == 'nube':
        return psycopg2.connect(postgres_url_nube_db)
    else:
        return psycopg2.connect(
            host=postgres_host_local,         
            database=postgres_db_local,   
            user=postgres_user_local,
            password=postgres_pass_local,
            port=postgres_port_local
        )


def cliente_mongodb():
    
    uri = mongo_url_nube_db

    try:
        cliente = MongoClient(uri, server_api=ServerApi('1'))
        cliente.admin.command('ping')
        print("Conexión exitosa a MongoDB Atlas.")
        return cliente
    except Exception as e:
        print("Error al conectar con MongoDB Atlas:", e)
        return None