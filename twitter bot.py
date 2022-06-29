import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
tweettopublish = ''
topTrendingUS = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

trends_result = api.trends_place(23424977) #this gets trends for the United States
for trend in trends_result[0]["trends"]: #this is a for each loop but i short circuited it at 1 so it only pulls the top one
    topTrendingUS = (trend["name"])
    break

tweettopublish = topTrendingUS + " is a not as big of an issue as climate change, we need to start paying more attention"
print(tweettopublish)
api.update_status(tweettopublish)
