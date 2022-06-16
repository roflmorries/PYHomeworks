import string
import random

import flask
from flask import request
from datetime import datetime

from pydantic import ValidationError

from core import config

from crud.articles import article_crud
from schemas.articles import Article

article_api = flask.Blueprint('article_api', __name__)


@article_api.get(config.API_ROUTE_PREFIX + 'articles')
def get_articles():
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.get_all()
		})


@article_api.get(config.API_ROUTE_PREFIX + 'articles/<id>')
def get_article(id):
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.get_one(id)
		})


@article_api.post(config.API_ROUTE_PREFIX + 'articles')
def create_article():
	image = request.files['image'].stream.read()
	file_name = (''.join(random.choices(string.ascii_letters, k=10)) + '_' + request.files['image'].filename).replace(' ', '_')
	if 'title' not in request.form or 'content' not in request.form or 'author' not in request.form:
		return flask.jsonify({
				'code': 9,
				'message': 'Title, content, author являются обязательными полями',
				'data': None
			})
	with open(config.MEDIA_FOLDER + file_name, 'wb') as f:
		f.write(image)
	data = dict(request.form)
	data['created_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	data['file_name'] = file_name
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.create(data)
		})


# Обновление
@article_api.put(config.API_ROUTE_PREFIX + 'articles/<id>')
def update_article(id):
	try:
		article = Article(id=str(id), title=request.json.get('title'), content=request.json.get('content'), author=request.json.get('author'))
	except ValidationError as e:
		return e.json()
	data = article_crud.update(article.dict(), id)
	if data is None:
		return flask.jsonify({
				'code': 9,
				'message': 'Статья не найдена',
				'data': None
			})
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': None
		})


# Удаление
@article_api.delete(config.API_ROUTE_PREFIX + 'articles/<id>')
def delete_article(id):
	data = article_delete.crud(article.dict(), id)
	if data is None:
		return flask.jsonify({
			'code': 9,
			'message': 'Статья не найдена!',
			'data': None
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': None
		})



