# 参考： https://github.com/htfc786/wordslearn/commit/56e80060b227171258f22a1c6aa793a2cdfdb9e2?diff=unified#diff-a4bd5d49f1ef748cd6d715a8241651fa2202999e3ae2ee760cabb21f47930365
# jwt：https://juejin.cn/post/7234450312726691898
from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from . import app
from . import db, Users
from . import created_salt, salt_password

@app.route('/user/login', methods=['POST'])
def user_login():
    # 1 获取各种参数
    username = request.json["username"]
    password = request.json["password"]

    # 2 查询盐值
    salt_query = Users.query.filter_by(username=username).first()
    if not salt_query:
        return jsonify({ "code": 400, "msg": "用户名或密码错误" })
    salt = salt_query.salt

    # 3 密码是否正确
    user = Users.query.filter_by(
        username=username,
        password=salt_password(password, salt)
    ).first()
    if not user:
        return jsonify({ "code": 400, "msg": "用户名或密码错误" })
    
    # 4 生成jwt密钥
    access_token = "Bearer " + create_access_token(identity = username)

    return jsonify({
        "code": 200, 
        "msg": "登陆成功", 
        "userid": user.id, 
        "access_token": access_token
    })

@app.route('/user/register', methods=['POST'])
def user_register():
    # 1 获取各种参数
    username = request.json["username"]
    password = request.json["password"]
    confirm = request.json["confirm"]

    # 2 判断验证密码是否相等
    if password != confirm:
        return jsonify({ "code": 400, "msg": "两次输入的密码不一样" })

    # 3 判断是否符合标准空
    if (len(username) < 3) or (len(username) > 16):
        return jsonify({ "code": 400, "msg": "用户名不符合要求" })
    if (len(password) < 3) or (len(password) > 16):
        return jsonify({ "code": 400, "msg": "密码不符合要求" })

    # 4 是否已有此用户
    exists = Users.query.filter_by(username=username).first()
    if exists:
        return jsonify({ "code": 400, "msg": "当前用户名已被注册！" })
    
    # 5 存数据库
    salt = created_salt()
    password_salt = salt_password(password, salt)
    user = Users(
        username=username, 
        password=password_salt,
        salt=salt
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({ "code": 200, "msg": "注册成功！" })
