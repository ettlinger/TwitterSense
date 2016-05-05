# TwitterSense

This is a capstone project for The Data Incubator.
Twitter Sense looks at millions of tweets from around the country and uses natural language processing to examine the positive and negative sentiment, or feeling, expressing in those tweets. The state and zipcode can be by extracted for each tweet using the latitutde and longitude from tweeters' cell phones. This allows us to look at the happiness of individual states and zipcodes in the US and compare it to things like income and population. Future applications including looking at how twitter sentiment changes as a function of changes in the stock market or the weather for different regions as well as keyword searches.

## Functionality
What twitter sense does is:
1) Use twitter's API to pull tweets from their live stream
1) Do natural language processing to determine the sentiment, positive or negative, of the tweets
1) Extract geographic location - state and zipcode - for the geotagged tweets using its longitude and lattitude
1) Aggregate via mean into state and zipcode which can be uploaded to cartodb
1) ...and uploaded into an iPython Notebook for generating a few graphs
