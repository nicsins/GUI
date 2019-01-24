import json
import urllib
import requests

# open the url and the screen name
# (The screen name is the screen name of the user for whom to return results for)
url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=python"

# this takes a python object and dumps it to a string which is a JSON
# representation of that object
data = json.load(requests.get(url))

# print the result
print( data)