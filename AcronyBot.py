#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter AcronyBot
# http://www.netlingo.com/acronyms.php


import tweepy, time
from credentials import *
import fileinput
import sys


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# days between tweets
d = 1

while True:

	with open('acronyms.txt','r') as f:
		tweettext = f.readline()
		api.update_status(tweettext)
		if tweettext == "":
			break

	with open('tweeted.txt', 'a') as f:
		""" 
		I delete the final \n because I need in the beginning of the line,
		otherwise everytime I rerun the cursor for appending does not start with \n.
		"""
		f.write("\n"+tweettext.strip())

	for line_number, line in enumerate(fileinput.input('acronyms.txt', inplace=1)):
  		if line_number == 0:
			continue
		else:
			sys.stdout.write(line)

	time.sleep(86400 * d)
	# 86400 sec per day


