from flask_wtf import FlaskForm
from wtforms import Form, StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    first_name = StringField(render_kw={"placeholder": "Имя"}, validators=[validators.InputRequired()])
    last_name = StringField(render_kw={"placeholder": "Фамилия"} ,validators=[validators.InputRequired()])
    email = StringField(render_kw={"placeholder": "Email"} ,validators=[validators.InputRequired(), validators.Email()])
    password = PasswordField(render_kw={"placeholder": "Пароль"} ,validators=[validators.InputRequired(), validators.Length(min=6)])
    confirm_password = PasswordField(render_kw={"placeholder": "Повторите пароль"} ,validators=[validators.InputRequired(), validators.EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField(render_kw={"placeholder": "Email"}, validators=[DataRequired(), Email()])
    password = PasswordField(render_kw={"placeholder": "Пароль"}, validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Войти')
