from sqlite3 import connect, Cursor, Row
from .utils import ConfigLoader
from os import mkdir
from os.path import exists

config = ConfigLoader()
config.ensure_config()

class Database:
	def __init__(self):
		if config.get_setting('db') == 'sqlite':
			if not exists('.hangman'):
				mkdir('.hangman')
				self.db = connect(".hangman/database.db")
			else:
				self.db = connect(".hangman/database.db")
			self.db.row_factory = Row
			with open("./src/sql/schema.sql", 'r') as file:
				sql = file.read()
			self.db.execute(sql)
	def cursor(self) -> Cursor:
		return self.db.cursor()
	def disconnect(self):
		self.db.close()
	def commit(self):
		self.db.commit()
