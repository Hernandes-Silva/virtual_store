import environ

from virtual_store.settings.base import *

env = environ.Env()

DEBUG = env.bool('DEBUG', False)
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
MERCADO_PAGO_PUBLIC_KEY = env('MERCADO_PAGO_PUBLIC_KEY')
MERCADO_PAGO_ACCESS_TOKEN = env('MERCADO_PAGO_ACCESS_TOKEN')
DATABASES = {
    'DEFAULT' : env.db(),
}