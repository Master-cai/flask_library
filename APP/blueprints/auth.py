import json
import random
from datetime import timedelta, date

from random import choice

import requests
from faker import Faker
from flask import Blueprint, render_template, request, jsonify
from flask import render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.exc import DataError, InternalError

from APP.decorators import admin_required
from APP.extentions import shitBuilder, shits
from APP.models import *
from APP.forms import LoginForm, RegisterForm
from APP.utils import redirect_back

auth = Blueprint('auth', __name__)


def init_auth(app):
    app.register_blueprint(blueprint=auth)


@auth.route('/createdb/')
def create_db():
    db.create_all()
    return 'Create successfully'


@auth.route('/dropdb/')
def drop_db():
    db.drop_all()
    return 'drop successfully'


@auth.route('/addBooks/')
def addBooks():
    # filePath = r'D:\OneDrive\python\DB_library\flask_library\APP\blueprints\books.json'
    # with open(filePath, encoding='utf-8') as f:
    #     js = json.load(f)
    #     print(js[1])
    #
    # for book in js:
    #     b = BookInfo()
    #     try:
    #         b.name = book['name']
    #     except KeyError:
    #         pass
    #     try:
    #         b.isbn = book['ISBN']
    #     except KeyError:
    #         pass
    #     try:
    #         b.author = book['author']
    #     except KeyError:
    #         pass
    #     # try:
    #     #     b.publicationDate = book['date'] + '-1'
    #     # except KeyError:
    #     #     pass
    #     try:
    #         b.publisher = book['press']
    #     except KeyError:
    #         pass
    #     try:
    #         b.sum = 10
    #         b.available_num = 10
    #     except KeyError:
    #         pass
    #     # try:
    #     #     b.price = int(book['price'].split('.')[0])
    #     # except (KeyError, ValueError):
    #     #     pass
    #     # try:
    #     #     b.score = book['score']
    #     # except KeyError:
    #     #     pass
    #     try:
    #         b.link = book['link']
    #     except (KeyError, DataError):
    #         pass
    #     try:
    #         db.session.add(b)
    #         db.session.commit()
    #     except InternalError:
    #         print(book['name'] + 'ERROR')
    #     print(book['name'] + 'done')
    books = BookInfo.query.all()
    for book in books:
        book.num = 10
        db.session.commit()
    return 'success'


@auth.route('/addUser')
def add_user():
    faker = Faker(locale="zh_CN")
    num = request.args.get('num', 1, type=int)
    for i in range(num):
        sno = '20170900{0:04d}'.format(i + 164)
        name = faker.name()
        password = 'abe45d28281cfa2a4201c9b90a143095'
        phone = faker.phone_number()
        email = faker.ascii_email()
        user = User()
        user.sno = sno
        user.phone = phone
        user.password = password
        user.name = name
        user.email = email
        db.session.add(user)
        db.session.commit()
    return 'successfully added user {}'.format(num)


@auth.route('/addCirculation')
def add_circulation():
    faker = Faker()
    num = request.args.get('num', 1, type=int)
    books = BookInfo.query.all()
    ISBNs = []
    snos = []
    for book in books:
        ISBNs.append(book.isbn)
    users = User.query.all()
    for user in users:
        snos.append(user.sno)
    for i in range(num):
        borrowTime = faker.date_between(start_date='-100d', end_date='today')
        delte = timedelta(days=60)
        delte2 = timedelta(days=30)
        deadline = borrowTime + delte
        back_time = faker.date_between(start_date=borrowTime, end_date=deadline + delte2)
        if back_time > deadline:
            status = 3
            print(status, back_time)
        else:
            status = 2
        c = Circulation()
        c.isbn = choice(ISBNs)
        c.sno = choice(snos)
        c.borrow_time = str(borrowTime)
        c.deadline = str(deadline)
        # print(borrowTime, deadline, back_time)
        randomStatus = random.randint(1, 4)
        if randomStatus == 1:
            c.status = 1
        else:
            c.status = status
            c.back_time = str(back_time)
        db.session.add(c)
        db.session.commit()
    return 'successful'


@auth.route('/addRecommendbooks')
def add_recommend_books():
    faker = Faker(locale="zh_CN")
    num = request.args.get('num', 1, type=int)
    books = BookInfo.query.all()
    ISBNs = []
    snos = []
    for book in books:
        ISBNs.append((book.isbn, book.name, book.author, book.publisher))
    users = User.query.all()
    for user in users:
        snos.append(user.sno)
    for i in range(num):
        book = choice(ISBNs)
        ISBN = book[0]
        bookName = book[1]
        author = book[2]
        press = book[3]
        sno = choice(snos)
        reason = faker.paragraph()
        status = random.randint(1, 4)
        recommend = RecommendBooks()
        recommend.isbn = ISBN
        recommend.sno = sno
        recommend.book_name = bookName
        recommend.author = author
        recommend.publisher = press
        recommend.reason = reason
        recommend.status = status
        db.session.add(recommend)
        db.session.commit()
    return 's'


@auth.route('/addOrders/')
def addOrders():
    filePath = r'D:\OneDrive\python\DB_library\flask_library\APP\blueprints\books.json'
    with open(filePath, encoding='utf-8') as f:
        js = json.load(f)
        print(js[1])
    faker = Faker(locale='zh_CN')
    for book in js:
        b = OrderBooks()
        try:
            b.name = book['name']
        except KeyError:
            pass
        try:
            b.isbn = book['ISBN']
        except KeyError:
            pass
        try:
            b.author = book['author']
        except KeyError:
            pass
        try:
            b.publisher = book['press']
        except KeyError:
            pass
        try:
            b.link = book['link']
        except (KeyError, DataError):
            pass
        b.num = 10
        b.price = random.randint(1, 100)
        b.date = str(faker.date_between(start_date='-100d', end_date='today'))
        b.description = faker.paragraph()
        b.type = random.randint(1, 3)
        try:
            db.session.add(b)
            db.session.commit()
        except InternalError:
            print(book['name'] + 'ERROR')
        print(book['name'] + 'done')
        return 'successful'
