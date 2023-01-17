import tweepy 
  
# Authentication 
consumer_key ='XXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
  
# Authorization to consumer key and consumer secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# Access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret) 
  
# Calling api 
api = tweepy.API(auth) 
  
# Fetching tweets 
tweets = api.search('#Python', lang ="en", count = 10, tweet_mode = 'extended') 
  
# Showing the tweets 
for tweet in tweets: 
    print("\n\n", tweet.full_text)
