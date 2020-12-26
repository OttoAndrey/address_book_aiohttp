import random

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import DSN, config
from db import User, Phone, Email, EmailEnum, PhoneEnum


def fill_db(session):
    fake = Faker('ru_RU')
    users = []
    phones = []
    emails = []

    for i in range(10):
        profile = fake.profile()

        if profile['sex'] == 'M':
            sex = 'male'
        else:
            sex = 'female'

        user = User(full_name=profile['name'],
                    sex=sex,
                    birthdate=profile['birthdate'],
                    living_address=profile['address'])
        users.append(user)

    session.add_all(users)
    session.commit()

    for user in session.query(User).all():
        fake_phone_number = fake.phone_number()
        clean_number = ''.join(number for number in fake_phone_number if number.isdigit())
        phone_type = random.choice([e.value for e in PhoneEnum])
        phone_number = Phone(number=clean_number,
                             type=phone_type,
                             user_id=user.id)
        phones.append(phone_number)

        email = fake.email()
        email_type = random.choice([e.value for e in EmailEnum])
        email_address = Email(email=email,
                              type=email_type,
                              user_id=user.id)
        emails.append(email_address)

    session.add_all(phones)
    session.add_all(emails)
    session.commit()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    db_engine = create_engine(db_url)
    Session = sessionmaker(bind=db_engine)
    session = Session()
    fill_db(session)
