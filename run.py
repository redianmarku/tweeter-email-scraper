import tweepy
import re
import time


def twitte_auth():
    try:
        consumer_key = ""
        consumer_secret = ""
        access_token = ""
        access_secret = ""

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
    except:
        print('Cant login tweeter.')
    return auth


def get_client():
    auth = twitte_auth()
    client = tweepy.API(auth, wait_on_rate_limit=True)
    return client



client = get_client()
print('Logged In.')

KEY = str(input('[?] Put your email keyword:'))
DELAY = int(input('[?] How many time delay between each scrape:'))

textfile = open("emails.txt", "w")

for status in tweepy.Cursor(client.search, q=KEY, since="2021-05-01").items():
    try:
        match = re.search(r'[\w\.-]+@[\w\.-]+', status.text)
        email = match.group(0)
        print(email.lower())
    except:
        continue

    try:
        textfile.write(email.lower() + "\n")
    except:
        continue
    time.sleep(DELAY)
    
