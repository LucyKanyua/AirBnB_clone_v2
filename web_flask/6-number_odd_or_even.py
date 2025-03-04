#!/usr/bin/python3
"""
The script starts a Flask web application listening on 0.0.0.0:5000
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """displays 'hello HBNB!' on route /"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB' on route '/hbnb'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_c(text):
    """prints a message about C that is contained in <text>"""
    mesg = "C {}".format(text.replace('_', ' '))
    return mesg


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hello_python(text="is cool"):
    """prints a message about python contained in route parameter <text>"""
    mesg = "Python {}".format(text.replace('_', ' '))
    return mesg


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """displays “n is a number” only if n is an integer"""
    mesg = "{} is a number".format(n)
    return mesg


@app.route("/number_template/<int:n>", strict_slashes=False)
def serve_html(n):
    """Renders the html template passing the value n to it"""
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def is_odd_or_even(n):
    """
    displays a HTML page only if n is an integer and states whether
    n is odd or even
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
