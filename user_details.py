import tweepy

#Creating an OAuthHandler instance. Into this we pass our api key and and api secret key
auth = tweepy.OAuthHandler(API_key, API_secret_key)

#Setting the access token provided by the Twitter
auth.set_access_token(access_token, access_token_secret)

#The API class is used to provide access to entire twitter RESTFul API methods 
api = tweepy.API(auth)

#For searching a User:-

#for twitter handle of the user
user_name="" 

tweets = tweepy.Cursor(api.user_timeline,id=user_name).items(1)

for tweet in tweets:
    print("User Name:-", tweet.user.name)
    print("User Screen Name:-",tweet.user.screen_name)
    print("Followers:-",tweet.user.followers_count)
    print("Friends:-",tweet.user.friends_count)
    print("Twitter Joining Date:-",tweet.user.created_at)
    print("Location:-",tweet.user.location)
    print("Twitter Account Verified:-",tweet.user.verified)
