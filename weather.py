from datetime import datetime
import os
import json
import pytz
import requests
import requests_toolbelt.adapters.appengine
from urllib.request import urlopen
 

# Use the App Engine Requests adapter. This makes sure that Requests uses
# URLFetch.
requests_toolbelt.adapters.appengine.monkeypatch()

import math
API_KEY = 'Z1----------------------7X'
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')
# When running local let us use our one-trick weather API stubserver
STUB_URL= ('http://localhost:8001')

def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        try:
            with urlopen(STUB_URL) as stuburl:
                data = json.loads(stuburl.read().decode('utf-8'))
                # Open the stub weather or else fail and show result without weather
        except Exception as exc:
            print(exc)
            data = None
 
    return data
