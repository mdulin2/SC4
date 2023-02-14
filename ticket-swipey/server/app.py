from flask import Flask, render_template, request, Markup, session
from flask_session import Session
import time
import json
import os
from datetime import datetime, timedelta
from tempfile import gettempdir
import uuid

secrets_file = open("secrets_config.json")
secrets_dict = json.load(secrets_file)

app = Flask(__name__)
app.secret_key = secrets_dict["flag"]
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = '../sessions/'
Session(app)

flag = secrets_dict["flag"]

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

@app.route("/", methods=["GET", "POST"])
def home():
    show_flag = ''
    too_late = 'false'

    if 'user' not in session:
        session['user'] = uuid.uuid4().hex
    if 'win' in session:
        show_flag = flag

    if request.method == 'POST':
        if 'user' not in session:
            return render_template("index.html", flag=show_flag, too_late=too_late)

        itemId = None
        quantity = None

        timestamp = datetime.timestamp(datetime.now())
        timestamp_floor = timestamp - (timestamp % 60)
        time_d = timestamp - timestamp_floor

        if time_d < 0.1:
            show_flag = flag
            session['win'] = 'I WIN'
        else:
            too_late='true'

        session.modified = True

    return render_template("index.html", flag=show_flag, too_late=too_late)

if __name__ == '__main__':
  app.run(debug=False)
