from flask import session
from flask_login import UserMixin, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

from APP.extentions import db, login_manager

# class Reader(db.Model, UserMixin):
#     __tablename__ = 'Reader'
#     RID = db.Column(db.String(20), primary_key=True)
#     password_hash = db.Column(db.String(128))
#     rName = db.Column(db.String(20))
#     is_admin = db.Column(db.Boolean, default=False)
#     department = db.Column(db.String(20))
#     major = db.Column(db.String(20))
#     borrowNum = db.Column(db.Integer, default=0)
#
#     @property
#     def id(self):
#         return self.RID
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def validate_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#
# class Book(db.Model):
#     __tablename__ = 'Book'
#     BID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     bName = db.Column(db.Text)
#     Category = db.Column(db.String(20))
#     ISBN = db.Column(db.String(20), unique=True)
#     author = db.Column(db.Text)
#     publicationDate = db.Column(db.DATE)
#     press = db.Column(db.String(40))
#     sum = db.Column(db.Integer)
#     currNum = db.Column(db.Integer)
#     price = db.Column(db.Integer)
#     score = db.Column(db.Integer)
#     link = db.Column(db.String(60))
#     page = db.Column(db.Integer)
#
#
# class Classify(db.Model):
#     __tablename__ = 'Classify'
#     CID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     classify = db.Column(db.String(20))
#
#
# class BorrowRecord(db.Model):
#     __tablename__ = 'BorrowRecord'
#     BID = db.Column(db.Integer, db.ForeignKey('Book.BID'), primary_key=True)
#     RID = db.Column(db.String(20), db.ForeignKey('Reader.RID'), primary_key=True)
#     borrowTime = db.Column(db.DATE, primary_key=True)
#     deadLine = db.Column(db.DATE)
#
#
# class ReadRecord(db.Model):
#     __tablename__ = 'ReadRecord'
#     BID = db.Column(db.Integer, db.ForeignKey('Book.BID'), primary_key=True)
#     RID = db.Column(db.String(20), db.ForeignKey('Reader.RID'), primary_key=True)
#     borrowTime = db.Column(db.DATE, primary_key=True)
#     backDate = db.Column(db.DATE)
#     punish = db.Column(db.Integer)
#
#
# class Person(db.Model):
#     __tablename__ = 'Person'
#     ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(20))
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     # if 'is_user' in session:
#     #     return Reader.query.filter_by(id=user_id).first()
#     # if Administrator.query.get(user_id):
#     #     return Administrator.query.get(user_id)
#     return Reader.query.get(user_id)


# from APP.extentions import db
#
#
# class User(db.Model, UserMixin):
#     __tablename__ = 'User'
#     sno = db.Column(db.String(13), primary_key=True)
#     password_hash = db.Column(db.String(32))
#     phone = db.Column(db.String(11), unique=True)
#     email = db.Column(db.String(50), unique=True)
#
#     # @property
#     # def id(self):
#     #     return self.RID
#     #
#     # def set_password(self, password):
#     #     self.password_hash = generate_password_hash(password)
#
#
# class BookInfo(db.Model):
#     __tablename__ = 'BookInfo'
#     isbn = db.Column(db.String(15), primary_key=True)
#     name = db.Column(db.String(100))
#     author = db.Column(db.String(100))
#     publisher = db.Column(db.String(100))
#     link = db.Column(db.String(100))
#     description = db.Column(db.String(500))
#     num = db.Column(db.Integer)
#     available_num = db.Column(db.Integer)
#
#
# class Circulation(db.Model):
#     __tablename__ = 'Circulation'
#     isbn = db.Column(db.String(15), primary_key=True)
#     sno = db.Column(db.String(13))
#     borrow_time = db.Column(db.DATE)
#     deadline = db.Column(db.DATE)
#     back_time = db.Column(db.DATE)
#
#
# class RecommendBooks(db.Model):
#     __tablename__ = 'RecommendBooks'
#     isbn = db.Column(db.String(15))
#     sno = db.Column(db.String(13))
#     book_name = db.Column(db.String(100))
#     author = db.Column(db.String(100))
#     publisher = db.Column(db.String(100))
#     reason = db.Column(db.String(500))
#     status = db.Column(db.Integer)  # 状态：1：未处理，2：确认采购，3：拒绝
#
#
# class OrderBooks():
#     __tablename__ = 'OrderBooks'
#     isbn = db.Column(db.String(15))
#     price = db.Column(db.Integer)
#     num = db.Column(db.Integer)
#     date = db.Column(db.DATE)
#     name = db.Column(db.String(100))
#     author = db.Column(db.String(100))
#     publisher = db.Column(db.String(100))
#     link = db.Column(db.String(100))
#     description = db.Column(db.String(500))
#     type = db.Column(db.Integer)  # ？来源：1：读者推荐，2：主动采购，3：读者捐赠？
