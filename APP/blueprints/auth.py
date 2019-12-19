import json
import random

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
    filePath = r'D:\OneDrive\python\DB_library\flask_library\APP\blueprints\books.json'
    with open(filePath, encoding='utf-8') as f:
        js = json.load(f)
        print(js[1])

    for book in js:
        b = BookInfo()
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
        # try:
        #     b.publicationDate = book['date'] + '-1'
        # except KeyError:
        #     pass
        try:
            b.publisher = book['press']
        except KeyError:
            pass
        try:
            b.sum = 10
            b.available_num = 10
        except KeyError:
            pass
        # try:
        #     b.price = int(book['price'].split('.')[0])
        # except (KeyError, ValueError):
        #     pass
        # try:
        #     b.score = book['score']
        # except KeyError:
        #     pass
        try:
            b.link = book['link']
        except (KeyError, DataError):
            pass
        try:
            db.session.add(b)
            db.session.commit()
        except InternalError:
            print(book['name'] + 'ERROR')
        print(book['name'] + 'done')


@auth.route('/addUser')
def add_user():
    faker = Faker(locale="zh_CN")
    num = request.args.get('num', 1, type=int)
    for i in range(num):
        sno = '20170900{0:04d}'.format(i+164)
        name = faker.name()
        password = 'abe45d28281cfa2a4201c9b90a143095'
        phone = faker.phone_number()
        email = faker.ascii_email()
        user = User()
        user.sno = sno
        user.phone =phone
        user.password = password
        user.name = name
        user.email = email
        db.session.add(user)
        db.session.commit()
    return 'successfully added user {}'.format(num)
# @auth.route('/addCirculation')
# def add_circulation():
#     books = BookInfo.query.all()
#
