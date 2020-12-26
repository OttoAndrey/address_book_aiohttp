import pathlib

import yaml
from sqlalchemy_imageattach.stores.fs import FileSystemStore

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'address_book_aiohttp' / 'config.yaml'
DSN = 'postgresql://{user}:{password}@{host}:{port}/{database}'


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config


config = get_config(config_path)

store = FileSystemStore(
    path='media/images',
    base_url='http://127.0.0.1:8000/'
)