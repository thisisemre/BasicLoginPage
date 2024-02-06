from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String, Column
from flask import Flask
import jwt
from datetime import datetime, timedelta, UTC

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
app.config["SECRET_KEY"] = "123"

db = SQLAlchemy(model_class=Base)

db.init_app(app)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), unique=True, nullable=False)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(250), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def get_token(self, expires=600):
        payload = {
            'user_id': self.id,
            'exp': datetime.now(UTC) + timedelta(seconds=expires),
            'used': False

        }
        return jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256") #algorithmyı os 'e göm

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            if datetime.now(UTC) <= datetime.fromtimestamp(payload['exp'], UTC) and not payload['used']:
                user_id = payload['user_id']
                payload['used'] = True
                return User.query.get(user_id)  # Kullanıcı kimliğini döndür
            else:
                return None

        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None


with app.app_context():
    db.create_all()
