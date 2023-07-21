from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    username = StringField("Username", id="username_login", validators=[DataRequired()])
    password = PasswordField("Password", id="pwd_login")
    submit = SubmitField("Sign In")
