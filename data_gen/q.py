#import twitter
import simplejson, sys, requests
from requests_oauthlib import OAuth1
#from textblob import TextBlob
import Quandl

with open("secrets/twitter_secrets.json.nogit") as fh:
      secrets = simplejson.loads(fh.read())

auth = OAuth1(
    secrets["api_key"],
    secrets["api_secret"],
    secrets["access_token"],
    secrets["access_token_secret"]
) 
r_stream = requests.post('https://stream.twitter.com/1.1/statuses/filter.json', auth=auth,
                          stream=True, data={"locations" : "-125,23,-70,50"} )
count=0
for line in r_stream.iter_lines():
    # filter out keep-alive new lines
    if not line:
        continue
    tweet = simplejson.loads(line)
    if 'text' in tweet and 'geo' in tweet:
        print "{{",tweet['geo'],"|||", tweet['created_at'],"|||", tweet['text'].encode('utf-8'),"}}"
    sys.stdout.flush()
    count+=1
    if count >500000:
	 break
    
