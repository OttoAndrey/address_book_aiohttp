import random

from faker import Faker
from sqlalchemy import create_engine

from db import user, phone, email, EmailEnum, PhoneEnum
from settings import DSN, config


def fill_db(db_engine):
    fake = Faker('ru_RU')
    conn = db_engine.connect()

    for i in range(10):
        profile = fake.profile()

        if profile['sex'] == 'M':
            sex = 'male'
        else:
            sex = 'female'

        new_user = user.insert().values(full_name=profile['name'],
                                        sex=sex,
                                        birthdate=profile['birthdate'],
                                        living_address=profile['address'],
                                        avatar_url=fake.image_url(),)
        conn.execute(new_user)

        all_users = conn.execute(user.select().order_by(user.c.id.desc()).limit(1))
        last_user = all_users.fetchone()
        last_user_id = last_user[0]

        fake_phone_number = fake.phone_number()
        clean_number = ''.join(number for number in fake_phone_number if number.isdigit())
        phone_type = random.choice([e.value for e in PhoneEnum])
        phone_number = phone.insert().values(number=clean_number,
                                             type=phone_type,
                                             user_id=last_user_id)
        conn.execute(phone_number)

        fake_email = fake.email()
        email_type = random.choice([e.value for e in EmailEnum])
        email_address = email.insert().values(address=fake_email,
                                              type=email_type,
                                              user_id=last_user_id)
        conn.execute(email_address)

    conn.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    db_engine = create_engine(db_url)
    fill_db(db_engine)
