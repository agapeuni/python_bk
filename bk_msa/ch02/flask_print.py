# Chapter02
# flask_print.py
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api')
def my_microservice():
    print("request", request)
    print("request.environ", request.environ)
    response = jsonify({'Hello': 'World!'})
    print("response", response)
    print("response.data", response.data)
    return response


@app.route('/test')
def my_microservice2():
    print("request", request)
    print("request.environ", request.environ)
    response = jsonify({'Hello': 'World!'})
    print("response", response)
    print("response.data", response.data)
    return response


if __name__ == '__main__':
    print(app.url_map)
    app.run()
