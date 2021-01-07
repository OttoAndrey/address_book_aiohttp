
def serialize_user(user):
    return{
        'id': user.id,
        'full_name': user.full_name,
        'sex': user.sex.value,
        'birthdate': str(user.birthdate),
        'living_address': user.living_address,
    }


def serialize_email(email):
    return{
        'id': email.id,
        'email': email.address,
        'type': email.type.value,
        'user_id': email.user_id,
    }


def serialize_phone(phone):
    return{
        'id': phone.id,
        'number': phone.number,
        'type': phone.type.value,
        'user_id': phone.user_id,
    }