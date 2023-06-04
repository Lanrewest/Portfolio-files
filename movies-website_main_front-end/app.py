from flask import Flask, render_template, url_for
import json
import urllib.request as request
import ssl

app = Flask(__name__)

api_key = "9b153f4e40437e115298166e6c1b997c"
base_url = "https://api.tmdb.org/3/discover/movie/?api_key="+api_key
# api_key = "0d4788fe34d08fa85c275fec31e7a8ea"
# base_url = "https://api.themoviedb.org/3/movie/550?api_key="+api_key

@app.route("/")
def home():
    ssl._create_default_https_context = ssl._create_unverified_context
    conn = request.urlopen(base_url)
    json_data = json.loads(conn.read())
    background_url = url_for('static', filename='backg.jpg')
    return render_template("base.html", background_url=background_url, data=json_data["results"])


# @app.route("/")
# def home():
#     return "Welcome Home"

@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/about")
def about():
    return render_template('about.html')



if __name__=="__main__":
    app.run(port=8000)
