import sqlite3
import datetime


connection = sqlite3.connect('test.db')
cursor = connection.cursor()


def create_table():
	query = """
	CREATE TABLE IF NOT EXISTS articles (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		title varchar(12) UNIQUE,
		text VARCHAR(300),
		create_at TEXT CURRENT_TIMESTAMP
	)
	"""
	cursor.execute(query)
	connection.commit()


# Создание статьи
def create_article(title, text):
	create_at = datetime.datetime.now()
	cursor.execute(f'INSERT into articles ( title, text, create_at) VALUES ("{title}", "{text}","{create_at}")',)
	connection.commit()


# Удаление статьи
def delete_article(id):
	cursor.execute(f"""DELETE from articles WHERE id ='{id}'""")
	connection.commit()


# Обновление статьи
def update_article(id, title, text):
	cursor.execute(f"""UPDATE articles set text = '{text}', title = '{title}' WHERE id = '{id}'""")
	connection.commit()


# Получение статьи
def get_article(search):
	cursor.execute(f"SELECT * FROM articles WHERE title OR text Like '%{search}%'")
	result = cursor.fetchall()
	print(result)
