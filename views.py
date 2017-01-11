from flask import redirect, render_template, request
from todoapp import app
from models import Task, Priority, Category, db

@app.route('/')
def dashboard():
	return  render_template('home.html', categories = Category.query.all(), priorities = Priority.query.all() , todos = Task.query.all())

@app.route('/new-task')
def new_task():
	desc_add = request.args.get('d',None)
	cat_add = request.args.get('c',None)
	pri_add = request.args.get('p',None)
	db.session.add(Task(desc=desc_add, cat = cat_add, pri = pri_add))
	db.session.commit()
	return redirect('/')

@app.route('/rem-task')
def rem_task():
	id_del = request.args.get('id',None)
	db.session.delete(Task.query.filter_by(id=id_del).first())
	db.session.commit()
	return redirect('/')

@app.route('/new-category',methods=['POST','GET'])
def new_cat():
	name_add = request.args.get('nm',None)
	db.session.add(Category(name=name_add))
	db.session.commit()
	return redirect('/')

@app.route('/rem-category',methods=['POST','GET'])
def rem_cat():
	name_del = request.args.get('nm',None)
	db.session.delete(Category.query.filter_by(name=name_del).first())
	db.session.commit()
	return redirect('/')

@app.route('/new-priority')
def new_pri():
	name_add = request.args.get('nm',None)
	db.session.add(Priority(name=name_add))
	db.session.commit()
	return redirect('/')

@app.route('/rem-priority')
def rem_pri():
	name_del = request.args.get('nm',None)
	db.session.delete(Priority.query.filter_by(name=name_del).first())
	db.session.commit()
	return redirect('/')