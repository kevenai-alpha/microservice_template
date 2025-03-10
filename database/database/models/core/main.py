from sqlalchemy.ext.declarative import declarative_base
from database.config import config
from sqlalchemy import create_engine
from sqla_wrapper import SQLAlchemy

Base = declarative_base()
if not config.postgres_uri:
    raise ValueError("DATABASE_URL is not set")

db = SQLAlchemy(
    config.postgres_uri,
)

engine = create_engine(
    config.postgres_uri,
    connect_args={"connect_timeout": config.connect_timeout},
)