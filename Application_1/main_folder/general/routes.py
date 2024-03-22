from flask import Blueprint, render_template
from main_folder import app

app.route("/home", methods=["GET", "POST"])
def home():
    message = "Hello World! Default home page."
    return render_template("index.html", message = message)

app.route("", methods=["GET", "POST"])
def default_page():
    message = "Default page"
    return render_template("index.html", message = message)