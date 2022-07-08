from .db import Database
from atexit import register

db = Database() # connect db
cur = db.cursor() # get cursor from db

def get_users() -> list:
	users_list = cur.execute("select * from users").fetchall() # execute sql to get users
	return users_list # return list

def create_user_account(user, password):
	cur.execute("insert into users (username, password, highscore) values (?, ?, ?)", (user, password, 0))
	db.commit()

def fetch_info(user):
	data = cur.execute(f"select * from users where username = '{user}'").fetchone()
	return {
		"user": data['username'],
		"password": data['password'],
		"highscore": data['highscore']
	}

def is_highscore(user, score):
	data = fetch_info(user)
	if score > data['highscore']:
		cur.execute(f"update users set highscore = {score} where username = {user}")

# ---------- atexit functions -----------

def on_exit():
	db.disconnect()

register(on_exit)