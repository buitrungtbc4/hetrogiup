from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, jsonify
import os
from school import School
from  schoolsql import select_school, insert_school, update_column
from werkzeug.utils import secure_filename
from strainLinearResgression import strain, predict
import numpy as np
app = Flask(__name__)


@app.route('/')
def welcome():
    if not session.get('logged_in'):
        return render_template('index.html')
    else:
        return render_template("home.html")


@app.route('/home')
def home():
    username = session['username']
    school = select_school(username)
    if school.filepath is not None:
        session['uploaded'] = True
    return render_template("home.html")


@app.route('/login', methods=['POST'])
def login():
    username = request.form['logname'].strip()
    school = select_school(username)
    if school is not None:
        if request.form['logpass'] == school.password:
            session['logged_in'] = True
            session['username'] = username
            session['name'] = school.name
    return redirect('/home')


@app.route('/signup', methods=['POST'])
def signup():
    name = request.form['name']
    username = request.form['username'].strip()
    password = request.form['password'].strip()
    school = School(None, name, username, password)
    if insert_school(school):
        session['logged_in'] = True
        session['username'] = username
        session['name'] = name
    return redirect('/home')


@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return welcome()


# @app.route('/uploadFile',methods =['POST'])
# def uploadFile():
#     file_val = request.formData["file"]
#     print file_val
#     return json.dumps({'status': 'OK', 'data': 'test'})

# config upload fil
UPLOAD_FOLDER = "upload"
ALLOWED_EXTENSIONS = set(['xlsx', 'csv', 'xls'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploadFile', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print filename
            username = session['username']
            update_column(username, 'path_file', filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/home')
    return home()


def path(filename):
    return './upload/' + filename


@app.route('/train', methods=['GET', 'POST'])
def trainning():
    username = session['username']
    filename = select_school(username).filepath
    theta, mu, sigma = strain(path(filename))
    round_theta = np.round(theta,3).tolist()
    round_mu = round(mu,3)
    round_sigma = round(sigma,3)
    return jsonify(
        theta= round_theta,
        mu= round_mu,
        sigma= round_sigma
    )


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
