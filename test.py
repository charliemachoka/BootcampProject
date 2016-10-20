from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import TodoList

Base = declarative_base()

engine = create_engine('sqlite:///todo.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def save_data():
	todo1 = TodoList()
	todo1.title = 'Todo One'
	todo1.body = 'Complete Projects'
	todo1.done = False

	todo2 = TodoList()
	todo2.title = 'Todo Two'
	todo2.body = 'Complete Projects Part two'
	todo2.done = False

	session.add(todo1)
	session.add(todo2)
	session.commit()

def save_user():
	user1 = Base()
	user1.username = 'charles'
	user1.email_address = 'user@gmail.com'
	user1.password = 'aggwa'
	

save_data()

#Get todos from DB
print('All Todos')
todos = session.query(TodoList).all()
for todo in todos:
	print(todo.title+'  '+todo.body+'  '+str(todo.done))

todo1 = session.query(TodoList).filter_by(todo_id=1).one()
print(todo1.title+'  '+todo1.body+'  '+str(todo1.done))

print('Delete Record by Id')
session.query(TodoList).filter_by(todo_id=1).delete()
session.commit()

print('Update Record')
session.query(TodoList).filter_by(todo_id=2).update({'body':'This is a sample project'})
session.commit()


