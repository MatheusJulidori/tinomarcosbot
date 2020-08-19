import tweepy
import time
import string
import random

auth = tweepy.OAuthHandler('pKYmoZFJiXjMKncQvVgpJa4YU','r0Dste6fKiHQEICZEU6jI3GC12bCdZUVxAa5QDfKGoT9d0Ex5T')
auth.set_access_token('4703295517-3YyiYYNhnJqcp25kXfdhY6CsKODvB6UwP2QuEQ7','GtzIRkE2S3YVmqjcMWA7EzBbcWsL1AnDjpEjS5Y9NJnCn')
beerer = 'AAAAAAAAAAAAAAAAAAAAACwdGQEAAAAAQjLhQ6JBdfIwXcExZ2ZDpRRmOrY%3DafDw6II4JZZFRgFe9tZxjdrBjMdPTvSxXgvmB2Cff6pB5YNidu'
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
me = api.me()

msg_padrao = 'Diga lá, Tino!'

i = 0

galvao = api.get_user('1068588022688636934')
status = galvao.status
status_id = status.id
while i<10000:
    try:
        if msg_padrao in status.text :
            api.update_status('@botdogalvao Sentiu!',status_id)
            print('replied')
            i+=1
            time.sleep(60)
    except tweepy.TweepError as e:
        print(e.reason)
        time.sleep(60)