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

@app.route('/wordsadmin/book/info', methods=['GET'])
@jwt_required()
def wordsadmin_book_info():
    bookid = request.args["bookid"]

    book = Books.query.filter_by(id=bookid).first()
    bookdata = {
        "bookid": book.id,
        "name": book.name,
        "description": book.description,
        "cover": book.cover,
    }
      
    return jsonify({ "code": 200, "msg": "查询成功！", "data": bookdata })

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
        })
      
    return jsonify({ "code": 200, "msg": "查询成功！", "data": groupsdata })

@app.route('/wordsadmin/group/info', methods=['GET'])
@jwt_required()
def wordsadmin_group_info():
    groupid = request.args["groupid"]

    group = Groups.query.filter_by(id=groupid).first()
    #书
    book = Books.query.filter_by(id=group.bookid).first()

    bookdata = {
        "groupid": group.id,
        "group": group.name,
        "book": {
            "bookid": book.id,
            "name": book.name,
        },
    }
      
    return jsonify({ "code": 200, "msg": "查询成功！", "data": bookdata })


@app.route('/wordsadmin/group/add', methods=['POST'])
@jwt_required()
def wordsadmin_group_add():
    group_bookid = request.json["bookid"]
    group_name = request.json["name"]

    if len(group_name) == 0 or len(group_name) > 32:
        return jsonify({ "code": 400, "msg": "请输入正确的组名" })

    exists = Books.query.filter_by(id=group_bookid).first()
    if not exists:
        return jsonify({ "code": 400, "msg": "当前书不存在！" })

    group = Groups(
        name=group_name,
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
    # 删除组
    group = Groups.query.filter_by(id=groupid).first()
    db.session.delete(group)
    db.session.commit()

    return jsonify({ "code": 200, "msg": "删除成功！" })

@app.route('/wordsadmin/group/edit', methods=['POST'])
@jwt_required()
def wordsadmin_group_edit():
    groupid = request.json["groupid"]
    group_name = request.json["name"]

    if len(group_name) == 0 or len(group_name) > 32:
        return jsonify({ "code": 400, "msg": "请输入正确的组名" })
    
    exists = Books.query.filter_by(id=groupid).first()
    if not exists:
        return jsonify({ "code": 400, "msg": "当前书不存在！" })
    
    group = Groups.query.filter_by(id=groupid).first()
    group.name=group_name

    db.session.commit()

    return jsonify({ "code": 200, "msg": "修改成功!" })

@app.route('/wordsadmin/word', methods=['GET'])
@jwt_required()
def wordsadmin_word():
    groupid = request.args["groupid"]

    words = Words.query.filter_by(groupid=groupid).all()
    wordsdata = []
    for word in words:

        word_type = "单词"
        if (word.type == 0):
            word_type = "词组"

        wordsdata.append({
            "id": word.id,
            "word": word.word,
            "pronounce": word.pronounce,
            "chinese": word.chinese,
            "type": word_type,
        })
      
    return jsonify({ "code": 200, "msg": "查询成功！", "data": wordsdata })
#####
@app.route('/wordsadmin/word/add', methods=['POST'])
@jwt_required()
def wordsadmin_word_add():
    word_groupid = request.json["groupid"]
    word_word = request.json["word"]
    word_pronounce = request.json["pronounce"]
    word_chinese = request.json["chinese"]
    word_note = request.json["note"]
    word_type = request.json["type"]

    exists = Groups.query.filter_by(groupid=word_groupid).first()
    if not exists:
        return jsonify({ "code": 400, "msg": "当前组不存在！" })
    
    word_bookid = exists.bookid

    word = Words(
        word=word_word,
        pronounce=word_pronounce,
        chinese=word_chinese,
        note=word_note,
        type=word_type,
        groupid=word_groupid,
        bookid=word_bookid,
    )
    db.session.add(word)
    db.session.commit()
    
    return jsonify({ "code": 200, "msg": "添加成功！" })

@app.route('/wordsadmin/word/del', methods=['POST'])
@jwt_required()
def wordsadmin_word_del():
    wordid = request.json["wordid"]

    # 删除单词
    word = Words.query.filter_by(id=wordid).first()
    db.session.delete(word)
    db.session.commit()

    return jsonify({ "code": 200, "msg": "删除成功！" })

@app.route('/wordsadmin/word/edit', methods=['POST'])
@jwt_required()
def wordsadmin_word_edit():
    word_wordid = request.json["wordid"]
    word_word = request.json["word"]
    word_pronounce = request.json["pronounce"]
    word_chinese = request.json["chinese"]
    word_note = request.json["note"]
    word_type = request.json["type"]
    
    word = Groups.query.filter_by(id=word_wordid).first()
    word.word=word_word
    word.pronounce=word_pronounce
    word.chinese=word_chinese
    word.note=word_note
    word.type=word_type

    db.session.commit()

    return jsonify({ "code": 200, "msg": "修改成功!" })
