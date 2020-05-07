#!/usr/bin/python3
""" Returns total subs for subreddit """
import requests


def number_of_subscribers(subreddit):
    r = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={
            'User-agent': 'NehalShastri'
        }).json()
    return (0 if ('message' in r and
                  r['message'] == 'Not Found') else
            r['data']['subscribers'])
