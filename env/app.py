from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World</h1>'


@app.route('/home/<name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>You are on {} the home page!</h1>'.format(name)


@app.route('/json')
def json():
    return jsonify({'key': 'value', 'key2': [1, 2, 3]})


@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>First {}. Second Item {}!</h1>'.format(name, location)

@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">
            <input type="text" name="name">
            <input type="text" name="location">
            <input type="submit">
            </form>'''
@app.route('/process',methods=['POST'])
def process():
    name=request.form['name']
    location=request.form['location']

    return 'Whats up your {}. You are going to {}. Right'.format(name,location)

if __name__ == '__main__':
    app.run()
