from flask import Blueprint, jsonify, request

from APP.extentions import shitBuilder, shits

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
    print(info)
    return jsonify(shits)


# 注册 写入
@apiUser.route('/register', methods=['POST'])
def api_user_register():
    userInfo = request.get_json()['params']
    email = userInfo['email']
    mobile = userInfo['mobile']
    password = userInfo['password']
    studentNumber = userInfo['studentNumber']
    print(email, mobile, password, studentNumber)
    # ------------------------------------#
    # sql
    # ------------------------------------#
    return 'success'


# 取所有书 读取
@apiUser.route('/book', methods=['GET', 'POST'])
def api_user_book():
    # bookInfo = request.get_json()['params']
    # --------
    # sql
    bookList = []
    # --------
    books = []
    # for book in bookList:
    b = {
        'ISBN': 1,
        'bookname': 1,
        'author': 1,
        'booknumber': 1,
        'location': 1
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
    # ------------------------------
    print('recommend:{} {} {} {} {}'.format(ISBN, author, bookName, cause, press))
    return 's'


# 用户查看自己推荐书目的历史情况 读取
@apiUser.route('/getOperation1', methods=['GET'])
def api_user_get_operation1():
    # ---------
    # sql select
    # operationRecords
    # -------
    # bookInfo = request.get_json()['params']
    operationList = []
    # for operation in operationRecords:
    o = {
        'key': 'op1',
        'type': '订购关系生效',
        'name': '曲丽丽',
        'status': 'judging',
        # 'status': 'agree',
        # 'status': 'reject',
        'updatedAt': '2019-10-03  19:23:12',
        'remark': '-'
    }
    operationList.append(o)
    operations = {
        'data': operationList
    }

    return jsonify(operationList)

# #
# @apiUser.route('/book', methods=['POST'])
# def
#
#     return jsonify()
#
#
# #
# @apiUser.route('/book', methods=['POST'])
# def
#
#     return jsonify()
#
#
# #
# @apiUser.route('/book', methods=['POST'])
# def
#     return jsonify()
