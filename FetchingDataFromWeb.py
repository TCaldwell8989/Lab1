import requests

import os

key = os.environ['omdb_key'] #1b1a8f2a
print (key)

base_url = 'http://www.omdbapi.com/'

movie = input('What Movie Name?')

params = { 'apikey' : key, 't' : movie }
data = requests.get(base_url, params).json()

# print(data)
print(data['Ratings'][0]['Value'])