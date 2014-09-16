import sys
import csv
import json
import smtplib
from datetime import datetime
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    # get family list
    try:
        family_list = load_data()
    except ValueError:
        return "Error: could not load data."

    names = sorted(family_list.keys())

    # load home page to display family member table
    # sort people by name --> ordered dict? 
    return render_template("index.html", names=names)

@app.route("/send/<name>")
def load_pollyanna(name=None):
    # load member object from database
    # send member.pollyanna to member.email
    # return page with notice email has been sent
    if not name:
        return "Error: that name doesn't exist."

    try:
        family_data = load_data()
    except ValueError:
        return "Error: could not load data."

    email(name, family_data[name])

def email(name="Darren McCleary", pollyanna="Darren McCleary"):
    # recipient = info["email"]
    ludaxmas = "mccleary.ludachristmas@gmail.com"
    recipient = "darren.rmc@gmail.com"
    message = """Hello {},\n\nYou're pollyanna is {}.\n\nCheers,\nThe Ludachristmas Team
              """.format(name, pollyanna)

    # do the emailing
    with smtplib.SMTP("smtp.gmail.com:587") as server:
        server.ehlo()
        server.starttls()
        with open("email.txt", "r") as email_file:
            line = [item.strip() for item in email_file.readline().split(",")]
            server.login(line[0], line[1])
            server.sendmail(ludaxmas, recipient, message)

def load_data():
    current_year = str(datetime.now().year)
    # filename = current_year + ".txt"
    filename = "data.json"
    with open(filename, "r") as f:
        try:
            return json.loads(f.read())
            # return 
        except ValueError:
            raise


if __name__ == '__main__':
    app.run(debug=True)

