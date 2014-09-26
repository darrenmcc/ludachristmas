import sys
import csv
import json
import smtplib
from datetime import datetime
from flask import Flask, render_template, url_for, redirect
from ludaxmas_api import Family

app = Flask(__name__)
Family = Family()

@app.route("/", methods=["GET"])
def home():
    # try:
    #     family_list = load_data()
    # except ValueError:
    #     return "Error: could not load data."

    # names = sorted(family_list.keys())
    names = sorted(Family.get_names())

    # load home page to display family member table
    return render_template("index.html", names=names)

@app.route("/<name>")
def load_pollyanna(name=None):
    # load member object from database
    # send member.pollyanna to member.email
    # return page with notice email has been sent
    
    if not name:
        return "Error: that name doesn't exist."

    try:
        family_list = load_data()
        for member in family_list: # this sucks
            if member.name == name:
                recipient = member
                break

    except ValueError:
        return "Error: could not load data."

    email(recipient)
    return render_template("email_sent.html", email=recipient.email)

def email(recipient):
    ludaxmas = "mccleary.ludachristmas@gmail.com"
    year = str(datetime.now().year)
    first_name = recipient.name.split()[0]

    if recipient.participating:
        body = "You're pollyanna is {}.".format(recipient.pollyanna)
    else:
        body = "You don't have a pollyanna {}. Such a curmudgeon...".format(first_name)

    message = """Subject: Your {} Pollyanna\n\nHello {},\n\n{}\n\nCheers,\nThe LudaChristmas Team
              """.format(year, first_name, body)

    # do the emailing
    # server = smtplib.SMTP("smtp.gmail.com:587")
    # server.ehlo()
    # server.starttls()
    # with open("email.txt", "r") as email_file:
    #     username, password = [item.strip() for item in email_file.readline().split(",")]
    #     server.login(username, password)
    #     server.sendmail(ludaxmas, recipient.email, message)
    # server.quit()

def load_data():
    # current_year = str(datetime.now().year)
    # filename = current_year + ".txt"
    filename = "data_list.json"
    with open(filename, "r") as f:
        try:
            family_list = json.loads(f.read())
            # return 
        except ValueError:
            raise

    return [FamilyMember(**info) for info in family_list if info["participating"]]

if __name__ == '__main__':
    app.run(debug=True)

