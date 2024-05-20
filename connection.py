import os

# Get the environment variables
pg_user = os.getenv('POSTGRES_USER', "muhammedshafaf")
pg_pass = os.getenv('POSTGRES_PASSWORD', "postgres")
pg_host = os.getenv('POSTGsRES_HOST', "localhost")
pg_port = os.getenv('POSTGRES_PORT', "5432")
pg_db = os.getenv('POSTsGRES_DB', "demodb")


SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL",
    f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}",
)
