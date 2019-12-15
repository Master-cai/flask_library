from flask import Blueprint, request, jsonify

from APP.extentions import db
from APP.models import BookInfo, User

apiAdmin = Blueprint('apiAdmin', __name__)


def init_api_admin(app):
    app.register_blueprint(blueprint=apiAdmin, url_prefix='/api/admin/')


# 删除某书的记录
@apiAdmin.route('/deleteBook', methods=['POST'])
def api_admin_delete_book():
    bookInfo = request.get_json()['params']['data']
    ISBN = bookInfo['ISBN']
    book = BookInfo.query.get(ISBN)
    if book is None:
        return jsonify({'status': 'fail'})
    db.session.delete(book)
    db.session.commit()
    return jsonify({'status': 'success'})


# 修改某书的信息
@apiAdmin.route('/reviseBook', methods=['POST'])
def api_admin_revise_book():
    bookInfo = request.get_json()['params']['data']
    ISBN = bookInfo['ISBN']
    reviseBook = BookInfo.query.get(ISBN)
    reviseBook.name = bookInfo['bookname']
    reviseBook.author = bookInfo['author']
    reviseBook.publisher = bookInfo['press']
    if reviseBook.available_num > bookInfo['booknumber']:
        return jsonify({'status': 'fail'})
    reviseBook.num = bookInfo['booknumber']
    db.session.commit()
    return jsonify({'status': 'success'})


@apiAdmin.route('/insertBook', methods=['POST'])
def api_admin_insert_book():
    bookInfo = request.get_json()['params']['data']
    ISBN = bookInfo['ISBN']
    author = bookInfo['author']
    bookname = bookInfo['bookname']
    booknumber = bookInfo['booknumber']
    press = bookInfo['press']
    link = bookInfo['link']
    description = bookInfo['description']
    oldBook = BookInfo.query.get(ISBN)
    if oldBook is None:
        # print('old')
        newBook = BookInfo()
        newBook.isbn = ISBN
        newBook.name = bookname
        newBook.author = author
        newBook.num = booknumber
        newBook.publisher = press
        newBook.available_num = booknumber
        newBook.description = description
        newBook.link = link
        db.session.add(newBook)
        db.session.commit()
        return jsonify({'status': 'success'})
    oldBook.isbn = ISBN
    oldBook.name = bookname
    oldBook.author = author
    oldBook.num = booknumber + oldBook.num
    oldBook.publisher = press
    oldBook.description = description
    oldBook.link = link
    db.session.commit()
    return jsonify({'status': 'success'})


# 插入新用户
@apiAdmin.route('/insertUser', methods=['POST'])
def api_admin_insert_user():
    userInfo = request.get_json()['params']['data']
    son = userInfo['studentNumber']
    password = userInfo['initPassword']
    oldUser = User.query.get(son)
    if oldUser:
        return jsonify({'status': 'fail'})
    newUser = User()
    newUser.sno = son
    newUser.password = password
    db.session.add(newUser)
    db.session.commit()
    return jsonify({'status': 'success'})


# 修改用户信息
@apiAdmin.route('/reviseUser', methods=['POST'])
def api_admin_revise_user():
    userInfo = request.get_json()['params']['data']
    email = userInfo['email']
    mobile = userInfo['mobile']
    password = userInfo['password']
    son = userInfo['studentNumber']
    oldUser = User.query.get(son)
    oldUser.password = password
    oldUser.phone = mobile
    oldUser.email = email
    db.session.commit()
    return jsonify({'status': 'success'})

# @apiAdmin.route('/s', methods=['GET'])
# def index():
#     return 's'


# @apiAdmin.route('/ab', methods=['GET'])
# def ab():
#     books = BookInfo.query.all()
#     for book in books:
#         book.num = 10
#     db.session.commit()
#     return 's'
