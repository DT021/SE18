import re
import requests
import json
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    # referenced: https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'JCnuzlUj7lPaGBOhdKX8l4OgX'
        consumer_secret = 'G2fxz9nUlRqpcjceXZDixPpUBV3RLjUssuwahx0E84KvSTqc5o'

        access_token = '37085096-IiPrmWSA62H8VdFpNoMhtTMYwHjPqfK8nYdauMg4N'
        access_token_secret = 'kGN557CaH0QSH39zHk4lhKcUIvLC6WJTB2FxW6enxkWBA'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


def get_news_sentiment(description):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(description)
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def getTwitterSentiments(ticker):
    dticker = '$' + ticker
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = ticker, count = 200)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    ##print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    ##print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
    # percentage of neutral tweets
    ##print("Neutral tweets percentage: {} %".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))

    ##print("Total Number of Tweets: {}".format(len(tweets)))
    if len(tweets) == 0:
        return 0, 0, 0, 0, ['None', 'None', 'None', 'None', 'None'], ['None', 'None', 'None', 'None', 'None']
    posPercent = len(ptweets)/len(tweets)
    negPercent = len(ntweets)/len(tweets)
    neutPercent = 1 - posPercent - negPercent

    return posPercent, negPercent, neutPercent, len(tweets), ptweets, ntweets


def getNewsSentiments(ticker):


    # Authentication
    APIkey = 'b33b392f1f39444eb2821e5134c156ee'

    url = ('https://newsapi.org/v2/everything?'
		'apiKey=' + APIkey +
		'&q=' + ticker+
		'&language=en')

    response = requests.get(url)
    binary = response.content
    jsonData = json.loads(binary) #gets JSON data

    # Check if any errors, return -1
    if ('Error Message' in jsonData):
        return -1

    totalResults = jsonData['totalResults']

    if (totalResults == 0):
        return -1


    pageSize = 100;
    numPages = min(100,int(totalResults/pageSize))
    allArticles = []

    for i in range(1,numPages):
        url = ('https://newsapi.org/v2/everything?'
			'apiKey=' + APIkey +
			'&q=' + ticker+
			'&language=en'+
			'&pageSize='+str(pageSize)+
			'&page='+str(i))
        for a in jsonData['articles']:
            allArticles.append(a)

    arts = []
    numAll = len(allArticles)
    for a in allArticles:
        parsedArts = {}
        if not a['description']:
            continue
        parsedArts['description'] = a['description']
        parsedArts['title'] = a['title']
        parsedArts['url'] = a['url']
        parsedArts['sentiment'] = get_news_sentiment(parsedArts['description'])
        arts.append(parsedArts)


    pnews = [a for a in arts if a['sentiment'] == 'positive']
    nnews = [a for a in arts if a['sentiment'] == 'negative']
    if numAll == 0:
        return 0, 0, 0, 0, ['None', 'None', 'None', 'None', 'None'], ['None', 'None', 'None', 'None', 'None']
    perPos = len(pnews)/numAll
    perNeg = len(nnews)/numAll
    perNeut = 1 - perPos - perNeg

    return perPos, perNeg, perNeut, numAll, pnews, nnews

#print(getNewsSentiments('Google'))
