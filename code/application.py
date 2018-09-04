from flask import Flask, render_template, request
from api_action_lib import api_dict_creation, user_keys_dataframe, update_same_status,\
 like_from_id, retweet_from_id, retweet_top_status, like_top_status
app = Flask(__name__)

api_dict = api_dict_creation(user_keys_dataframe)
username_list = list(user_keys_dataframe.username)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/retweet_or_like_from_id", methods=["POST"])
def retweet_like_from_twitter_id():
    twitter_id = int(request.form.get("tweet_id"))
    print("retweet checkbox is:", request.form.get("id_retweet_check"))
    print("like checkbox is:", request.form.get("id_like_check"))
    print("Twitter ID is:", twitter_id)
    wait_interval = int(request.form.get("id_wait_interval"))
    # print(str(username_list))
    if request.form.get("id_like_check") == 'on':
        like_from_id(api_dict, twitter_id, wait_interval)
    if request.form.get("id_retweet_check") == 'on':
        retweet_from_id(api_dict, twitter_id, wait_interval)
    return "Operation completed"

@app.route("/tweet", methods = ["POST"])
def tweet_bomb():
    tweet_text = request.form.get("tweet_text")
    wait_interval = int(request.form.get("wait_interval"))
    update_same_status(api_dict, tweet_text, wait_interval)
    return "Tweeted"

@app.route("/retweet_or_like_from_timeline", methods = ["POST"])
def retweet_like_using_screen_name():
    twitter_screen_name = request.form.get("screen_name")
    status_count = int(request.form.get("status_count"))
    print("retweet checkbox is:", request.form.get("timeline_retweet_check"))
    print("like checkbox is:", request.form.get("timeline_like_check"))
    wait_interval = int(request.form.get("timeline_wait_interval"))
    # print(str(username_list))
    if request.form.get("timeline_like_check") == 'on':
        like_top_status(api_dict, twitter_screen_name, status_count, wait_interval)
    if request.form.get("timeline_retweet_check") == 'on':
        retweet_top_status(api_dict, twitter_screen_name, status_count, wait_interval)
    return "Operation completed"
