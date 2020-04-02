import tweepy

#Tweepy supports both OAuth 1a (application-user) and OAuth 2 (application-only) authentication. 
# Authentication is handled by the tweepy.AuthHandler class.


#Consumer API keys:- (These are the API Keys which are provided in your Twitter Developer account under Keys and Token Section)
#API key
#API secret key

#Access token & access token secret ( These will also be provided in your Twitter Developer account under Keys and Token Section)
#access_token
#access_token_secret

#Creating an OAuthHandler instance. Into this we pass our api key and and api secret key
auth = tweepy.OAuthHandler(API_key, API_secret_key)

#Setting the access token provided by the Twitter
auth.set_access_token(access_token, access_token_secret)



#The API class is used to provide access to entire twitter RESTFul API methods 
api = tweepy.API(auth)
print(api.me())
