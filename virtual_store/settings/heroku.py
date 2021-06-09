import environ

from virtual_store.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env('SECRET_KEY')
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'virtual-store',
    'API_KEY': '672655461637579',
    'API_SECRET': 'PIphqISxwggpeKTsGPI6sd8nfc8'
}
DEFAULT_FILE_STORAGE='cloudinary_storage.storage.MediaCloudinaryStorage'

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
MERCADO_PAGO_PUBLIC_KEY = env('MERCADO_PAGO_PUBLIC_KEY')
MERCADO_PAGO_ACCESS_TOKEN = env('MERCADO_PAGO_ACCESS_TOKEN')
DATABASES = {
    'default' : env.db(),
}