@article_api.put(config.API_ROUTE_PREFIX + 'articles/<id>')
def update_article(id):
	try:
		article = Article(id=str(id), title=request.json.get('title'), content=request.json.get('content'), author=request.json.get('author'))
	except ValidationError as e:  # Отловили ошибку PyDantic и записали ее в переменную e
		return e.json()  # Преобразовали ошибку в JSON и вернули ее
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

