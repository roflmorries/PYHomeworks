@article_api.put(config.API_ROUTE_PREFIX + 'articles/<id>')
def update_article(id):
	if 'title' not in request.json or 'content' not in request.json or 'author' not in request.json:
		return flask.jsonify({
				'code': 9,
				'message': 'Title, content, author являются обязательными полями',
				'data': None
			})
	data = article_update.crud(article.dict(), id)
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

