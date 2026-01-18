from sqlalchemy.engine import URL

DATABASE_URL = URL.create(
    drivername="postgresql+asyncpg",
    username="myuser",
    password="mypassword",
    host="localhost",
    port=5432,
    database="mydb"
)
