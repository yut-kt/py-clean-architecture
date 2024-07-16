from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from py_clean_architecture.config import RDB_DATABASE, RDB_HOST, RDB_PASSWORD, RDB_PORT, RDB_USER

Base = declarative_base()

from .model import *  # noqa: E402, F403

engine = create_engine(
    URL.create(
        drivername="mysql+pymysql",
        host=RDB_HOST,
        username=RDB_USER,
        password=RDB_PASSWORD,
        port=RDB_PORT,
        database=RDB_DATABASE,
    ),
)

SessionLocal = sessionmaker(bind=engine)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)
