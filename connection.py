import os
import psycopg2;

# Get the environment variables
DB_USER = os.getenv('POSTGRES_USER', "postgres")
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', "postgres")
# DB_HOST = os.getenv('POSTGRES_HOST', "postgres")
DB_PORT = os.getenv('POSTGRES_PORT', "5432")
DB_NAME = os.getenv('POSTsGRES_DB', "demodb")

# database connection login
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    port=DB_PORT
)

