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


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
