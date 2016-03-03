import requests
import json
def get_events():
    url = 'https://api.meetup.com/self/events'
    params = {'photo-host': 'public', 'page': 1, 'sig_id': 184859886, 'sig': '8dcbb49f2f63c3df00a553fd3e479ec3a0f5f89d'}
    r = requests.get('https://api.meetup.com/self/events', params=params)
    events = r.json()
    events_list = {'events':events[0]}
    j = json.loads(events_list)
    print j

    print events_list
    return events_list
    #print events_list
    # https://api.meetup.com/self/events?photo-host=public&page=1&sig_id=184859886&sig=8dcbb49f2f63c3df00a553fd3e479ec3a0f5f89d
