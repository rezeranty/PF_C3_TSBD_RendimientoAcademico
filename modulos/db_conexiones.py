import psycopg2

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from dotenv import load_dotenv
import os


load_dotenv("modulos/.env")

postgres_url_db = os.getenv("DB_POSTGRESQL_RENDER_URL")
mongo_url_db = os.getenv("DB_MONGODB_ATLAS_URL")


def cliente_postgresql():
    return psycopg2.connect(postgres_url_db)


def cliente_mongodb():
    try:
        return MongoClient(mongo_url_db, server_api=ServerApi('1'))
     
    except Exception as e:
        return None