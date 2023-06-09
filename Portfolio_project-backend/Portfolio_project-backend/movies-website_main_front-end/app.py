from flask import Flask, render_template
import json
import urllib.request as request
import ssl
from flask_cors import CORS

app = Flask(__name__)
core = CORS(app)


@app.route("/")
def home():
    return render_template("index1.html")

@app.route('/login', methods=["GET"], strict_slashes=False)
def login():
    print("login page")
    return render_template('login.html')

@app.route('/sign_up', methods=["GET"], strict_slashes=False)
def sign_up():
    return render_template('signUp.html')

if __name__=="__main__":
    app.run(debug=True)
