def create_model():
	from models import db
	db.create_all()

def enter_cats():
	from models import Category
	work = Category(name='work')
	home = Category(name='home')

	db.session.add(work)
	db.session.add(home)
	db.session.commit()

def enter_pris():
	from models import Priority
	high = Priority(name='high')
	med = Priority(name='medium')
	low = Priority(name='low')

	db.session.add(high)
	db.session.add(med)
	db.session.add(low)