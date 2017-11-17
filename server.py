from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from  schoolsql import select_school, insert_school, update_column
from school import School
from  schoolsql  import select_school, insert_school, update_column

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return "chao anh Trung"


@app.route('/login', methods=['POST'])
def login():
    username = request.form['logname']
    school = select_school(username)
    if school is None:
        return home()
    if request.form['logpass'] == school.password:
        session['logged_in'] = True
        session['username'] = school.getUsername()
        return render_template('login.html')
    else:
        return render_template('hello.html')

@app.route('/login', methods= ['POST'])
def login():
    username = request.form['username']
    school = select_school(username)
    if school is None:
        return home()
    if request.form['password'] == school.password:
        session['logged_in'] = True
        session['id_school'] = school.id
    else:
        flash('wrong password')
    return home()

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    username = request.form['username']
    password = request.form['password']
    school = School(None, name, username, password)
    insert_school(school)
    session['logged_in'] = True
    session['username'] = username
    return home()

@app.route('/logout',methods=['GET'])
def logout():
    session['logged_in'] = False
    session['username'] = None
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug= True)
