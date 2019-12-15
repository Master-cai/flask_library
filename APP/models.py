from flask import session
from flask_login import UserMixin, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

from APP.extentions import db, login_manager


class Reader(db.Model, UserMixin):
    __tablename__ = 'Reader'
    RID = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(32))
    department = db.Column(db.String(20))
    major = db.Column(db.String(20))
    borrowNum = db.Column(db.Integer, default=0)

    @property
    def id(self):
        return self.RID

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class User(db.Model, UserMixin):
    __tablename__ = 'User'
    sno = db.Column(db.String(13), primary_key=True)
    password = db.Column(db.String(32))
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(50), unique=True)


class BookInfo(db.Model):
    __tablename__ = 'BookInfo'
    isbn = db.Column(db.String(15), primary_key=True)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    link = db.Column(db.String(100))
    description = db.Column(db.String(500))
    num = db.Column(db.Integer)
    available_num = db.Column(db.Integer)


class Circulation(db.Model):
    __tablename__ = 'Circulation'
    isbn = db.Column(db.String(15), db.ForeignKey('BookInfo.isbn'), primary_key=True)
    sno = db.Column(db.String(13), db.ForeignKey('User.sno'), primary_key=True)
    borrow_time = db.Column(db.DATE)
    deadline = db.Column(db.DATE)
    back_time = db.Column(db.DATE)


class RecommendBooks(db.Model):
    __tablename__ = 'RecommendBooks'
    isbn = db.Column(db.String(15), primary_key=True)
    sno = db.Column(db.String(13), primary_key=True)
    book_name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    reason = db.Column(db.String(500))
    status = db.Column(db.Integer)  # 状态：1：未处理，2：确认采购，3：拒绝


class OrderBooks(db.Model):
    __tablename__ = 'OrderBooks'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(15))
    price = db.Column(db.Integer)
    date = db.Column(db.DATE)
    name = db.Column(db.String(100))
    author = db.Column(db.String(100))
    publisher = db.Column(db.String(100))
    link = db.Column(db.String(100))
    description = db.Column(db.String(500))
    num = db.Column(db.Integer)
    type = db.Column(db.Integer)  # ？来源：1：读者推荐，2：主动采购，3：读者捐赠？


class Notice(db.Model):
    __tablename__ = 'Notice'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    text = db.Column(db.String(1000))
    date = db.Column(db.DATE)
