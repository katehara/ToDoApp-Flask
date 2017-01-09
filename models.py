from flask.ext.sqlalchemy import SQLAlchemy
from todoapp import app

db = SQLAlchemy(app)

class Task(db.Model):
	__tablename__ = 'task'
	id = db.Column('id', db.Integer, primary_key = True)
	desc = db.Column('description',db.Unicode)
	cat = db.Column('category', db.Unicode, db.ForeignKey(category.name))
	pri = db.Column('Priority', db.Unicode, db.ForeignKey(priority.name))

	priority = db.relationship('Priority', foreign_keys=pri)
	category = db.relationship('Category', foreign_keys=cat)

class Priority(db.Model):
	__tablename__ = 'priority'
	name = db.Column('name', db.Unicode, primary_key=True)

class Category(db.Model):
	__tablename__ = 'category'
	name = db.Column('name', db.Unicode, primary_key=True)