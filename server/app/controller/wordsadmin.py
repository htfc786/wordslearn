from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from . import app
from . import db, Books, Groups, Words

@app.route('/wordsadmin/book', methods=['GET'])
@jwt_required()
def wordsadmin_book():
    books = Books.query.all()
    booksdata = []
    for book in books:
        booksdata.append({
            "bookid": book.id,
            "name": book.name,
            "description": book.description,
            "cover": book.cover,
        })
      
    return jsonify({ "code": 200, "msg": "查询成功！", "data": booksdata })

@app.route('/wordsadmin/book/add', methods=['POST'])
@jwt_required()
def wordsadmin_book_add():
    book_name = request.json["name"]
    book_description = request.json["description"]
    book_cover = request.json["cover"]

    if len(book_name) == 0 or len(book_name) > 32:
        return jsonify({ "code": 400, "msg": "请输入正确的书名" })

    if len(book_description) > 255:
        return jsonify({ "code": 400, "msg": "书的描述天长了！不可大于255字" })
    
    book = Books(
        name=book_name, 
        description=book_description,
        cover=book_cover,
    )
    db.session.add(book)
    db.session.commit()
    
    return jsonify({ "code": 200, "msg": "添加成功！" })

@app.route('/wordsadmin/book/del', methods=['POST'])
@jwt_required()
def wordsadmin_book_del():
    bookid = request.json["bookid"]

    # 删除书下单词
    Words.query.filter_by(bookid=bookid).delete()
    # 删除书下组
    Groups.query.filter_by(bookid=bookid).delete()
    # 删除书
    book = Books.query.filter_by(id=bookid).first()
    db.session.delete(book)
    db.session.commit()

    return jsonify({ "code": 200, "msg": "删除成功！" })

@app.route('/wordsadmin/book/edit', methods=['POST'])
@jwt_required()
def wordsadmin_book_edit():
    bookid = request.json["bookid"]
    book_name = request.json["name"]
    book_description = request.json["description"]
    book_cover = request.json["cover"]

    if len(book_name) == 0 or len(book_name) > 32:
        return jsonify({ "code": 400, "msg": "请输入正确的书名" })

    if len(book_description) > 255:
        return jsonify({ "code": 400, "msg": "书的描述天长了！不可大于255字" })
    
    book = Books.query.filter_by(id=bookid).first()
    book.name=book_name
    book.description=book_description
    book.cover=book_cover

    db.session.commit()

    return jsonify({ "code": 200, "msg": "修改成功!" })

@app.route('/wordsadmin/group', methods=['GET'])
@jwt_required()
def wordsadmin_group():
    bookid = request.args["bookid"]

    groups = Groups.query.filter_by(bookid=bookid).all()
    groupsdata = []
    for group in groups:
        groupsdata.append({
            "groupid": group.id,
            "name": group.name,
            "description": group.description,
        })
      
    return jsonify({ "code": 200, "msg": "查询成功！", "data": groupsdata })

@app.route('/wordsadmin/group/add', methods=['POST'])
@jwt_required()
def wordsadmin_group_add():
    group_bookid = request.json["bookid"]
    group_name = request.json["name"]
    group_description = request.json["description"]

    if len(group_name) == 0 or len(group_name) > 32:
        return jsonify({ "code": 400, "msg": "请输入正确的组名" })

    if len(group_description) > 255:
        return jsonify({ "code": 400, "msg": "书的描述天长了！不可大于255字" })

    exists = Books.query.filter_by(id=group_bookid).first()
    if not exists:
        return jsonify({ "code": 400, "msg": "当前书不存在！" })

    group = Groups(
        name=group_name, 
        description=group_description,
        bookid=group_bookid,
    )
    db.session.add(group)
    db.session.commit()
    
    return jsonify({ "code": 200, "msg": "添加成功！" })

@app.route('/wordsadmin/group/del', methods=['POST'])
@jwt_required()
def wordsadmin_group_del():
    groupid = request.json["groupid"]

    # 删除组下单词
    Words.query.filter_by(groupid=groupid).delete()
    # 删除书
    group = Groups.query.filter_by(id=groupid).first()
    db.session.delete(group)
    db.session.commit()

    return jsonify({ "code": 200, "msg": "删除成功！" })

@app.route('/wordsadmin/group/edit', methods=['POST'])
@jwt_required()
def wordsadmin_group_edit():
    groupid = request.json["groupid"]
    group_name = request.json["name"]
    group_description = request.json["description"]

    if len(group_name) == 0 or len(group_name) > 32:
        return jsonify({ "code": 400, "msg": "请输入正确的书名" })

    if len(group_description) > 255:
        return jsonify({ "code": 400, "msg": "书的描述天长了！不可大于255字" })
    
    exists = Books.query.filter_by(id=groupid).first()
    if not exists:
        return jsonify({ "code": 400, "msg": "当前书不存在！" })
    
    group = Groups.query.filter_by(id=groupid).first()
    group.name=group_name
    group.description=group_description

    db.session.commit()

    return jsonify({ "code": 200, "msg": "修改成功!" })

