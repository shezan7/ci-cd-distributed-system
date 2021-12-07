from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {
        'msg': 'Hello World!',
        'app_version': '4'
    }

@app.route('/add/<a>/<b>')
def add_route(a, b):
    return {
        'sum': add(a, b)
    }

# Input can be both strings and digits
def add(x,y):
    if type(x) == str and not x.isdigit():
        return "Invalid Input"

    if type(y) == str and not y.isdigit():
        return "Invalid Input"

    x = int(x)
    y = int(y)
    return x + y


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)








