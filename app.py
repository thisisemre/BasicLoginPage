from flask import Flask, render_template, url_for, redirect
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt()


class Base(DeclarativeBase):
    pass


class RegiserForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(4, 20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(4, 20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    def validate_username(self, username):
        existing_username = User.query.filter_by(username=username.data).first()
        if existing_username:
            raise ValidationError("That username alread exists")


class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(4, 20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(4, 20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "123"

db = SQLAlchemy(model_class=Base)

db.init_app(app)


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route("/",methods={"GET", "POST"})
def home():
    return render_template('index.html')


@app.route("/login", methods={"GET", "POST"})
def login():
    form = LoginForm()
    return render_template('login.html', form=form)



@app.route("/register", methods={"GET", "POST"})
def register():
    form = RegiserForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html', form=form)


@app.route("/main")
def main():
    return render_template("main.html")


if __name__ == '__main__':
    app.run(debug=True)
