import psycopg2
from dotenv import load_dotenv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

url_local = os.getenv("DB_POSTGRESQL_NUBE_URL")

host_local = os.getenv("DB_POSTGRESQL_LOCAL_HOST")
db_local = os.getenv("DB_POSTGRESQL_LOCAL_DB")
user_local = os.getenv("DB_POSTGRESQL_LOCAL_USER")
pass_local = os.getenv("DB_POSTGRESQL_LOCAL_PASS")
port_local = os.getenv("DB_POSTGRESQL_LOCAL_PORT")


def cliente_postgresql(host=None):
    if host and host == 'nube':
        return psycopg2.connect(url_local)
    else:
        return psycopg2.connect(
            host=host_local,         
            database=db_local,   
            user=user_local,
            password=pass_local,
            port=port_local
        )