#!/usr/bin/python3
"""
module that starts a flask web application
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def index():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    "Displays HBNB"
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def dispay_c(text):
    """
    Displays C then value of text variable
    """
    return 'C ' + text.replace('_', ' ')

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text='is cool'):
    """
    displays 'python', then value of text variable
    """
    return "python " + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
