import tweepy
import pandas as pd
from key_file_vault import access_keys_excel
access_code = pd.read_excel(access_keys_excel)

api_dict = {}
for username in access_code.username:
    row = access_code[access_code.username == username]
    consumer_key = row.consumer_key.tolist()[0]
    consumer_secret = row.consumer_secret.tolist()[0]
    access_token = row.access_token.tolist()[0]
    access_token_secret = row.access_token_secret.tolist()[0]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api_dict[username] = api

#print(api_dict)
def follow_each_other(access_code, api_dict):
    for current_username in api_dict.keys():
        for other_username in access_code[access_code.username != current_username]['username']:
            api_dict[current_username].create_friendship(api_dict[other_username].me().screen_name)
            print(current_username, " follows ", other_username)
