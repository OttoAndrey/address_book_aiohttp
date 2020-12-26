import enum

from sqlalchemy import (
    Column, ForeignKey,
    Integer, String, Date, Enum, Text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_imageattach.entity import Image, image_attachment

Base = declarative_base()


class SexEnum(enum.Enum):
    male = 'male'
    female = 'female'


class PhoneEnum(enum.Enum):
    city = 'city'
    mobile = 'mobile'


class EmailEnum(enum.Enum):
    personal = 'personal'
    work = 'work'


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    image = image_attachment('UserImage')
    sex = Column(Enum(SexEnum), nullable=False)
    birthdate = Column(Date, nullable=False)
    living_address = Column(Text, nullable=False)

    images = relationship('UserImage', backref='user')
    phones = relationship('Phone', backref='user')
    emails = relationship('Email', backref='user')


class UserImage(Base, Image):
    __tablename__ = 'user_image'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))


class Phone(Base):
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum(PhoneEnum), nullable=False)
    number = Column(String(11), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))


class Email(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum(EmailEnum), nullable=False)
    email = Column(String(254), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
