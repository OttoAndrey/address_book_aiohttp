import asyncio

from aiohttp import web

from db import close_pg, init_pg
from routes import setup_routes
from settings import config

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = web.Application()
app['config'] = config
setup_routes(app)
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app, host='127.0.0.1', port=8000)
