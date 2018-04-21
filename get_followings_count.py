# twripbot - GPL - Copyright 2018 - abx1
from twython import Twython
import utils

def get_followings_count(twitter, username):
	followings_count = twitter.show_user(screen_name=username)
        print followings_count['friends_count']

if __name__ == '__main__':
	try:
		twitter = utils.connect()
	except Exception as e:
		print e
	
	try:
		get_followings_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e