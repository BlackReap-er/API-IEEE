from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
from connect import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'black5'
app.config['MYSQL_DATABASE_DB'] = 'Details'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
