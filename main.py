from flask import Flask, url_for, request

app = Flask(__name__)


@app.route("/")
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'hello world'


@app.route('/alert-hook', methods=['POST', 'GET'])
def deal_hook():
    if request.method == 'GET':
        print('method is get')
        return 'get ok'
    if request.method == 'POST':
        print('method is post')
        return 'post ok'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80, debug=True)
