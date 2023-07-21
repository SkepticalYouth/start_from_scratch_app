from flask import Flask, Blueprint
from app import create_app
from config import config_dict

# from flask_mongoengine import MongoEngine
# from flask_login import LoginManager


try:
    config_mode = config_dict["Debug"]
except KeyError:
    exit("Error: Invalid CONFIG_MODE environment variable entry.")
app = create_app(config_mode)
app.secret_key = "super secret key"
app.config["SESSION_TYPE"] = "filesystem"
# app.config["MONGODB_SETTINGS"] = {
#     "db": "your_database",
#     "host": "localhost",
#     "port": 27017,
# }
# db = MongoEngine()
# db.init_app(app)
# login = LoginManager(app)
app.run(debug=True, host="0.0.0.0", port="5001", threaded=True)
