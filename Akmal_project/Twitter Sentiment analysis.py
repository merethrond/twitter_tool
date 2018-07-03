import tweepy
from textblob import TextBlob

consumer_key = "IRsTQwZosT2mCdmPoFZCW8sCw"
consumer_secret =  "TNiL5zjFMrSBA3dacynxjfrSrb184qtcoEIGoBI7KK2m3GhThS"

access_token = "2908245252-2BAC5LKREbO7HbzEtCmsMyxD14ZgTMNcfVP93LJ" 
access_token_secret = "zOzz5PwQVzBKEaDHFFzqoA1zBGBVlGhyUgZWQiEWR8iym"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
AAP_Tweets = api.search('Aam Aadmi Party')
for tweet in AAP_Tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)