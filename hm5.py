from flask import Flask, jsonify

app = Flask(__name__)

ALL_USERS = [
    {
        'username': 'Matthew',
        'age': '18',
        'id': '1'

    },
    {
        'username': 'Jane',
        'age': '20',
        'id': '2'
    },
    {
        'username': 'Wayne',
        'age': '25',
        'id': '3'
    },
    {
        'username': 'Kenzie',
        'age': '27',
        'id': '4'
    }
]


@app.route('/user')
def users():
    return jsonify(ALL_USERS)


@app.route('/user/<int:id>')
def get_id(id):
    for user in range(len(ALL_USERS)):
        if ALL_USERS[user]['id'] == id:
            return jsonify(ALL_USERS[id - 1]['username'], ALL_USERS[id - 1]['age'])
        return 'Пользователя с таким ID не существует!'


app.run('localhost', 8000)
