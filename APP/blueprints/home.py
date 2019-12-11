import random
from flask import Blueprint, render_template, request
from flask import render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user

from APP.extentions import db
from APP.models import *
from APP.forms import SearchInfo
from APP.utils import redirect_back

home = Blueprint('home', __name__)


def init_home(app):
    app.register_blueprint(blueprint=home)


@home.route('/search/', methods=['GET', 'POST'])
def search():
    form = SearchInfo()
    if form.validate_on_submit():
        pages = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 3, type=int)

        seachtype = form.SearchType.data
        searchInfo = form.SearchInfo.data
        print(seachtype)
        print(searchInfo)
        if seachtype == 'BID':
            books = Book.query.filter(Book.BID.like('%{}%'.format(searchInfo))).all()
        if seachtype == 'BookName':
            books = Book.query.filter(Book.bName.like('%{}%'.format(searchInfo))).all()
        if seachtype == 'Category':
            books = Book.query.filter(Book.Category.like('%{}%'.format(searchInfo))).all()
        if seachtype == 'Press':
            books = Book.query.filter(Book.press.like('%{}%'.format(searchInfo))).all()
        if seachtype == 'Author':
            books = Book.query.filter(Book.author.like('%{}%'.format(searchInfo))).all()
        if books != None:
            print(books[0].bName)
            return render_template('library/search.html', form=form, booksList=books)
    return render_template('library/search.html', form=form)


@login_required
@home.route('/borrow/')
def borrow():
    BID = request.args.get('BID', type=int)
    book = Book.query.get(BID)
    if book.currNum > 0:
        book.currNum = book.currNum - 1
        flash('Borrowed.', 'info')
        db.session.commit()
    else:
        flash('No book now!', 'danger')
    return redirect_back()


@home.route('/allb/')
def allb():
    book = Book()
    book.publicationDate = '1234-2-1'
    db.session.add(book)
    db.session.commit()
    searchInfo = '123'
    books = Book.query.filter(Book.BID.like('%{}%'.format(searchInfo))).all()
    print(books)
    return render_template('library/all.html', books=books)
