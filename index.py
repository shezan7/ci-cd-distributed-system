from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {
        'msg': 'Hello from Shezan!',
        'app_version': '7'
    }

@app.route('/add/<a>/<b>')
def add_route(a, b):
    return {
        'sum': multiply(a, b)
    }

# Input can be both strings and digits
def multiply(x,y):
    if type(x) == str and not x.isdigit():
        return "Invalid Input"

    if type(y) == str and not y.isdigit():
        return "Invalid Input"

    x = int(x)
    y = int(y)
    return x * y


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)








