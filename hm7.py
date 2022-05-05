import flask
from flask import Flask, request

app = Flask(__name__)
tasks = []


@app.route('/task', methods=['GET'])
def get_tasks():
    return flask.jsonify(tasks)


@app.route('/task', methods=['POST'])
def create_task():
    data = request.json
    if 'id' in data and 'name' in data and 'details' in data and 'deadline' in data and 'creation' in data:
        id = data['id']
        if len(list(filter(lambda x: x['id'] == id, tasks))) != 0:
            return flask.jsonify({
                'code': 2,
                'message': 'Такая задача уже есть в системе!'
            })
        tasks.append(data)
        return flask.jsonify({
            'code': 0,
            'message': 'Задача создана!'
        })
    return flask.jsonify({
        'code': 1,
        'message': 'У задачи есть необходимые поля: id, name, details, deadline, creation'
    })


@app.route('/task/<int:task_id>', methods=['DELETE'])
def delete_task(task_id: int):
    global tasks
    if len(tasks) >= task_id:
        tasks.pop(task_id - 1)
        return flask.jsonify({
            'code': 0,
            'message': 'Задача удалена!'
        })
    return flask.jsonify({
        'code': 3,
        'message': 'Задача не найдена!'
    })


@app.route('/task/<int:task_id>', methods=['PUT'])
def update_task(task_id: int):
    global tasks
    data = request.json
    if len(tasks) >= task_id:
        if 'id' in data and 'name' in data and 'details' in data and 'deadline' in data and 'creation' in data:
            tasks[task_id - 1] = data
            return flask.jsonify({
                'code': 0,
                'message': 'Задача обновлена!'
            })
        return flask.jsonify({
            'code': 1,
            'message': 'У задачи есть необходимые поля: id, name, details, deadline, creation'
        })
    return flask.jsonify({
        'code': 3,
        'message': 'Задача не найдена!'
    })


if __name__ == '__main__':
    app.run(debug=True)
