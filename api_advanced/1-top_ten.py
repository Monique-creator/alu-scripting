#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first 10 hot posts
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Fetches the top 10 hot posts for a subreddit.
    If the subreddit is invalid, prints None.
    """
    # Define the URL for the subreddit's hot posts in JSON format
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    # Set a custom User-Agent to avoid being blocked by Reddit
    headers = {
        "User-Agent": "linux:0x01.top.ten:v1.0.0 (by /u/your_username)"
    }

    # Limit the results to 10 as per requirements
    params = {
        "limit": 10
    }

    try:
        # Request data without following redirects
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # If status code is 200 (OK), parse the JSON
        if response.status_code == 200:
            data = response.json().get("data")
            children = data.get("children")
            
            for post in children:
                print(post.get("data").get("title"))
        else:
            # If subreddit doesn't exist or is a redirect, print None
            print(None)
            
    except Exception:
        # Handle any connection errors gracefully
        print(None)
