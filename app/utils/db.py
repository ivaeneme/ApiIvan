import flask_mysqldb
from flask_mysqldb import MySQL

conexMysql = flask_mysqldb.MySQL()

def init_app(app):
    conexMysql.init_app(app)