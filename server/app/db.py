from flask_sqlalchemy import SQLAlchemy
import pymysql

# ModuleNotFoundError: No module named 'MySQLdb'
# flask_sqlalchemy 库使用 MySQLdb
pymysql.install_as_MySQLdb()

#db使用： https://juejin.cn/post/7239296984985288765

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(16), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    salt = db.Column(db.String(6), nullable=False)
    isadmin = db.Column(db.Boolean, default=False, nullable=False)

class Words(db.Model):
    __tablename__ = 'words'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    word = db.Column(db.String(64), nullable=False)
    pronounce = db.Column(db.String(64), nullable=True)
    chinese = db.Column(db.String(128), nullable=True)
    note = db.Column(db.String(255), nullable=True)
    type = db.Column(db.Boolean, default=True, nullable=False) # 单词类型 1-单词 0-词组
    sound_id = db.Column(db.Integer, nullable=True)
    sound_start = db.Column(db.Float, nullable=True)
    sound_end = db.Column(db.Float, nullable=True)
    groupid = db.Column(db.Integer, nullable=False)
    bookid = db.Column(db.Integer, nullable=False)

class Groups(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    bookid = db.Column(db.Integer, nullable=False)

class Groups(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    cover = db.Column(db.String(2048), nullable=True)


class Sounds(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    url = db.Column(db.String(2048), nullable=False)


