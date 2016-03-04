import requests
# import json
import simplejson as json
def get_events():
    url = 'https://api.meetup.com/activity'
    params = {'member_id': 184859886,
                'format': 'json',
                'photo-host': 'public',
                'sig_id': 184859886,
                'sig': '8a5c4ded3d246545acb6095533e37c44bc6dabe3'}
    r = requests.get(url, params=params)
    events = r.json()
    return events

