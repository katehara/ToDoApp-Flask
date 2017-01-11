from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask:alchemy@localhost/todoapp'

db = SQLAlchemy(app)

# class Priority(db.Model):
# 	__tablename__ = 'priority'
# 	name = db.Column('name', db.String(50), primary_key=True)

# 	def __init__(self, name):
# 		self.name = name

# class Category(db.Model):
# 	__tablename__ = 'category'
# 	name = db.Column('name', db.String(50), primary_key=True)

# 	def __init__(self, name):
# 		self.name = name

# class Task(db.Model):
# 	__tablename__ = 'task'
# 	id = db.Column('id', db.Integer, primary_key = True)
# 	desc = db.Column('description',db.String(140))
# 	cat = db.Column('category', db.String(50), db.ForeignKey(Category.name))
# 	pri = db.Column('priority', db.String(50), db.ForeignKey(Priority.name))

# 	priority = db.relationship('Priority', foreign_keys=pri)
# 	category = db.relationship('Category', foreign_keys=cat)

# 	def __init__(self, desc,cat, pri):
# 		self.desc = desc
# 		self.cat = cat
# 		self.pri = pri

# db.create_all()

from views import *

# @app.route('/')
# def dashboard():
#     return  render_template('home.html', categories = Category.query.all(), priorities = Priority.query.all() , todos = Task.query.all())

# @app.route('/new-task')
# def new_task():
#     return redirect('/')

# @app.route('/rem-task')
# def rem_task():
#     return redirect('/')

# @app.route('/new-category')
# def new_cat():
#     return redirect('/')

# @app.route('/rem-category')
# def rem_cat():
#     return redirect('/')

# @app.route('/new-priority')
# def new_pri():
#     return redirect('/')

# @app.route('/rem-priority')
# def rem_pri():
#     return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)
