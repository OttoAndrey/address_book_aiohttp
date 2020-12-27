from aiohttp import web

import db


async def index(request):
    response_obj = {'status': 'success'}
    return web.json_response(response_obj)


async def get_users_list(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.user.select())
        records = await cursor.fetchall()
        users = []
        for record in records:
            user = {
                'id': record.id,
                'full_name': record.full_name,
                'sex': record.sex.value,
                'birthdate': str(record.birthdate),
                'living_address': record.living_address,
            }
            users.append(user)
        return web.json_response(users)


async def get_emails_list(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.email.select())
        records = await cursor.fetchall()
        emails = []
        for record in records:
            email = {
                'id': record.id,
                'email': record.address,
                'type': record.type.value,
                'user_id': record.user_id,
            }
            emails.append(email)
        return web.json_response(emails)


async def get_phones_list(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.phone.select())
        records = await cursor.fetchall()
        phones = []
        for record in records:
            phone = {
                'id': record.id,
                'number': record.number,
                'type': record.type.value,
                'user_id': record.user_id,
            }
            phones.append(phone)
        return web.json_response(phones)


async def create_email(request):
    data = await request.post()
    email_obj = {
        'address': data['address'],
        'type': data['type'],
        'user_id': data['user_id'],
    }
    async with request.app['db'].acquire() as conn:
        await conn.execute(db.email.insert().values(email_obj))
        return web.json_response(email_obj, status=201)


async def create_phone(request):
    data = await request.post()
    phone_obj = {
        'number': data['number'],
        'type': data['type'],
        'user_id': data['user_id'],
    }
    async with request.app['db'].acquire() as conn:
        await conn.execute(db.phone.insert().values(phone_obj))
        return web.json_response(phone_obj, status=201)


async def create_user(request):
    data = await request.post()
    user_obj = {
        'full_name': data['full_name'],
        'sex': data['sex'],
        'birthdate': data['birthdate'],
        'living_address': data['living_address'],
    }

    async with request.app['db'].acquire() as conn:
        inserted_user = await conn.execute(db.user.insert().values(user_obj))
        first_row = await inserted_user.first()
        user_id = first_row[0]
        print(user_id)

        phone_obj = {}
        if 'number' in data:
            phone_obj = {
                'number': data['number'],
                'type': data['phone_type'],
                'user_id': user_id,
            }
            await conn.execute(db.phone.insert().values(phone_obj))

        email_obj = {}
        if 'address' in data:
            email_obj = {
                'address': data['address'],
                'type': data['email_type'],
                'user_id': user_id,
            }
            await conn.execute(db.email.insert().values(email_obj))

        answer = {
            'user': user_obj,
            'email': email_obj,
            'phone': phone_obj,
        }
        return web.json_response(answer, status=201)
