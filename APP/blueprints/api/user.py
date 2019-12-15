from faker import Faker
from flask import Blueprint, jsonify, request

from APP.extentions import shitBuilder, shits, db
from APP.models import RecommendBooks, BookInfo, User

apiUser = Blueprint('apiUser', __name__)


def init_api_user(app):
    app.register_blueprint(blueprint=apiUser, url_prefix='/api/user/')


@apiUser.route('/login', methods=['GET', 'POST'])
@apiUser.route('/logout', methods=['GET', 'POST'])
def test():
    # print(request.get_json())
    return jsonify(shitBuilder)


@apiUser.route('/info', methods=['GET', 'POST'])
def api_user_info():
    info = request.get_json()
    # role
    # print(info)
    # {'username': 'admin'}
    return jsonify(shits)


# 注册 写入
@apiUser.route('/register', methods=['POST'])
def api_user_register():
    userInfo = request.get_json()['params']
    email = userInfo['email']
    mobile = userInfo['mobile']
    password_md5 = userInfo['password']
    studentNumber = userInfo['studentNumber']
    # print(email, mobile, password_md5, studentNumber)

    # ------------------------------------#
    # sql
    reader = User()
    reader.sno = studentNumber
    reader.password = password_md5
    reader.phone = mobile
    reader.email = email
    db.session.add(reader)
    db.commit()
    # ------------------------------------#
    return 'success'


# 取所有书 读取
@apiUser.route('/book', methods=['GET', 'POST'])
def api_user_book():
    # bookInfo = request.get_json()['params']
    # --------
    # sql
    bookList = BookInfo.query.all()

    # --------
    books = []
    for book in bookList:
        b = {
            'ISBN': book.isbn,
            'bookname': book.name,
            'author': book.author,
            'booknumber': book.num,
            'press': book.press
        }
        books.append(b)
    data = {
        'data': books
    }
    return jsonify(data)


# 新书荐购信息 写入
@apiUser.route('/recommend', methods=['POST'])
def user_api_recommend():
    recommendBookInfo = request.get_json()['params']
    ISBN = recommendBookInfo['ISBN']
    author = recommendBookInfo['author']
    bookName = recommendBookInfo['bookname']
    cause = recommendBookInfo['cause']
    press = recommendBookInfo['press']
    # -----------------------------
    # sql
    recommendBook = RecommendBooks()
    recommendBook.isbn = ISBN
    recommendBook.isbn = ISBN
    recommendBook.isbn = ISBN
    recommendBook.isbn = ISBN
    recommendBook.isbn = ISBN
    recommendBook.isbn = ISBN

    # ------------------------------
    print('recommend:{} {} {} {} {}'.format(ISBN, author, bookName, cause, press))
    return 's'


# 用户查看自己推荐书目的历史情况 读取
@apiUser.route('/getOperation1', methods=['GET'])
def api_user_get_operation1():
    son = request.args.get('son', type=str)
    url = request.url
    print(url)
    # ---------
    # sql select
    # operationRecords
    if son != 'admin':
        histories = RecommendBooks.query.filter_by(sno=son).all()
    else:
        histories = RecommendBooks.query.all()
    # -------
    # bookInfo = request.get_json()['params']
    historiesList = []
    # for history in histories:
    h = {
        'key': 'op1',
        'type': '订购关系生效',
        'name': '曲丽丽',
        'status': 'judging',
        # 'status': 'agree',
        # 'status': 'reject',
        'updatedAt': '2019-10-03  19:23:12',
        'remark': '-'
    }
    historiesList.append(h)
    operations = {
        'data': historiesList
    }

    return jsonify(operations)

