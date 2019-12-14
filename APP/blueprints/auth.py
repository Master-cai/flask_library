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


@login_required
@auth.route('/home/')
def index():
    return render_template('library/home.html')


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))
    form = LoginForm()
    if form.validate_on_submit():
        readerID = form.ReaderID.data
        password = form.password.data
        remember = form.remember.data
        reader = Reader.query.filter_by(RID=readerID).first()
        if reader is not None and reader.validate_password(password):
            login_user(reader, remember=remember)
            flash('Welcome back.', 'info')
            if current_user.is_admin:
                return redirect(url_for('admin.index'))
            else:
                return redirect(url_for('auth.index'))
        flash('Invalid username or password.', 'warning')
    return render_template('auth/login.html', form=form)


@auth.route('/logout/')
@login_required
def logout():
    # print("stage 1")
    logout_user()
    flash('Logout success.', 'info')
    print(url_for('auth.login'))
    return redirect(url_for('auth.login'))


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        password = form.password.data
        RID = form.RID.data
        rName = form.rName.data
        department = form.department.data
        major = form.department.data

        newReader = Reader()
        newReader.password = password
        newReader.RID = RID
        newReader.rName = rName
        newReader.department = department
        newReader.major = major
        # print(newReader)
        # print(newReader.query.all())

        if (newReader.query.filter_by(RID=newReader.RID).first() == None) and \
                (newReader.query.filter_by(rName=newReader.rName).first() == None):
            newReader.set_password(password)
            db.session.add(newReader)
            db.session.commit()
            flash('Congratulations ! Register Successfully !', 'info')
            return redirect(url_for('auth.login'))
        else:
            flash('ID or Nickname already registered')
    return render_template('auth/register.html', form=form)


@auth.route('/createdb/')
def create_db():
    db.create_all()
    return 'Create successfully'


@auth.route('/dropdb/')
def drop_db():
    db.drop_all()
    return 'drop successfully'


@auth.route('/add/')
def add():
    p = Person()
    p.ID = '%d' % random.randrange(100)
    db.session.add(p)
    db.session.commit()
    return 'successfully added'


@auth.route('/page/')
def page():
    pages = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 3, type=int)
    persons = Person.query.limit(per_page).offset((pages - 1) * per_page)
    return render_template('personList.html', personList=persons)


@auth.route('/pag')
@admin_required
def pag():
    pages = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 3, type=int)
    persons = Person.query.paginate(pages, per_page)
    return render_template('personList.html', personList=persons)


@auth.route('/addBooks/')
def addBooks():
    filePath = r'D:\OneDrive\python\DB_library\flask_library\APP\blueprints\books.json'
    with open(filePath, encoding='utf-8') as f:
        js = json.load(f)
        print(js[1])

    for book in js:
        b = Book()
        try:
            b.bName = book['name']
        except KeyError:
            pass
        try:
            b.ISBN = book['ISBN']
        except KeyError:
            pass
        try:
            b.author = book['author']
        except KeyError:
            pass
        try:
            b.publicationDate = book['date'] + '-1'
        except KeyError:
            pass
        try:
            b.press = book['press']
        except KeyError:
            pass
        try:
            b.sum = 10
            b.currNum = 10
        except KeyError:
            pass
        try:
            b.price = int(book['price'].split('.')[0])
        except (KeyError, ValueError):
            pass
        try:
            b.score = book['score']
        except KeyError:
            pass
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


@auth.route('/createAdmin/')
def create_admin():
    reader = Reader()
    reader.RID = 1
    reader.set_password('111111')
    reader.rName = 'admin'
    reader.is_admin = True
    db.session.add(reader)
    db.session.commit()
    return 'Admin success'


@auth.route('/createReader/')
def create_reader():
    num = request.args.get("num", 1, type=int)
    Max = int(Reader.query.order_by(Reader.RID.desc()).first().RID)
    faker = Faker()
    departments = ['Philosophy', 'Economics', 'Law', 'Education', 'Mathematics', 'Astronomy', 'Biology', 'Medicine',
                   'Computer Science']
    for i in range(num):
        newReader = Reader()
        RID = Max + i + 1
        password = '111111'
        rName = faker.name()
        department = choice(departments)
        major = choice(departments)
        borrowNum = 0
        newReader.set_password(password)
        newReader.RID = RID
        newReader.rName = rName
        newReader.department = department
        newReader.major = major
        newReader.borrowNum = borrowNum
        db.session.add(newReader)
        db.session.commit()
    return 'success create %d reader' % num




