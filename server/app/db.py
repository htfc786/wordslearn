from flask_sqlalchemy import SQLAlchemy
import pymysql

# ModuleNotFoundError: No module named 'MySQLdb'
# flask_sqlalchemy 库使用 MySQLdb
pymysql.install_as_MySQLdb()

#db使用： https://juejin.cn/post/7239296984985288765

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(16))
    password = db.Column(db.String(32))
    salt = db.Column(db.String(6))
    isadmin = db.Column(db.Boolean, default=False)