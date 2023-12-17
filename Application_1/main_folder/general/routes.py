from flask import Blueprint, render_template

home = Blueprint('home', __name__)

home.route("/", methods=["GET", "POST"])
home.route("/home", methods=["GET", "POST"])
home.route("", methods=["GET", "POST"])
def home():
    message = "Hello World! Default home page."
    return render_template("index.html", message = message)