from flask import render_template, url_for, flash, redirect,session
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, RegistrationForm1,Exam
from flaskblog.models import User, Post
from flask_login import login_user,current_user,logout_user,login_required


#dummy data
posts=[
    {
        'author':'joel',
        'title':'exam ',
        'content':'maths',
        'Faculty':'faculty A',
        'date_posted':'apr 12 2022'
    },
    {
        'author':'gh',
        'title':'exam 2',
        'content':'chemistry',
        'Faculty':'faculty A',
        'date_posted':'apr 13 2022'
    }
]

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('initlogin.html',posts=posts)


@app.route('/home')
def homepage():
    return render_template('home.html',posts=posts)

@app.route('/home2')
@login_required
def homepage2():
    return render_template('home2.html',posts=posts)

@app.route('/initlogin')
def initlogin():
    return render_template('initlogin.html')

@app.route('/facultylogin',methods=['GET','POST'])
def facultylogin():
    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash('You have been logged in !','success')
            return redirect(url_for('homepage2'))
        else:
            flash('Login Unsuccessfull!, Check username and password')
   
    return render_template('facultylogin.html',title='login',form=form)


@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('homepage2'))
    form=RegistrationForm()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created,now login!','success')
        return redirect(url_for('facultylogin'))
    return render_template('register.html',title='register',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=='password' :
            session['logged_in'] = True
            flash('You have been logged in !','success')
            return redirect(url_for('homepage'))
        else:
            flash('login unsuccessfull','danger')
    return render_template('login.html',title='login',form=form)



@app.route('/support')
def support():
    return render_template('support.html',title='support')

@app.route('/test')
def test():
    return render_template('test.html',title='test')

@app.route('/createexam')
def createexam():
    form=Exam()
    # if form.validate_on_submit():
    return render_template('create.html',title='createexam')
    
@app.route('/myexams')
def myexams():
    return render_template('myexams.html',title='my-exams')

@app.route('/managefaculty')
def managefaculty():
    return render_template('managefaculty.html',title='manage-faculty')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))