from flask import render_template, request, session
from app.base import blueprint

# from flask_login import login_required


@blueprint.route("/")
def route_default():
    return render_template("index.html")


@blueprint.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")
