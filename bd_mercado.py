import psycopg2 as pg
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["PGCLIENTENCODING"] = "UTF8"

def bd_mercado():
    try:
        conn = pg.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        client_encoding="UTF8" 
        )
        
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None