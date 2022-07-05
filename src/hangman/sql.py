from .db import Database
from atexit import register

db = Database() # connect db
cur = db.cursor() # get cursor from db

def get_users() -> list:
	users_list = cur.execute("select * from users").fetchall() # execute sql to get users
	return users_list # return list

def create_user_account(user, password):
	cur.execute("insert into users (username, password) values (?, ?)", (user, password))
	db.commit()

# ---------- atexit functions -----------

def on_exit():
	db.disconnect()

register(on_exit)