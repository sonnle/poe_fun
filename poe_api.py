import json
import requests

def test_poe():
    url = 'http://www.pathofexile.com/api/public-stash-tabs?id='
    id = '100888182-105804434-99340529-114550086-107078097'

    r = requests.get(url+id)

    j = r.json()

    for i in range(len(j['stashes'])):
        print j['stashes'][i]['accountName']
        print len(j['stashes'][i]['items'])
        print ''


if __name__ == '__main__':
    test_poe()
