#!/usr/bin/python3
""" A Function to return the first 10 posts for a given subreddit """
import requests


def top_ten(subreddit):
    """Returns the top ten posts for a subreddit"""

    add = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    p = {'sort': 'new', 'limit': 10}
    h = {'User-Agent': 'My_ALX_API_Client'}

    dt = requests.get(add, headers=h, params=p, allow_redirects=False)
    if dt.status_code == 200:
        alldata = dt.json()['data']['children']
        for i in range(len(alldata)):
            print((alldata[i]['data']['title']))
    else:
        print("None")
