#!/usr/bin/env python3
"""
Basic Flask app
Create a get_locale function with the babel.localeselector decorator.
Use request.accept_languages to determine the best
match with our supported languages.
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """class that set default language and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """a function determine the best match with our supported languages."""
    return request.accept_languages(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """  a single '/' index route """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
