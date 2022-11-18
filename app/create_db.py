import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

db_path = os.path.join('sqlite.db')

DATABASE_URL = f'sqlite:///{db_path}'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
