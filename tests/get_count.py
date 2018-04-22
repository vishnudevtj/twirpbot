# twripbot - GPL - Copyright 2018 - r00tus3r
from twirpbot import connect
from twirpbot import get_count_of_hashtags_per_user
from twirpbot import get_followers_count
from twirpbot import get_followings_count
from twirpbot import get_likes_count
from twirpbot import get_tweets_count

if __name__ == '__main__':
	try:
		twitter = connect()
	except Exception as e:
		print e
	try:
		print get_count_of_hashtags_per_user(twitter, 'aswinmguptha', 'nullcon')
	except Exception as e:
		print e
	try:
		print get_followers_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
	try:
		print get_followings_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
	try:
		print get_likes_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
	try:
		print get_tweets_count(twitter, 'aswinmguptha')
	except Exception as e:
		print e
