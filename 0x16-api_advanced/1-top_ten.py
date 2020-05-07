#!/usr/bin/python3
"""Top 10 hot posts of subreddit printed via API"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    r = requests.get(url, headers={'User-agent': 'it me'}).json()
    if 'message' in r and r['message'] == 'Not Found':
        print("None")
        return
    for i in r['data']['children']:
        print(i['data']['title'])
