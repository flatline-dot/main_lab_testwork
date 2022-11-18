from sqlalchemy.orm import sessionmaker
from .create_db import engine

Session = sessionmaker(bind=engine, autocommit=False)


def get_session():
    with Session() as session:
        return session
