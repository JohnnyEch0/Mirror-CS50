import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 
        request.form.get("birthday")

        name = request.form.get("name")
        if not name:
            redirect("/")

        month = request.form.get("month")
        if not month or not 0< month <13:
            redirect("/")

        day = request.form.get("day")
        if not day or not 0 < day < 32:
            redirect("/")

        # print(name, month, day)
        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)



        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html

        birthdays_list = db.execute("SELECT name, month, day FROM birthdays")

        return render_template("index.html", birthdays=birthdays_list)


