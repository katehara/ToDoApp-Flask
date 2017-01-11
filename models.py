from flask_sqlalchemy import SQLAlchemy
from todoapp import db

class Priority(db.Model):
	__tablename__ = 'priority'
	name = db.Column('name', db.String(50), primary_key=True)

	def __init__(self, name):
		self.name = name

class Category(db.Model):
	__tablename__ = 'category'
	name = db.Column('name', db.String(50), primary_key=True)

	def __init__(self, name):
		self.name = name

class Task(db.Model):
	__tablename__ = 'task'
	id = db.Column('id', db.Integer, primary_key = True)
	description = db.Column('description',db.String(140))
	category = db.Column('category', db.String(50), db.ForeignKey(Category.name))
	priority = db.Column('priority', db.String(50), db.ForeignKey(Priority.name))

	priority_r = db.relationship('Priority', foreign_keys=priority)
	category_r = db.relationship('Category', foreign_keys=category)

	def __init__(self, desc,cat, pri):
		self.description = desc
		self.category = cat
		self.priority = pri

# db.create_all()