import json
from application_only_auth import Client

location = [38.557657, -121.708919]
# The consumer secret is an example and will not work for real requests
# To register an app visit https://dev.twitter.com/apps/new
CONSUMER_KEY = 'ZVUSsTWfsdqUhbG9IBBpsFTVA'
CONSUMER_SECRET = 'FQJql1iyMIVMMhtORLfxFSUNMgSNsBzueye1N9AATdFhM20D0d'
LAT, LONG = location[0],location[1]

client = Client(CONSUMER_KEY, CONSUMER_SECRET)

# Format search request string
#request_url = 'https://api.twitter.com/1.1/search/tweets.json?q=geocode={},{},1mi'.format(LAT,LONG)
request_url = 'https://api.twitter.com/1.1/search/tweets.json?q=geocode=38.557657,-121.708919,1mi'

tweet = client.request(request_url)
print(json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':')))
# print the number of tweets found
print(tweet["search_metadata"]["count"])

# Show rate limit status for this application
status = client.rate_limit_status()
print(status['resources']['search'])
