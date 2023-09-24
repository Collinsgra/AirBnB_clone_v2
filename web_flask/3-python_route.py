#!/usr/bin/python3
"""display “HBNB”"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home_page():
    """/ hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """/ hbnb"""
    return 'HBNB'


@app.route('/c/', strict_slashes=False)
@app.route('/c/<text>', strict_slashes=False)
def c(text="is_cool"):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
