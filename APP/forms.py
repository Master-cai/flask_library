from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, ValidationError, HiddenField, \
    BooleanField, PasswordField, IntegerField, DateTimeField, DateField
from wtforms.validators import DataRequired, Email, Length, Optional, URL, EqualTo


class LoginForm(FlaskForm):
    ReaderID = StringField('ReaderID', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(6, 20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')


class RegisterForm(FlaskForm):
    RID = StringField('RID', validators=[DataRequired(), Length(1, 20)])
    rName = StringField('readerName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(1, 20),
                                                     EqualTo('password_confirm', message='password doesn`t match')])
    password_confirm = PasswordField('Password_confirm', validators=[DataRequired()])
    department = StringField('Department', validators=[DataRequired(), Length(1, 20)])
    major = StringField('Department', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('Register')


class SearchInfo(FlaskForm):
    # SearchType = StringField('SearchType', validators=[DataRequired(), Length(1, 20)])
    typeChoices = ['BID', 'BookName', 'Category', 'Press', 'Author']
    SearchType = SelectField('SearchType', choices=[(t, t) for t in typeChoices])
    SearchInfo = StringField('SearchInfo', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('Search')


class newBookForm(FlaskForm):
    BID = StringField('BID', validators=[DataRequired(), Length(1, 20)])
    bName = StringField('bName', validators=[DataRequired()])
    Category = StringField('Category', validators=[DataRequired(), Length(1, 20)])
    ISBN = StringField('ISBN', validators=[DataRequired(), Length(1, 20)])
    author = StringField('author', validators=[DataRequired(), Length(1, 20)])
    publicationDate = DateField('publicationDate', validators=[DataRequired()])
    press = StringField('press', validators=[DataRequired(), Length(1, 40)])
    sum = IntegerField('sum', validators=[DataRequired()])
    currNum = IntegerField('currNum', validators=[DataRequired()])
    submit = SubmitField('submit')


class ReturnBookForm(FlaskForm):
    RID = StringField('RID', validators=[DataRequired(), Length(1, 20)])
    BID = StringField('BID', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('Return')


class ReaderInfoForm(FlaskForm):
    # SearchType = StringField('SearchType', validators=[DataRequired(), Length(1, 20)])
    typeChoices = ['RID', 'rName', 'department']
    SearchType = SelectField('SearchType', choices=[(t, t) for t in typeChoices])
    SearchInfo = StringField('SearchInfo', validators=[DataRequired(), Length(1, 20)])
    submit = SubmitField('Search')
