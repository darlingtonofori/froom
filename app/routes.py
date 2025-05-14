from flask import render_template, redirect, url_for, request, flash
from app import app, db
from app.models import User, Thread
from datetime import datetime

@app.route('/')
def home():
    threads = Thread.query.all()
    return render_template('home.html', threads=threads)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Failed. Check username and/or password', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Account Created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/thread/<int:thread_id>', methods=['GET', 'POST'])
def thread(thread_id):
    thread = Thread.query.get_or_404(thread_id)
    if request.method == 'POST':
        comment = request.form['comment']
        # Handle comment logic here
    return render_template('thread.html', thread=thread)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and file.mimetype == 'application/octet-stream' and len(file.read()) <= 100*1024*1024:
        file.save(f'uploads/{file.filename}')
        flash('File Uploaded Successfully', 'success')
    else:
        flash('File size exceeds limit, please upload via Dropbox', 'danger')
        return redirect('https://www.dropbox.com/scl/fo/mm5f8x63xf91cl5rxjh82/AG1C9IkSGPEGjP_I9jdZtMk?rlkey=tvxs1j794w1zq8123oz77c1s8&st=gcdumu0u&dl=0')
    return redirect(url_for('home'))
