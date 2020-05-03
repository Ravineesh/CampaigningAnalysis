import tweepy
import datetime
import csv
import pandas as pd
import time


#Tweepy supports both OAuth 1a (application-user) and OAuth 2 (application-only) authentication. 
# Authentication is handled by the tweepy.AuthHandler class.


#Creating an OAuthHandler instance. Into this we pass our consumer key and secret
auth = tweepy.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)


#The API class is used to provide access to entire twitter RESTFul API methods 
api = tweepy.API(auth)


#For searching a User:-
user=""

#Search tweets between the date
startDate = datetime.datetime(2008, 1, 1, 0, 0, 0)
endDate =   datetime.datetime(2020, 4, 15, 0, 0, 0)

user_name=[]
user_id=[]
user_screen_name=[]
source = []
language = []
tweet_text = []
tweet_creation_date = []
retweets_count = []
like_count = []
hashtag = []
user_mention = []

# for tweet in tweets:
tweets = tweepy.Cursor(api.user_timeline,id=user,tweet_mode='extended').items(1500)
# i=1
temp1=0
temp2=0
k=0
hashtag_str = ""
user_mention_str = ""
for tweet in tweets:
    k = k+1
    i=0
    j=0
    hashtag_str=""
    user_mention_str=""

    if((tweet.created_at > startDate) & (tweet.created_at < endDate)):
        user_name.append(tweet.user.name)
        user_id.append(tweet.user.id_str)
        source.append(tweet._json["source"])
        user_screen_name.append(tweet.user.screen_name)
        language.append(tweet._json["lang"])
        tweet_text.append(tweet.full_text)
        retweets_count.append(tweet._json["retweet_count"])
        like_count.append(tweet._json["favorite_count"])
        tweet_creation_date.append(tweet.created_at)
        
        if(len(tweet._json["entities"]["hashtags"])>0):
            temp1 = len(tweet._json["entities"]["hashtags"])
            for i in range(0,temp1):
                hashtag_str = hashtag_str + tweet._json["entities"]["hashtags"][i]['text']
                hashtag_str = hashtag_str+","
            
            hashtag.append(hashtag_str)
        else:
            hashtag.append("#none")
        

        
        if(len(tweet._json["entities"]["user_mentions"])>0):
            temp2 = len(tweet._json["entities"]["user_mentions"])
            for j in range(0,temp2):
                temp2 = len(tweet._json["entities"]["user_mentions"])
                user_mention_str = user_mention_str +  tweet._json["entities"]["user_mentions"][j]['screen_name']
                user_mention_str = user_mention_str + ","
            
            user_mention.append(user_mention_str)
        
        else:
            user_mention.append("#none")
            
    

print("Tweet Fetched:-", k)

df = pd.DataFrame(columns={'User_Name','User_Screen_Name','Source','User_ID','Lang','Tweet','Tweet_Date','Retweet_Count',
                           'Like_Count','Hashtag','User_Mention'})


df.User_Name = user_name
df.User_Screen_Name= user_screen_name 
df.User_ID = user_id
df.Source = source
df.Lang = language
df.Tweet = tweet_text
df.Tweet_Date = tweet_creation_date
df.Retweet_Count = retweets_count
df.Like_Count = like_count
df.Hashtag = hashtag
df.User_Mention = user_mention

df.to_csv(r'user_tweet.csv', index = False, header=True)
