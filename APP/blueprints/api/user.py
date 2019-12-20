from datetime import datetime, date

from flask import Blueprint, jsonify, request

from APP.extentions import shitBuilder, shits, db, basePermission, adminPermissions, userPermissions
from APP.models import RecommendBooks, BookInfo, User, Circulation

apiUser = Blueprint('apiUser', __name__)


def init_api_user(app):
    app.register_blueprint(blueprint=apiUser, url_prefix='/api/user/')


@apiUser.route('/login', methods=['GET', 'POST'])
def test():
    loginInfo = request.get_json()
    username = loginInfo['username']
    password = loginInfo['password']
    if username == 'admin':
        if password == '8914de686ab28dc22f30d3d8e107ff6c':  # password: ant.design
            return jsonify(shitBuilder)
        return jsonify({'status': 'fail'})
    user = User.query.get(username)
    if user is None:
        return jsonify({'status': 'fail'})
    if password == user.password:
        return jsonify(shitBuilder)
    return jsonify({'status': 'fail'})


@apiUser.route('/logout', methods=['GET', 'POST'])
def logout():
    return jsonify({'status': 'success'})


@apiUser.route('/info', methods=['GET', 'POST'])
def api_user_info():
    infos = request.get_json()
    sno = infos['username']
    info = basePermission
    if sno == 'admin':
        return adminPermissions
    else:
        userPermissions['result']['name'] = User.query.get(sno).name
        userPermissions['result']['creatorId'] = sno
        return userPermissions


# 注册 写入
@apiUser.route('/register', methods=['GET', 'POST'])
def api_user_register():
    userInfo = request.get_json()['params']
    print(userInfo)
    name = userInfo['studentName']
    email = userInfo['email']
    mobile = userInfo['mobile']
    password_md5 = userInfo['password']
    studentNumber = userInfo['studentNumber']
    print(email, mobile, password_md5, studentNumber)

    # ------------------------------------#
    # sql
    reader = User()
    reader.sno = studentNumber
    reader.name = name
    reader.password = password_md5
    reader.phone = mobile
    reader.email = email
    db.session.add(reader)
    db.session.commit()
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
            'press': book.publisher
        }
        books.append(b)
    data = {
        'data': books
    }
    return jsonify(data)


# 新书荐购信息 写入
@apiUser.route('/recommend', methods=['POST'])
def user_api_recommend():
    # sno = request.args
    recommendBookInfo = request.get_json()['params']
    sno = recommendBookInfo['studentNumber']
    ISBN = recommendBookInfo['ISBN']
    author = recommendBookInfo['author']
    bookName = recommendBookInfo['bookname']
    cause = recommendBookInfo['cause']
    press = recommendBookInfo['press']
    print(recommendBookInfo)
    print(cause)
    # -----------------------------
    # sql
    recommendBook = RecommendBooks()
    recommendBook.isbn = ISBN
    recommendBook.sno = sno
    recommendBook.author = author
    recommendBook.book_name = bookName
    recommendBook.reason = cause
    recommendBook.publisher = press
    recommendBook.status = 1
    db.session.add(recommendBook)
    db.session.commit()
    # ------------------------------
    return jsonify({'status': 'success'})


# 用户查看自己推荐书目的历史情况 读取
@apiUser.route('/getOperation1', methods=['GET'])
def api_user_get_operation1():
    global status, time, name
    sno = request.args.get('sno', type=str)
    url = request.url
    # print(url)
    # ---------
    # sql select
    # operationRecords
    if sno != 'admin':
        histories = RecommendBooks.query.filter_by(sno=sno).all()
    else:
        histories = RecommendBooks.query.all()
    # -------
    # bookInfo = request.get_json()['params']
    historiesList = []
    for history in histories:
        statusCode = history.status
        if statusCode == 1:
            status = 'judging'
        elif statusCode == 2:
            status = 'agree'
        else:
            status = 'reject'
        name = User.query.get(history.sno).name
        # print(name+'*'*50)
        time = datetime.now()
        h = {
            'key': 'op1',
            'type': '订购关系生效',
            'name': name,
            'status': status,
            'updatedAt': time,
            'remark': '-'
        }
        # 'status': 'agree',
        # 'status': 'reject',
        historiesList.append(h)
    operations = {
        'data': historiesList
    }
    return jsonify(operations)


@apiUser.route('/security', methods=['POST'])
def api_user_security():
    securityInfo = request.get_json()['params']
    oldPassword = securityInfo['oldPassword']
    newPassword = securityInfo['password']
    sno = securityInfo['studentNumber']
    reader = User.query.get(sno)
    if reader is None:
        return jsonify({'status': 'fail'})
    elif reader.password != oldPassword:
        return jsonify({'status': 'fail'})
    else:
        reader.password = newPassword
        db.session.commit()
        return jsonify({'status': 'success'})


# @apiUser.route('/borrowRecord')
# def api_user_borrow_record():
#     son = request.args.get('son', type=str)
#


# 根据不同身份，返回正在借阅的书籍记录
@apiUser.route('/borrowingRecord')
def api_user_borrowing_record():
    user = request.args.get('sno', type=str)
    if user == 'admin':
        records = Circulation.query.filter(
            db.cast(Circulation.borrow_time, db.DATE) <= db.cast(datetime.now(), db.DATE)).all()
    # records = RecordModel.query.filter(db.cast(RecordModel.reporttime, db.DATE) == db.cast(datetime.datetime.now(), db.DATE)).all()
    else:
        records = Circulation.query.filter(
            (db.cast(Circulation.borrow_time, db.DATE) <= db.cast(datetime.now(), db.DATE)),
            Circulation.sno == user
        ).all()
    if len(records) == 0:
        return jsonify({'status': 'fail'})
    dataList = []
    for record in records:
        judge_status(record)
        ISBN = record.isbn
        book = BookInfo.query.get(ISBN)
        bookName = book.name
        author = book.author
        borrowTime = record.borrow_time
        deadline = record.deadline
        t = {
            'ISBN': ISBN,
            'bookName': bookName,
            'author': author,
            'loanTime': borrowTime,
            'deadline': deadline
        }
        dataList.append(t)
    data = {
        'data': dataList,
        'pageSize': 10,
        'pageNo': 1,
        'totalPage': 1,
        'totalCount': 10
    }
    return jsonify(data)


@apiUser.route('/borrowRecord')
def api_user_borrow_record():
    user = request.args.get('sno', type=str)
    if user == 'admin':
        records = Circulation.query.all()
    else:
        # print(user)
        records = Circulation.query.filter_by(sno=user).all()
        if len(records) == 0:
            return jsonify({'status': 'fail'})
        dataList = []
        for record in records:
            judge_status(record)
            ISBN = record.isbn
            book = BookInfo.query.get(ISBN)
            bookName = book.name
            author = book.author
            borrowTime = record.borrow_time
            returnTime = record.back_time
            t = {
                'ISBN': ISBN,
                'bookName': bookName,
                'author': author,
                'loanTime': borrowTime,
                'returnTime': returnTime
            }
            dataList.append(t)
        data = {
            'data': dataList,
            'pageSize': 10,
            'pageNo': 1,
            'totalPage': 1,
            'totalCount': 10
        }
        return jsonify(data)


def judge_status(record):
    if record.status == 1 and record.deadline < date.today():
        record.status = 3
        db.session.commit()
