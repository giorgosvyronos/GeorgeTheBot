import os
import sys
import random
import json
import logging
from pathlib import Path
from tkinter import N
import tweepy
import random
import csv
from random_word import RandomWords
from quote import quote as Quote
import requests

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

def get_tweet(tweets_file= ROOT / "tweets.csv", excluded_tweets=None):
    """Get tweet to post from CSV file"""
    tweets = get_tweet_list(tweets_file)

    if excluded_tweets:
        recent_tweets = [status_object.text for status_object in excluded_tweets]
    else:
        recent_tweets = []
    possible_tweets = [tweet for tweet in tweets if tweet not in recent_tweets]

    selected_tweet = random.choice(possible_tweets)
    return selected_tweet

def get_quote(recent_tweets=[]):
    """Get Quote to post from Quote, RandomWords Libraries"""
    response = requests.get("http://randommovielines.herokuapp.com/api/v1.0/randomlines")
    quote = response.json()["line"]
    # [{'author': 'William Shakespeare',
    # 'book': 'As You Like It',
    # 'quote': 'The fool doth think he is wise..}]
    char_size = len(f"\Someone Somewhere Once Said:\n\n\t{quote}\n\n\t#GeorgeTheBot")-280
    if char_size > 0:
        quote = (quote)[:(len(quote)-(char_size+10))] + "..."
    possible_tweet = f"Someone Somewhere once said:\n\n\t{quote}\n\n\t#GeorgeTheBot"

    return possible_tweet
    
   

def lambda_handler(event, context):
    logging.info("Get credentials")

    consumer_key = os.getenv('CONSUMER_KEY_DEV')
    consumer_secret = os.getenv('CONSUMER_SECRET_DEV')
    access_token = os.getenv('ACCESS_TOKEN_DEV')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET_DEV')

    logging.info("Authenticate")
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    logging.info("Get tweet form csv file")
    recent_tweets = api.user_timeline()[:3]
    tweet = get_quote(recent_tweets)

    logging.info(f"Post tweet: {tweet}")
    api.update_status(tweet)

    return {"statusCode" : 200, "tweet" : tweet}

logging.info(get_quote())