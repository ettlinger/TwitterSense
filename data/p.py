#import twitter
import simplejson, sys, requests
from requests_oauthlib import OAuth1
from textblob import TextBlob

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
    if ('text' in tweet) and ('geo' in tweet) and (str(tweet['geo']) != 'None'):
        stext = TextBlob(tweet["text"])
        tweettext=tweet['text'].encode('utf-8').replace('\n','')
        print tweet['geo'],"|", tweet['created_at'],"|", tweettext, "|", stext.sentiment[0]
#        print "{{",tweet['geo'],"|||", tweet['created_at'],"|||"
        count+=1
    sys.stdout.flush()
    if count >100000:
	 break
    
