import requests
import simplejson as json

# Calls the meetup api and sets a variable to the json value and returns it.
def get_events():
    url = 'https://api.meetup.com/2/concierge'
    params = {'zip': 32801,
                'offset': 0,
                'city': 'Orlando',
                'format': 'json',
                'category_id': 34,
                'photo-host' : 'public',
                'page': 500,
                'radius': 30,
                'sig_id': 184859886,
                'sig': '83442ad767f8be2fd2b2c7225e723d07f1527f5a'
                }
    r = requests.get(url, params=params)
    events = r.json()
    return events

# https://api.meetup.com/2/concierge?zip=32801&offset=0&city=Orlando&format=json&category_id=34&photo-host=public&page=500&radius=30&sig_id=184859886&sig=83442ad767f8be2fd2b2c7225e723d07f1527f5a

