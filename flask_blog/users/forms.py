from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from flask_blog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердить пароль:', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    @staticmethod
    def validata_username(username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Это имя занято. Выберите другое')

    @staticmethod
    def validata_email(email):
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('Пользователь с таким email-ом уже существует')


class LoginForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль:', validators=[DataRequired()])
    remember = BooleanField('Напомнить пароль')
    submit = SubmitField('Войти')


class UpdataAccountForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    picture = FileField('Обновить фото профиля', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Обновить')

    @staticmethod
    def validata_username(username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Это имя занято. Выберите другое')

    @staticmethod
    def validata_email(email):
        if email.data != current_user.email:
            user = User.query.filter_by(username=email.data).first()
            if user:
                raise ValidationError('Пользователь с таким email-ом уже существует')


class RequestResetForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    submit = SubmitField('Изменить пароль')

    @staticmethod
    def validate_email(email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Аккаунт с таким адресом не существует')

