from flask import request
from flask import render_template, flash, Blueprint
from sqlalchemy import or_

from APP.decorators import admin_required
from APP.models import *
from APP.forms import newBookForm, SearchInfo, ReturnBookForm
from APP.utils import redirect_back

admin = Blueprint('admin', __name__)


def init_admin(app):
    app.register_blueprint(blueprint=admin, url_prefix='/admin/')


@admin.route('/')
@admin_required
def index():
    return render_template('admin/admin.html')


@admin.route('/bookManage/', methods=['GET', 'POST'])
@admin_required
def book_manage():
    form = SearchInfo()
    if form.validate_on_submit():
        pages = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 3, type=int)

        seachtype = form.SearchType.data
        searchInfo = form.SearchInfo.data
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
        if len(books):
            # print(books)
            return render_template('admin/bookManage.html', form=form, booksList=books)
        else:
            flash('No book!', 'danger')
            return redirect_back()
    return render_template('admin/bookManage.html', form=form)


@admin.route('/addBook/', methods=['GET', 'POST'])
@admin_required
def add_book():
    form = newBookForm()
    if form.validate_on_submit():
        BID = form.BID.data
        bName = form.bName.data
        Category = form.Category.data
        ISBN = form.ISBN.data
        author = form.author.data
        publicationDate = form.publicationDate.data
        press = form.press.data
        sum = form.sum.data
        currNum = form.currNum.data
        print(BID, ISBN)
        existBook = Book.query.filter(or_(Book.BID == BID, Book.ISBN == ISBN)).all()
        if len(existBook):
            flash('BID or ISBN has existed!', 'danger')
            return redirect_back()
        newBook = Book()
        newBook.BID = BID
        newBook.bName = bName
        newBook.Category = Category
        newBook.ISBN = ISBN
        newBook.author = author
        newBook.publicationDate = publicationDate
        newBook.press = press
        newBook.sum = sum
        newBook.currNum = currNum
        db.session.add(newBook)
        db.session.commit()
        flash('add successfully', 'info')
        return redirect_back()
    return render_template('admin/addBook.html', form=form)


@admin.route('/deleteBook/')
@admin_required
def delete_book():
    BID = request.args.get('BID', type=int)
    book = Book.query.get(BID)
    db.session.delete(book)
    flash('Delete !', 'success')
    db.session.commit()
    return redirect_back()


@admin.route('/returnBook/', methods=['GET', 'POST'])
@admin_required
def return_book():
    form = ReturnBookForm()
    if form.validate_on_submit():
        RID = form.RID.data
        BID = form.BID.data
        book = Book.query.get(BID)
        if book and book.currNum + 1 <= book.sum:
            book.currNum += 1
            db.session.commit()
            flash('Return successfully !', 'success')
        else:
            flash('no book or book doesn`t need to return!', 'danger')
        return redirect_back()
    return render_template('admin/returnBook.html', form=form)


@admin.route('/readerManage/', methods=['GET', 'POST'])
@admin_required
def reader_manage():
    return 's'
