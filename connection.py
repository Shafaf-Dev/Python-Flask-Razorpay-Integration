import os

# Get the environment variables
pg_user = os.getenv('POSTGRES_USER', "postgres_user")
pg_pass = os.getenv('POSTGRES_PASSWORD', "postgres")
pg_host = os.getenv('POSTGRES_HOST', "localhost")
pg_port = os.getenv('POSTGRES_PORT', "5432")
pg_db = os.getenv('POSTGRES_DB', "postgres_db")


SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URL",
    f"postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}",
)

RAZORPAY_KEY_ID = os.getenv('RAZORPAY_API_KEY_ID', None)
RAZORPAY_SECRET = os.getenv('RAZORPAY_API_SECRET', None)