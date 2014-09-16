import sys
import csv
import json
import smtplib
from datetime import datetime
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def home():
    # get family list
    try:
        family_list = load_data():
    except ValueError:
        return "Error: could not load data."

    names = sorted([member.name for member in family_list])
    # load home page to display family member table
    return render_template("index.html", names=names)

@app.route("/send/<name>")
def load_pollyanna(name=None):
    # load member object from database
    # send member.polyanna to member.email
    # return page with notice email has been sent
    if not name:
        return "Error: that name doesn't exist."

    try:
        family_data = load_data():
    except ValueError:
        return "Error: could not load data."

    email(name, family_data[name])

def email(name, info):
    # email = info["email"]
    email = "darren.rmc@gmail.com"
    message = """Hello {},

                You're pollyanna is {}.

                Cheers,
                The Ludachristmas Team""".format(name, info["pollyanna"])

    # do the emailing
    server = smtplib.SMTP('smtp.gmail.com', 587)
    with open("email.txt", "r") as email_file:
        line = [item.strip() for item in email_file.readline().split(",")]
        server.login(line[0], line[1])



def load_data():
    current_year = str(datetime.now().year)
    filename = current_year + ".txt"
    with open(filename, "r") as f:
        try:
            return json.loads(f.read())
        except ValueError:
            raise
