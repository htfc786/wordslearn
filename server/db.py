from config import * # 导入config
from server import app
from flask_sqlalchemy import SQLAlchemy
import pymysql

# ModuleNotFoundError: No module named 'MySQLdb'
# flask_sqlalchemy 库使用 MySQLdb
pymysql.install_as_MySQLdb()

# 配置数据库信息
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DBUSERNAME}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBDATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(10))
    password = db.Column(db.String(16))