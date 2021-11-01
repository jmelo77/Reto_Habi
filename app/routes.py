
from app import api, views, app

'''
API routes defined
'''
label = app.config.get('HABI_BACKEND_PREFIX')
api_version = 'v1'

api.add_resource(views.HealthResource, '/%s/api/%s/health' % (label, api_version))
api.add_resource(views.PropertiesResource, '/%s/api/%s/prop/fil/' % (label, api_version))