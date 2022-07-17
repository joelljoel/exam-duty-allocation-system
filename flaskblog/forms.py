from wsgiref.validate import validator
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
         user=User.query.filter_by(username=username.data).first()
         if user:
            raise ValidationError('Username already exists!')

    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email  already exists!')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class RegistrationForm1(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    faculty_post=StringField('position',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class Exam(FlaskForm):
    examname = StringField('Examname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    examcode = StringField('Examcode',
                           validators=[DataRequired(), Length(min=2, max=20)])

    examdate = StringField('Examdate',
                           validators=[DataRequired(), Length(min=2, max=20)])
    faculty_name = StringField('Facultyname',
                           validators=[DataRequired(), Length(min=2, max=20)])
    faculty_email = StringField('Email',
                        validators=[DataRequired(), Email()])
    faculty_post=StringField('Position',validators=[DataRequired()])
    
    submit = SubmitField('Sign Up')

