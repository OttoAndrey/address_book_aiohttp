from sqlalchemy import create_engine, MetaData

from db import email, phone, user
from settings import config, DSN


def create_tables(db_engine):
    meta = MetaData()
    meta.create_all(bind=db_engine, tables=[user, email, phone])


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    db_engine = create_engine(db_url)
    create_tables(db_engine)
