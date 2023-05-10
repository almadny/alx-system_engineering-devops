#!/usr/bin/python3
""" A Function to return the count of subscriber for a given subreddit """
import requests
def number_of_subscribers(subreddit):
    """Returns the numbers of subscribers for the subreddit"""
    address = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    hder = {'User-Agent':'My_ALX_API_Client'}
    try:
        data = requests.get(address, headers=hder, allow_redirects=False)
        data = data.json()
        sub = data['data']['subscribers']
        return sub
    except:
        return 0
