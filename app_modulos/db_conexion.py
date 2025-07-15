import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def cliente_postgresql():
    cliente= psycopg2.connect(os.getenv("DB_POSGRESQL_URL"))
    return cliente