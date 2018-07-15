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