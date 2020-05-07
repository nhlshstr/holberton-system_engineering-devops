#!/usr/bin/python
""" Recursive | Returns hot titles for subreddit"""
import requests


def recurse(subreddit, hot_list=[], last=""):
    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'\
            .format(subreddit) +\
            ('&after={}'.format(last) if last != "" else "")
    r = requests.get(url, headers={'User-agent': 'NehalShastri'}).json()
    if 'message' in r and r['message'] == 'Not Found':
        return None
    hot_array = r['data']['children']

    if len(hot_array) == 0:
        return hot_list
    for i in range(0, len(hot_array)):
        hot_list.append(hot_array[i]["data"]["title"])
    return (recurse(subreddit, hot_list, hot_array[-1]["data"]["name"]))
