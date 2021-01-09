from aiohttp import web
from aiohttp_validate import validate

import db
from schema import UPDATE_PHONE_REQUEST_SCHEMA, UPDATE_EMAIL_REQUEST_SCHEMA, UPDATE_USER_REQUEST_SCHEMA,\
    CREATE_PHONE_REQUEST_SCHEMA, CREATE_EMAIL_REQUEST_SCHEMA, CREATE_USER_REQUEST_SCHEMA
from serializers import *


async def index(request):
    response_obj = {'status': 'success'}
    return web.json_response(response_obj)


async def get_users_list(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.user.select())
        records = await cursor.fetchall()
        context = {
            'users': [serialize_user(record) for record in records]
        }
        return web.json_response(context, status=200)


async def get_emails_list(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.email.select())
        records = await cursor.fetchall()
        context = {
            'emails': [serialize_email(record) for record in records]
        }
        return web.json_response(context, status=200)


async def get_phones_list(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.phone.select())
        records = await cursor.fetchall()
        context = {
            'phones': [serialize_phone(record) for record in records]
        }
        return web.json_response(context, status=200)


@validate(request_schema=CREATE_EMAIL_REQUEST_SCHEMA)
async def create_email(data, request):
    email_obj = {
        'address': data['address'],
        'type': data['type'],
        'user_id': data['user_id'],
    }
    async with request.app['db'].acquire() as conn:
        await conn.execute(db.email.insert().values(email_obj))
        return web.json_response(email_obj, status=201)


@validate(request_schema=CREATE_PHONE_REQUEST_SCHEMA)
async def create_phone(data, request):
    phone_obj = {
        'number': data['number'],
        'type': data['type'],
        'user_id': data['user_id'],
    }
    async with request.app['db'].acquire() as conn:
        await conn.execute(db.phone.insert().values(phone_obj))
        return web.json_response(phone_obj, status=201)


@validate(request_schema=CREATE_USER_REQUEST_SCHEMA)
async def create_user(data, request):
    context = {}
    user_obj = {
        'full_name': data['user']['full_name'],
        'sex': data['user']['sex'],
        'birthdate': data['user']['birthdate'],
        'living_address': data['user']['living_address'],
    }

    async with request.app['db'].acquire() as conn:
        inserted_user = await conn.execute(db.user.insert().values(user_obj))
        first_row = await inserted_user.first()
        user_id = first_row[0]
        user_obj['id'] = user_id
        context['user'] = user_obj

        if 'phone' in data.keys():
            phone_obj = {
                'number': data['phone']['number'],
                'type': data['phone']['type'],
                'user_id': user_obj['id'],
            }
            inserted_phone = await conn.execute(db.phone.insert().values(phone_obj))
            first_row = await inserted_phone.first()
            phone_id = first_row[0]
            phone_obj['id'] = phone_id
            context['phone'] = phone_obj

        if 'email' in data.keys():
            email_obj = {
                'address': data['email']['address'],
                'type': data['email']['type'],
                'user_id': user_obj['id'],
            }
            inserted_email = await conn.execute(db.email.insert().values(email_obj))
            first_row = await inserted_email.first()
            email_id = first_row[0]
            email_obj['id'] = email_id
            context['email'] = email_obj

        return web.json_response(context, status=201)


@validate(request_schema=UPDATE_USER_REQUEST_SCHEMA)
async def update_user(data, request):
    async with request.app['db'].acquire() as conn:
        user_id = request.match_info['user_id']
        result = await conn.execute(db.user.update()
                                    .returning(*db.user.c)
                                    .where(db.user.c.id == user_id)
                                    .values(data))
        user_record = await result.fetchone()
        user = serialize_user(user_record)
        return web.json_response(user, status=200)


@validate(request_schema=UPDATE_EMAIL_REQUEST_SCHEMA)
async def update_email(data, request):
    async with request.app['db'].acquire() as conn:
        email_id = request.match_info['email_id']
        result = await conn.execute(db.email.update()
                                    .returning(*db.email.c)
                                    .where(db.email.c.id == email_id)
                                    .values(data))
        email_record = await result.fetchone()
        email = serialize_email(email_record)
        return web.json_response(email, status=200)


@validate(request_schema=UPDATE_PHONE_REQUEST_SCHEMA)
async def update_phone(data, request):
    async with request.app['db'].acquire() as conn:
        phone_id = request.match_info['phone_id']
        result = await conn.execute(db.phone.update()
                                    .returning(*db.phone.c)
                                    .where(db.phone.c.id == phone_id)
                                    .values(data))
        phone_record = await result.fetchone()
        phone = serialize_phone(phone_record)
        return web.json_response(phone, status=200)


async def delete_user(request):
    async with request.app['db'].acquire() as conn:
        user_id = request.match_info['user_id']
        await conn.execute(db.user.delete()
                           .where(db.user.c.id == user_id))
        return web.json_response(status=204)


async def delete_email(request):
    async with request.app['db'].acquire() as conn:
        email_id = request.match_info['email_id']
        await conn.execute(db.email.delete()
                           .where(db.email.c.id == email_id))
        return web.json_response(status=204)


async def delete_phone(request):
    async with request.app['db'].acquire() as conn:
        phone_id = request.match_info['phone_id']
        await conn.execute(db.phone.delete()
                           .where(db.phone.c.id == phone_id))
        return web.json_response(status=204)
