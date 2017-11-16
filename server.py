from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from  schoolsql  import select_school, insert_school, update_column

app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
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

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug= True)
