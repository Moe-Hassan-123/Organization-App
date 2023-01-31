"""
@author: Mohamed Hassan
@email: mdhn6832@gmail.com

The app allows for easier handling and organization of projects and deadlines.
"""
from flask_session import Session
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    session,
    )

import Server.server as api

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)


@app.route('/', methods=["POST", "GET"])
def sign_in():
    """A Page for Signing in."""
    if request.method == "GET":
        return render_template('signin.html')

    user_id = request.form["user_id"]
    session["user_id"] = user_id
    session["name"] = api.get_user_data(user_id)
    return redirect(f"/{ session['name'] }")
    

@app.route("/<string>")
def index():
    """Displayes the users projects"""
    if session["user_id"] is None:
        return redirect("/")
    render_template("index.html", projects = api.retrieve_projects())
    