import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'Dev')
print ('Using %s environment' % ENVIRONMENT)

app = Flask(__name__)
CORS(app, resources={ r'/*': {'origins': '*'}}, supports_credentials=True)
app.config.from_object('app.settings.%s' %  ENVIRONMENT)
api = Api(app)

db_config = {
    'host':'3.130.126.210',
    'port':3309,
    'username':'pruebas',
    'password':'VGbt3Day5R',
    'database':'habi_db',
    'charset':'utf8'
}

from app import routes