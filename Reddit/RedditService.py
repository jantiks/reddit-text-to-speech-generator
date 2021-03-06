from . import RedditUtils as utils
import praw

reddit = ""


def startSession():
    global reddit
    reddit = praw.Reddit(
        client_id=utils.appID,
        client_secret=utils.secretKey,
        user_agent='MyBot/0.0.1',
        username=utils.username,
        password=utils.password,
    )


def getHotSubmissions(limit):
    subreddit = reddit.subreddit("askReddit")

    return subreddit.hot(limit=limit)
