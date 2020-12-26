from sqlalchemy import create_engine

from db import Base
from settings import config, DSN


def create_tables(db_engine):
    Base.metadata.create_all(db_engine, Base.metadata.tables.values(), checkfirst=True)


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    db_engine = create_engine(db_url)
    create_tables(db_engine)
