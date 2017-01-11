def create_model():
	from models import db
	db.create_all()

def enter_cats():
	from models import Category , db
	work = Category(name='Work')
	home = Category(name='Home')

	db.session.add(work)
	db.session.add(home)
	db.session.commit()

def enter_pris():
	from models import Priority , db
	high = Priority(name='High')
	med = Priority(name='Medium')
	low = Priority(name='Low')

	db.session.add(high)
	db.session.add(med)
	db.session.add(low)

create_model()
enter_cats()
enter_pris()