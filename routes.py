from views import *


def setup_routes(app):
    app.router.add_get('/', index)

    app.router.add_post('/emails/list', get_emails_list, name='emails')
    app.router.add_post('/phones/list', get_phones_list, name='phones')
    app.router.add_post('/users/list', get_users_list, name='users')

    app.router.add_put('/emails/create', create_email, name='create-email')
    app.router.add_put('/phones/create', create_phone, name='create-phone')
    app.router.add_put('/users/create', create_user, name='create-user')
