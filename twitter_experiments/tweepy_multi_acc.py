import tweepy
import pandas as pd
from vault import user_keys_excel
access_code = pd.read_excel(user_keys_excel)

def api_dict_creation(access_code):
    '''
    args: access_code
    Api Dictionary creation from excel file
    return : api_dict
    '''
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
    return api_dict
api_dict = api_dict_creation(access_code)
def follow_each_other(access_code, api_dict):
    '''
    args : access_code, api_dict
    Follows the account by picking up the all the username from the dictionary except the current username
    Return : None
    '''
    for current_username in api_dict.keys():
        for other_username in access_code[access_code.username != current_username]['username']:
            try:
                api_dict[current_username].create_friendship(api_dict[other_username].me().screen_name)
                print(current_username, " follows ", other_username)
            except:
                print(current_username, " already follows ", other_username)

def create_tweet_file():
    '''
    args : api_dict,
    read api excel, copy user column and write to new tweet excel file
    use this tweet file, write tweets in new column called tweets,
    Return : None
    '''
    writer = pd.ExcelWriter("user_tweets.xlsx")
    df = pd.DataFrame()
    df["username"] = access_code.username
    df['tweet'] = access_code.username
    df.to_excel("user_tweets.xlsx")

#update status
def update_status_from_excel():
    '''
args : api_dict,
Opens the excel file, picks up the tweets and tweets for the current username
Return : None
    '''
    df = pd.read_excel('excel_files/user_tweets.xlsx')
    for current_username in df.username:
        print(current_username)
        tweet = api_dict[current_username].update_status(df.tweet)
        print(tweet.text)

#update status & #retweet
def tweet_retweet(tweet_text = 'I am a sample tweet'):
    '''
    Args: tweet_text
    This function tweets a particular tweet from multiple accounts
    Then it retweet that tweet from other accounts.
    Returns: None
    '''
    for current_username in api_dict.keys():
        print(current_username)
        tweet = api_dict[current_username].update_status(tweet_text)
        print(tweet.text)
        for other_username in access_code[access_code.username != current_username]['username']:
            try:
                api_dict[other_username].retweet(tweet.id)
                print(other_username, " Retweets ", current_username , "Tweet text:", tweet.text)
            except Exception as e:
                print('ERROR:',e,'from id',other_username,'on retweeting',tweet.text)

# create_tweet_file()
# update_status()

# follow_each_other(access_code, api_dict)
