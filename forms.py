from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, ValidationError, Email
from wtforms import StringField, PasswordField, SubmitField
from user import User


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email(message="Invalid email"), Length(max=50)],
                        render_kw={"placeholder": "Email"})
    username = StringField(validators=[InputRequired(), Length(4, 20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(4, 20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_username = User.query.filter_by(username=username.data).first()
        if existing_username:
            raise ValidationError("That username already exists")

    def validate_email(self, email):
        existing_email = User.query.filter_by(email=email.data).first()
        if existing_email:
            raise ValidationError("That email address is already registered")


class LoginForm(FlaskForm):
    login_input = StringField(validators=[InputRequired(), Length(4, 50)], render_kw={"placeholder": "Username/Email"})
    password = PasswordField(validators=[InputRequired(), Length(4, 20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")


class ResetRequestForm(FlaskForm):
    login_input = StringField(validators=[InputRequired(), Length(4, 50)], render_kw={"placeholder": "Username/Email"})
    submit = SubmitField("Reset your password")


class ResetPasswordForm(FlaskForm):
    password = PasswordField(validators=[InputRequired(), Length(4, 20)], render_kw={"placeholder": "Password"})
    check_password = PasswordField(validators=[InputRequired(), Length(4, 20)],
                                  render_kw={"placeholder": "Type your password again"})
    submit = SubmitField("Reset your password")
