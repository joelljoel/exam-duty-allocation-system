from crypt import methods
from flask import render_template, url_for, flash, redirect,session,request
import requests
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm, RegistrationForm1,Exam,UpdateAccountForm
from flaskblog.models import Admin, User, Post
from flask_login import login_user,current_user,logout_user,login_required



#application routes
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return render_template('initlogin.html')


@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/home2')
@login_required
def homepage2():
    return render_template('home2.html')

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
            next_page=request.args.get('next')
            flash('You have been logged in !','success')
            return redirect(next_page) if next_page else  redirect(url_for('homepage2'))
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


# @app.route('/login',methods=['GET','POST'])
# def login():
#     form=LoginForm()
#     if form.validate_on_submit():
#         user=Admin.query.filter_by(email=form.email.data).first()
#         if user and bcrypt.check_password_hash(user.password,form.password.data):
#             login_user(user,remember=form.remember.data)
#             next_page=request.args.get('next')
#             flash('You have been logged in !','success')
#             return redirect(next_page) if next_page else  redirect(url_for('homepage'))
#         else:
#             flash('Login Unsuccessfull!, Check username and password')
   
#     return render_template('login.html',title='login',form=form)



@app.route('/support')
def support():
    return render_template('support.html',title='support')

@app.route('/test')
def test():
    return render_template('test.html',title='test')

@app.route('/createexam',methods=['POST','GET'])
def createexam():
    form=Exam()
    if form.validate_on_submit():
        flash(f'Exam Successfully Created !','success')
        return redirect(url_for('homepage'))
    return render_template('create.html',title='createexam' ,form=form)

@app.route('/manageexam')
def manage_exam():
    return render_template('manageexam.html',title='manage-faculty')
    
@app.route('/myexams')
def myexams():
    return render_template('myexams.html',title='my-exams')

@app.route('/managefaculty')
def managefaculty():
    return render_template('managefaculty.html',title='manage-faculty')

@app.route('/account', methods=['GET','POST'])
@login_required
def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Account Updated!','success')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data= current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html',title='account',image_file=image_file,form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/post/new')
def new_post():
    return render_template('create.html',title='New Post')

@app.route('/updateaccount')
def update_account():
    form=UpdateAccountForm()
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('updateaccount.html',title='Update Account',form=form,image_file=image_file)