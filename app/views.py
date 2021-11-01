import pymysql
from flask import request
from flask_restful import Resource
from app import db_config, ENVIRONMENT

class HTTPStatusCode(object):
    HTTP_400_BAD_REQUEST = 400
    HTTP_401_UNAUTHORIZED = 401
    HTTP_200_OK = 200
    HTTP_204_NO_CONTENT = 204
    HTTP_500_SERVER_ERROR = 500

status = HTTPStatusCode()

class HealthResource(Resource):
    """
    Servicio para revisar que la API y la conexion a la BD esta OK
    """
    def get(self):
        is_database_working = True
        try:
            query = 'SELECT 1'
            conn = pymysql.connect(host=db_config['host'],
                                    user=db_config['username'],
                                    passwd=db_config['password'],
                                    db=db_config['database'],
                                    port=db_config['port'],
                                    charset=db_config['charset'])
            cursor = conn.cursor()
            cursor.execute(query)
        except Exception as e:
            output = str(e)
            is_database_working = False
        return {"status": "-- Service Habi.co online --",
                "env": ENVIRONMENT,
                "db_status": "OK" if is_database_working else output}, status.HTTP_200_OK

class PropertiesResource(Resource):
    """
    Servicio para listar las propiedades
    """
    def post(self):
        sql="SELECT pro.address, pro.city, sta.name AS status, pro.price, pro.description \
            FROM status_history AS sta_his \
            INNER JOIN property AS pro ON sta_his.property_id=pro.id \
            INNER JOIN status AS sta ON sta_his.status_id=sta.id \
            WHERE (sta_his.status_id = '3' OR sta_his.status_id = '4' OR sta_his.status_id = '5') "    
        conn = None
        try:
            fil = request.get_json()
            filKey = fil.keys()
            filVal = fil.values()
            listFilKey = list(filKey) 
            listFilVal = list(filVal)
        
            if len(filVal) > 0:
                prefix = ""
                w = "AND "
                for k in range(len(listFilVal)):
                    if listFilKey[k]=="status":
                        prefix="sta."
                        listFilKey[k]="name"
                    else:
                        prefix="pro."
                    w+=prefix+str(listFilKey[k])+"= '"+str(listFilVal[k])+"' AND "
    
                where = (w).rstrip("AND ")
                query=sql+where        
            else:
                query=sql
            conn = pymysql.connect(host=db_config['host'],
                                    user=db_config['username'],
                                    passwd=db_config['password'],
                                    db=db_config['database'],
                                    port=db_config['port'],
                                    charset=db_config['charset'])
            cursor = conn.cursor()
            cursor.execute(query)
            cols = [field[0] for field in cursor.description]
            rows = cursor.fetchall()
            resp = [dict(zip(cols, row)) for row in rows]
            return resp, status.HTTP_200_OK

        except Exception as exec:
            raise ConnectionError(str(exec)) from exec
        finally:
            if conn:
                conn.close()            