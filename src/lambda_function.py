import os
import sys
import random
import json
import logging
from pathlib import Path
import tweepy
import csv

logging.basicConfig(stream=sys.stdout, encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ROOT = Path(__file__).resolve().parents[0]

def get_tweet_list(file_path:str):
    """
    Method used to extract tweets from csv
    :arg = file_path (The path to csv containing tweets)
    :return = tweet_list (List[str] containing the list of tweets)
    """
    file = open(file_path, mode="r", encoding="utf-8-sig")
    csvreader = csv.reader(file)
    tweet_list = [tweet[0] for tweet in csvreader if tweet]
    file.close()
    return tweet_list

def get_tweet(tweets_file, excluded_tweets=None):
    """Get tweet to post from CSV file"""
    tweets = get_tweet_list(tweets_file)

    if excluded_tweets:
        recent_tweets = [status_object.text for status_object in excluded_tweets]
        possible_tweets = [tweet for tweet in possible_tweets if tweet not in recent_tweets]

    selected_tweet = random.choice(possible_tweets)
    return selected_tweet

def lambda_handler(event, context):
    logging.info("Get credentials")

    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCES_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    logging.info("Authenticate")
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    logging.info("Get tweet form csv file")
    tweets_file = ROOT / "tweets.csv"
    recent_tweets = api.user_timeline()[:3]
    tweet = get_tweet(tweet)

    logging.info(f"Post tweet: {tweet}")
    api.update_status(tweet)

    return {"statusCode" : 200, "tweet" : tweet}

    
logging.info(get_tweet_list("src/tweets.csv"))