import enum

import aiopg.sa
from sqlalchemy import (
    Column, ForeignKey,
    Integer, String, Date, Enum, Text, MetaData, Table,
)


class SexEnum(enum.Enum):
    male = 'male'
    female = 'female'


class PhoneEnum(enum.Enum):
    city = 'city'
    mobile = 'mobile'


class EmailEnum(enum.Enum):
    personal = 'personal'
    work = 'work'


meta = MetaData()

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('full_name', String(255), nullable=False),
    Column('sex', Enum(SexEnum), nullable=False),
    Column('birthdate', Date, nullable=False),
    Column('living_address', Text, nullable=False),
)

email = Table(
    'email', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('type', Enum(EmailEnum), nullable=False),
    Column('address', String(254), nullable=False),
    Column('user_id', Integer, ForeignKey('user.id', ondelete='CASCADE')),
)

phone = Table(
    'phone', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('type', Enum(PhoneEnum), nullable=False),
    Column('number', String(11), nullable=False),
    Column('user_id', Integer, ForeignKey('user.id', ondelete='CASCADE')),
)


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
