from datetime import datetime
from enum import unique
from flaskapp import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    examname = db.Column(db.String(100),unique=True, nullable=False)
    examcode = db.Column(db.String(100),unique=True, nullable=False)
    exam_date = db.Column(db.DateTime, nullable=False)
    exam_time = db.Column(db.DateTime, nullable=False)
    exam_duration = db.Column(db.DateTime, nullable=False)
    faculty_name = db.Column(db.String(100), nullable=False)
    faculty_post = db.Column(db.String(100), nullable=False)
    facult_email = db.Column(db.String(100),unique=True, nullable=False)
    # user = db.relationship('User', backref='username', lazy=True)
    

    def __repr__(self):
        return f"Post('{self.examname}', '{self.exam_date}')"

class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Admin('{self.username}', '{self.email}', '{self.image_file}')"

