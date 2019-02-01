from flask import Flask, request
from service.linkDataBase import LinkDataBase

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/get', methods=['GET', 'POST'])
def get_data():
    obj = LinkDataBase().get_data(request.args['id'])
    print(obj)
    return 'success '

@app.route('/update', methods=['GET'])
def update():
    LinkDataBase().up_data(request.args['id'])
    return 'update'

@app.route('/insert', methods=['GET'])
def insert():
    LinkDataBase().insert_data()
    return 'insert'

@app.route('/delete', methods=['GET'])
def delete():
    LinkDataBase().delete_data(request.args['id'])
    return 'delete'


if __name__ == '__main__':
    app.run()
