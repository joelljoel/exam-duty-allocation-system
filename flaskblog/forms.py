# from wsgiref.validate import validator
# from xml.dom import ValidationErr
from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField,DateField,TimeField
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
   

    examdate = DateField('Examdate',
                           validators=[DataRequired()])
    examtime = TimeField('ExamTime',
                           validators=[DataRequired()])
    examDuration = TimeField('ExamDuration',
                           validators=[DataRequired()])
    faculty_name = StringField('Facultyname',
                           validators=[DataRequired(), Length(min=2, max=30)])
    faculty_email = StringField('FacultyEmail',
                        validators=[DataRequired(), Email()])
    faculty_post=StringField('Position',validators=[DataRequired()])
    
    submit = SubmitField('Create Exam')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    faculty_post=StringField('position',validators=[DataRequired()])
   
    submit = SubmitField('Update')

    def validate_username(self,username):
        if username.data!= current_user.username:
            user=User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already exists!')

    def validate_email(self,email):
        if email.data!= current_user.email:
            user=User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email  already exists!')
