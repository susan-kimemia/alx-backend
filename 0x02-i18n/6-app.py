#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """class that set default language and timezone"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """making sure this execute before anything"""
    user = get_user()
    g.user = user


def get_user():
    """
    unction that returns a user dictionary or None if the
    ID cannot be found or if login_as was not passed
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))
    return None


@babel.localeselector
def get_locale() -> str:
    """
    a function determine the best match
    with our supported languages.
    """
    # Force locale with URL parameter
    url_locale = request.args.get('locale')
    if url_locale in app.config['LANGUAGES']:
        print(url_locale)
        return url_locale
    # getting locale from user settings
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        """getting the language from user settings"""
        return g.user['locale']
    # locale from user header
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """a method that render the index"""
    # title = _("home_title")
    # header = _("home_header")
    # return render_template('3-index.html', title=title, header=header)
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(debug=True)
