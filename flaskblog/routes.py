from flask import render_template, url_for, flash, redirect
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, RegistrationForm1
from flaskblog.models import User, Post


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
def homepage2():
    return render_template('home2.html',posts=posts)

@app.route('/initlogin')
def initlogin():
    return render_template('initlogin.html')

@app.route('/facultylogin',methods=['GET','POST'])
def facultylogin():
    form=LoginForm()
    if form.validate_on_submit():
        if form.email.data=='faculty@blog.com' and form.password.data=='password' :
            flash('You have been logged in !','success')
            return redirect(url_for('homepage2'))
        else:
            flash('login unsuccessfull','danger')
    return render_template('facultylogin.html',title='login',form=form)


@app.route('/register',methods=['GET','POST'])
def register():
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
            flash('You have been logged in !','success')
            return redirect(url_for('homepage'))
        else:
            flash('login unsuccessfull','danger')
    return render_template('login.html',title='login',form=form)



@app.route('/about')
def about():
    return render_template('about.html',title='about')

@app.route('/test')
def test():
    return render_template('test.html',title='test')