from .sql import get_users, create_user_account, fetch_info
from maskpass import advpass
from cerberus import Validator
from .cerberus_schemas import password_schema, username_schema

v = Validator()

def login():
	users = get_users()
	if users:
		while True:
			user = input("Enter username: ")
			data = fetch_info(user)
			if user == 'exit':
				exit()
			og = data['password']
			password = advpass("Enter password: ")
			if password != og:
				print("Wrong password")
			else:
				break
		return { "user": user, "password": password }
	else:
		return False

def create_account():
	while True:
		user = input("Username must have 3 or more characters. ")
		if v.validate({ "name": user }, username_schema):
			break
		else:
			print("Must have 3 or more characters. ")
	while True:
		password = advpass("Password must have 8 or more characters. ")
		if not v.validate({ "password": password }, password_schema):
			print("Must have 8 or more characters. ")
		confirm = advpass("Confirm password: ")
		if password != confirm:
			print("Passwords doesn't match")
		else:
			create_user_account(user, password)
			break