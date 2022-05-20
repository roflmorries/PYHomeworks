@article_api.put(config.API_ROUTE_PREFIX + 'articles/<id>')
def create_article(id):
	if 'title' not in request.json or 'content' not in request.json or 'author' not in request.json:
		return flask.jsonify({
				'code': 9,
				'message': 'Title, content, author являются обязательными полями',
				'data': None
			})
	request.json['update_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.update(id - 1)
		})

@article_api.delete(config.API_ROUTE_PREFIX + 'articles/<id>')
def del_article(id):
	return flask.jsonify({
			'code': 0,
			'message': 'OK',
			'data': article_crud.delete(id - 1)
		})

