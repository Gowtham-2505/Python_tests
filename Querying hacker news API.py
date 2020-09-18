import json
import urllib.request as request

with request.urlopen('https://hacker-news.firebaseio.com/v0/item/<id>.json'.replace('<id>', input())) as response:
    source = response.read()
    data = json.loads(source)
print(data['title'])
