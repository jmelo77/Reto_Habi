import os

class Common(object):
    '''
    Configuration base, for all enviroments.
    '''
    DEBUG = os.environ.get('DEBUG', False)
    VERSION = '1.0'
    HABI_BACKEND_PREFIX = 'habi-api'

class Dev(Common):

    DEBUG = True

    db_config = {
    'host':'3.130.126.210',
    'port':3309,
    'username':'pruebas',
    'password':'VGbt3Day5R',
    'database':'habi_db',
    'charset':'utf8'
    }

class Stg(Common):

    DEBUG = os.environ.get('DEBUG', True)

class Prd(Common):
    
    DEBUG = os.environ.get('DEBUG', False)
