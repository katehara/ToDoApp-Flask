from flask.ext.sqlalchemy import SQLAlchemy
from todoapp import app

db = SQLAlchemy(app)