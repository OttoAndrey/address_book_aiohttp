from views import *


def setup_routes(app):
    app.router.add_get('/', index)

    app.router.add_post('/users/list', get_users_list, name='users')
    app.router.add_post('/emails/list', get_emails_list, name='emails')
    app.router.add_post('/phones/list', get_phones_list, name='phones')

    app.router.add_post('/users/{user_id}', get_user_detail, name='user')
    app.router.add_post('/emails/{email_id}', get_email_detail, name='email')
    app.router.add_post('/phones/{phone_id}', get_phone_detail, name='phone')

    app.router.add_put('/users/create', create_user, name='create-user')
    app.router.add_put('/emails/create', create_email, name='create-email')
    app.router.add_put('/phones/create', create_phone, name='create-phone')

    app.router.add_patch('/users/{user_id}/update', update_user, name='update-user')
    app.router.add_patch('/emails/{email_id}/update', update_email, name='update-email')
    app.router.add_patch('/phones/{phone_id}/update', update_phone, name='update-phone')

    app.router.add_delete('/users/{user_id}/delete', delete_user, name='delete-user')
    app.router.add_delete('/emails/{email_id}/delete', delete_email, name='delete-email')
    app.router.add_delete('/phones/{phone_id}/delete', delete_phone, name='delete-phone')
