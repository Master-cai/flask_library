from datetime import datetime, date

from flask import Blueprint, request, jsonify

from APP.extentions import db
from APP.models import BookInfo, User, OrderBooks, Circulation, RecommendBooks

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
    bookNum = int(bookInfo['booknumber'])
    if reviseBook.available_num > bookNum:
        return jsonify({'status': 'fail'})
    reviseBook.num = bookInfo['booknumber']
    db.session.commit()
    return jsonify({'status': 'success'})


# 添加新书
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
        newBook.num = int(booknumber)
        newBook.publisher = press
        newBook.available_num = int(booknumber)
        newBook.description = description
        newBook.link = link
        db.session.add(newBook)
        db.session.commit()
        return jsonify({'status': 'success'})
    oldBook.isbn = ISBN
    oldBook.name = bookname
    oldBook.author = author
    oldBook.num = int(booknumber) + oldBook.num
    oldBook.publisher = press
    oldBook.description = description
    oldBook.link = link
    db.session.commit()
    return jsonify({'status': 'success'})


# 删除用户
@apiAdmin.route('/deleteUser', methods=['POST'])
def api_admin_delete_user():
    userInfo = request.get_json()['params']['data']
    studentNumber = userInfo['studentNumber']
    user = User.query.get(studentNumber)
    if user is None:
        return jsonify({'status': 'fail'})
    db.session.delete(user)
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


@apiAdmin.route('/getBook', methods=['GET'])
def api_admin_get_book():
    books = BookInfo.query.all()
    dataList = []
    for book in books:
        ISBN = book.isbn
        bookName = book.name  # 此处是否为全部书籍数量
        author = book.author
        bookNumber = book.available_num
        press = book.publisher
        t = {
            'ISBN': ISBN,
            'bookname': bookName,
            'author': author,
            'booknumber': bookNumber,
            'press': press
        }
        dataList.append(t)
    data = {
        'data': dataList
    }
    return jsonify(data)


# @apiAdmin.route('/getUser', methods=['GET'])
# def api_admin_get_user():
#     return jsonify()


# 新书采购订单修改
# @apiAdmin.route('/reviseBookProcurement')
# def api_admin_revise_book_procurement():
#     procurement = request.get_json()['params']['data']
#     ISBN = procurement['ISBN']
#     author = procurement['author']
#     bookName = procurement['bookname']
#     press = procurement['press']
#     price = procurement['price']
#     book = OrderBooks.query.get(ISBN)
#     if book is None:
#         return jsonify({'status': 'fail'})
#     book.isbn = ISBN
#     book.author = author
#     book.name = bookName
#     book.price = price
#     book.publisher = press
#     db.session.commit()
#     return jsonify({'status': 'fail'})

# @apiAdmin.route('/deleteBookProcurement', methods=['POST'])
# def api_admin_delete_book_procurement():
#     procurement = request.get_json()['params']['data']
#     ISBN = procurement['ISBN']
#     book = OrderBooks.query.get(ISBN)
#     if book is None:
#         return jsonify({'status': 'fail'})
#     db.session.delete(book)
#     db.session.commit()
#     return jsonify({'status': 'success'})


# @apiAdmin.route('/deleteRecommendBook', methods=['POST'])
# def api_admin_delete_recommendBook():
#     recommendBook = request.get_json()
#     id = recommendBook['key']


# 获取借阅记录------需要删掉展开的借阅日期查询框
@apiAdmin.route('/searchRecord', methods=['POST'])
def api_admin_search_record():
    # print(request.get_json())
    global totalCount
    pageInfo = request.get_json()['params']['parameter']
    page = pageInfo['pageNo']
    pageSize = pageInfo['pageSize']
    recordInfo = request.get_json()['params']['queryParam']
    # print(recordInfo)
    # 更新图书借阅状态
    circulate = Circulation.query.all()
    for c in circulate:
        # print(c)
        if c.status == 1 and date.today() > c.deadline:
            c.status = 3
    db.session.commit()

    # records = Circulation.query.filter(Circulation.sno.contains(studentNo), Circulation.status == status).limit(pageSize).offset((page - 1) * pageSize)
    # totalCount = Circulation.query.filter(Circulation.sno.contains(studentNo),Circulation.status == status).count()
    # print(recordInfo, len(recordInfo))
    if 'status' not in recordInfo:
        records = Circulation.query.limit(pageSize).offset((page - 1) * pageSize)
        # print(records)
        totalCount = Circulation.query.count()
        # 非初始状态
    else:
        if recordInfo['status'] == '0':
            # 输入学号搜索全部书籍
            if 'id' in recordInfo:
                studentNo = recordInfo['id']
                records = Circulation.query.filter(Circulation.sno.like('%{}%'.format(studentNo))).limit(
                    pageSize).offset(
                    (page - 1) * pageSize)
                # print('id : 输入学号搜索全部书籍')
                # print(records.all())
                totalCount = Circulation.query.filter(Circulation.sno.contains(studentNo)).count()
            # 无学号搜索全部书籍
            else:
                records = Circulation.query.limit(pageSize).offset((page - 1) * pageSize)
                # print('id: 无学号搜索全部书籍')
                # print(records)
                totalCount = Circulation.query.count()
        else:
            # 输入学号搜索对应状态书籍
            if 'id' in recordInfo:
                studentNo = recordInfo['id']
                status = recordInfo['status']
                records = Circulation.query.filter(Circulation.sno.contains(studentNo),
                                                   Circulation.status == status).limit(pageSize).offset(
                    (page - 1) * pageSize)
                # print('输入学号搜索对应状态书籍')
                # print(records.all())
                totalCount = Circulation.query.filter(Circulation.sno.contains(studentNo),
                                                      Circulation.status == status).count()
            # 无学号搜索对应状态书籍
            else:
                status = recordInfo['status']
                records = Circulation.query.filter(Circulation.status == status).limit(pageSize).offset(
                    (page - 1) * pageSize)
                # print('无学号搜索对应状态书籍')
                # print(records)
                totalCount = Circulation.query.filter(Circulation.status == status).count()
    dataList = []
    no = 0
    for record in records:
        no += 1
        ISBN = record.isbn
        sno = record.sno
        borrowTime = record.borrow_time
        deadline = record.deadline
        backTime = record.back_time
        status = record.status
        sname = User.query.get(sno).name
        bookName = BookInfo.query.get(ISBN).name
        # print(borrowTime)
        t = {
            'no': no,
            'studentNumber': sno,
            'studentName': sname,
            'status': status,
            'updatedAt': backTime,
            'action': 1,
            'loanTime': borrowTime,
            'deadline': deadline,
            'ISBN': ISBN,
            'bookName': bookName,
            'key': 1,
            'editable': 0
        }
        dataList.append(t)
        # print(borrowTime)
        # print(t)
    d = {
        'data': dataList,
        'pageNo': page,
        'pageSize': pageSize,
        'totalCount': totalCount,
        'totalPage': (totalCount // pageSize) + 1
    }
    return jsonify(d)


# 修改借阅记录----t的格式不对
@apiAdmin.route('/reviseRecord', methods=['POST'])
def api_admin_revise_record():
    record = request.get_json()['params']['data']
    sno = record['studentNumber']
    # print(record)
    ISBN = record['ISBN']
    oldRecord = Circulation.query.filter(Circulation.sno == sno, Circulation.isbn == ISBN).first()
    loanTime = record['loanTime']
    backTime = record['updatedAt']
    deadline = record['deadline']
    status = record['status']
    # dd = "Fri Nov 09 2018 14:41:35 GMT" # 星期: a 月: b 日: d 年: Y
    GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
    # print(datetime.strptime(dd, GMT_FORMAT).date())
    if status == '1' or status == '2' or status == '3':
        oldRecord.status = status
    if loanTime is not None:
        oldRecord.borrow_time = datetime.strptime(loanTime, GMT_FORMAT).date()
    if backTime is not None:
        oldRecord.back_time = datetime.strptime(backTime, GMT_FORMAT).date()
    if deadline is not None:
        oldRecord.deadline = datetime.strptime(deadline, GMT_FORMAT).date()
    db.session.commit()
    return jsonify({'status': 'success'})


# records = Circulation.query.limit(pageSize).offset((page - 1) * pageSize)
# # print(records)
# totalCount = Circulation.query.count()
# 学生荐读——请求数据 -------json格式未定_需新增ISBN字段
@apiAdmin.route('/getRecommendBook', methods=['POST'])
def api_admin_get_recommend():
    recommend = request.get_json()['params']['queryParam']
    pageInfo = request.get_json()['params']['parameter']
    page = pageInfo['pageNo']
    pageSize = pageInfo['pageSize']
    print(recommend)
    if len(recommend) == 0:
        print("初始状态")
        records = RecommendBooks.query.limit(pageSize).offset((page - 1) * pageSize)
        totalCount = RecommendBooks.query.count()
        # 非初始状态
    else:
        if 'status' not in recommend or recommend['status'] == '0':
            # 无学号查找全部信息
            if 'id' not in recommend:
                print("无学号查找全部信息")
                records = RecommendBooks.query.limit(pageSize).offset((page - 1) * pageSize)
                totalCount = RecommendBooks.query.count()
            else:
                print("有学号查找全部信息")
                sno = recommend['id']
                records = RecommendBooks.query.filter(RecommendBooks.sno.contains(sno)).limit(pageSize).offset(
                    (page - 1) * pageSize)
                totalCount = RecommendBooks.query.count()
        else:
            if 'id' not in recommend:
                print("无学号查找状态信息")
                bookStatus = recommend['status']
                records = RecommendBooks.query.filter(RecommendBooks.status == bookStatus).limit(pageSize).offset(
                    (page - 1) * pageSize)
                totalCount = RecommendBooks.query.filter(RecommendBooks.status == bookStatus).count()
            else:
                print("有学号查找状态信息")
                sno = recommend['id']
                bookStatus = recommend['status']
                records = RecommendBooks.query.filter(RecommendBooks.sno.contains(sno),
                                                      RecommendBooks.status == bookStatus).limit(pageSize).offset(
                    (page - 1) * pageSize)
                totalCount = RecommendBooks.query.filter(RecommendBooks.sno.contains(sno),
                                                         RecommendBooks.status == bookStatus).count()
    dataList = []
    no = 0
    for record in records:
        no += 1
        sno = record.sno
        ISBN = record.isbn
        sname = User.query.get(sno).name
        bookName = record.book_name
        reason = record.reason
        status = record.status
        t = {
            'no': no,
            'studentNumber': sno,
            'studentName': sname,
            'status': status,
            'recommendBook': bookName,
            "ISBN": ISBN,
            'recommendReason': reason,
            "loanTime": 1,
        }
        dataList.append(t)
    d = {
        'data': dataList,
        'pageNo': page,
        'pageSize': pageSize,
        'totalCount': totalCount,
        'totalPage': (totalCount // pageSize) + 1
    }
    return jsonify(d)


# 学生荐读——修改数据----需新增ISBN字段
@apiAdmin.route('/reviseRecommendBook', methods=['POST'])
def api_admin_revise_recommend():
    recommend = request.get_json()['params']['data']
    bookName = recommend['recommendBook']
    reason = recommend['recommendReason']
    status = recommend['status']
    sno = recommend['studentNumber']
    ISBN = recommend['ISBN']
    print(ISBN)
    book = RecommendBooks.query.filter(RecommendBooks.sno == sno, RecommendBooks.isbn == ISBN).first()
    # book = RecommendBooks.query.filter(RecommendBooks.sno == sno, RecommendBooks.ibook_name == bookName)
    book.book_name = bookName
    book.reason = reason
    if status == '1' or status == '2' or status == '3':
        book.status = status
        print(status)
    else:
        return jsonify({'status': 'fail'})
    db.session.commit()
    return jsonify({'status': 'success'})


# 新书采购--请求数据
@apiAdmin.route('/bookProcurement', methods=['GET'])
def api_admin_book_procurement():
    books = OrderBooks.query.all()
    dataList = []
    for book in books:
        ISBN = book.isbn
        bookName = book.name
        author = book.author
        bookNumber = book.num
        price = book.price
        press = book.publisher
        t = {
            'ISBN': ISBN,
            'bookname': bookName,
            'author': author,
            'bookNumber': bookNumber,
            'price': price,
            'press': press
        }
        dataList.append(t)
    data = {
        'data': dataList
    }
    return jsonify(data)


# 新书采购--修改数据
@apiAdmin.route('/reviseBookProcurement', methods=['POST'])
def api_admin_revise_book_procurement():
    book = request.get_json()['params']['data']
    ISBN = book['ISBN']
    info = OrderBooks.query.get(ISBN)
    bookName = book['bookname']
    author = book['author']
    bookNumber = book['bookNumber']
    price = book['price']
    press = book['press']
    info.name = bookName
    info.author = author
    info.num = bookNumber
    info.price = price
    info.publisher = press
    db.session.commit()
    return jsonify({'status': 'success'})


# 添加用户
@apiAdmin.route('/getUser', methods=['GET'])
def api_admin_get_User():
    users = User.query.all()
    dataList = []
    for user in users:
        sno = user.sno
        email = user.email
        password = user.password
        mobile = user.phone
        t = {
            'studentNumber': sno,
            'email': email,
            'password': password,
            'mobile': mobile,
        }
        dataList.append(t)
    data = {
        'data': dataList
    }
    return jsonify(data)


# 学生荐读——删除数据
@apiAdmin.route('/deleteRecommendBook', methods=['POST'])
def api_admin_delete_recommend_book():
    recommend = request.get_json()['params']['data']
    ISBN = recommend['ISBN']
    sno = recommend['studentNumber']
    book = RecommendBooks.query.filter(RecommendBooks.sno == sno, RecommendBooks.isbn == ISBN).first()
    if book is None:
        return jsonify({'status': 'fail'})
    db.session.delete(book)
    db.session.commit()
    return jsonify({'status': 'success'})


# 新书采购——删除
@apiAdmin.route('/deleteBookProcurement', methods=['POST'])
def api_admin_delete_book_procurement():
    book = request.get_json()['params']['data']
    ISBN = book['ISBN']
    print(ISBN)
    info = OrderBooks.query.filter_by(isbn=ISBN).first()
    print(info)
    if info is None:
        return jsonify({'status': 'fail'})
    db.session.delete(info)
    db.session.commit()
    return jsonify({'status': 'success'})
