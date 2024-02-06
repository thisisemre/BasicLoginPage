from flask import render_template, url_for, redirect, flash
from flask_login import login_user, LoginManager, login_required, logout_user
from flask_bcrypt import Bcrypt
from forms import LoginForm, RegisterForm, ResetRequestForm, ResetPasswordForm
from user import app, db, User
from mail import send_reset_password_mail

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


@app.route("/", methods={"GET", "POST"})
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if "@" in form.login_input.data:
            user = User.query.filter_by(email=form.login_input.data).first()
        else:
            user = User.query.filter_by(username=form.login_input.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("main"))
    return render_template('login.html', form=form)


@app.route("/register", methods={"GET", "POST"})
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data, 12)
        new_user = User(username=form.username.data, password=hashed_password, email=form.email.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html', form=form)


@app.route("/password/reset", methods={"GET", "POST"})
def reset_request():
    form = ResetRequestForm()
    if form.validate_on_submit():
        if "@" in form.login_input.data:
            user = User.query.filter_by(email=form.login_input.data).first()
        else:
            user = User.query.filter_by(username=form.login_input.data).first()
        if user:
            reset_url = url_for('reset_password', token=user.get_token(), _external=True)
            send_reset_password_mail(user.email, reset_url)
        flash('Mail has been sent successfully!', 'success')
        return redirect(url_for("login"))
    return render_template("reset_request.html", form=form)


@app.route("/password/reset/<token>", methods=["GET", "POST"])
def reset_password(token):
    user = User.verify_token(token)
    if user is None:
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        if form.check_password.data == form.password.data:
            hashed_password = bcrypt.generate_password_hash(form.password.data, 12)
            user.password = hashed_password
            db.session.commit()
            return redirect(url_for('login'))
        else:
            print("Şifreler aynı değil")
    return render_template("change_password.html", form=form)


@app.route("/main", methods={"GET", "POST"})
@login_required
def main():
    return render_template("main.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == '__main__':
    app.run(debug=True)
