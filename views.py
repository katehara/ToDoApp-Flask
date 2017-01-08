from flask import redirect, render_template
from todoapp import app

@app.route('/')
def dashboard():
    return  render_template('home.html')

@app.route('/new-task')
def new_task():
    return redirect('/')

@app.route('/rem-task')
def rem_task():
    return redirect('/')

@app.route('/new-category')
def new_cat():
    return redirect('/')

@app.route('/rem-category')
def rem_cat():
    return redirect('/')

@app.route('/new-priority')
def new_pri():
    return redirect('/')

@app.route('/rem-priority')
def rem_pri():
    return redirect('/')