from flask import Flask, url_for
from importlib import import_module
from os import path
from flask_login import LoginManager

# from config import Config
# from flask_bcrypt import Bcrypt
# from flask_bootstrap import Bootstrap

# app = Flask(__name__)
# app.config.from_object(Config)
# bcrypt = Bcrypt(app)
# bootstrap = Bootstrap(app)

# from app import routes, models
# app.run(debug=True, host='0.0.0.0', port='5000')


def apply_themes(app):
    """
    Add support for themes.

    If DEFAULT_THEME is set then all calls to
      url_for('static', filename='')
      will modfify the url to include the theme name

    The theme parameter can be set directly in url_for as well:
      ex. url_for('static', filename='', theme='')

    If the file cannot be found in the /static/<theme>/ lcation then
      the url will not be modified and the file is expected to be
      in the default /static/ location
    """

    @app.context_processor
    def override_url_for():
        return dict(url_for=_generate_url_for_theme)

    def _generate_url_for_theme(endpoint, **values):
        if endpoint.endswith("static"):
            themename = values.get("theme", None) or app.config.get(
                "DEFAULT_THEME", None
            )
            if themename:
                theme_file = "{}/{}".format(themename, values.get("filename", ""))
                if path.isfile(path.join(app.static_folder, theme_file)):
                    values["filename"] = theme_file
        return url_for(endpoint, **values)


def register_blueprints(app):
    lstModule = ["base"]
    for item in lstModule:
        module = import_module("app.{}.routes".format(item))
        app.register_blueprint(module.blueprint)


def create_app(config):
    app = Flask(__name__, static_folder="base/static")
    app.config.from_object(config)
    register_blueprints(app)
    apply_themes(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    return app
