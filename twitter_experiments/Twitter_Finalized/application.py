from flask import Flask, render_template, request
from api_action_lib import api_dict_creation, access_code
app = Flask(__name__)

api_dict = api_dict_creation(access_code)
username_list = list(access_code.username)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    twitter_id = request.form.get("tweet_id")
    print("retweet checkbox is:", request.form.get("retweet_check"))
    print("like checkbox is:", request.form.get("like_check"))
    print("Twitter ID is:", twitter_id)
    print(username_list)
    return render_template("hello.html", name=twitter_id)
