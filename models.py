from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine



Base = declarative_base()

class TodoList(Base):
    __tablename__ = 'todo'
    todo_id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False, unique=True)
    body = Column(String(255), nullable=False)
    done = Column(Boolean)


class User(Base):
	__tablename__ = 'userdata'
	user_id = Column(Integer,primary_key=True)
	username = Column(String(20),nullable=False,unique=True)
	email_address = Column(String(25),nullable=False)
	password = Column(String(15),nullable=False)

engine = create_engine('sqlite:///todo.db')
Base.metadata.create_all(engine)
