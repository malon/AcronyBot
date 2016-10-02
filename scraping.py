#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter AcronyBot
# This script scraps the list of acronyms from
# http://www.netlingo.com/acronyms.php
# shuffle them and store them in a file


import requests
from bs4 import BeautifulSoup
import sys
from random import shuffle


result = requests.get("http://www.netlingo.com/acronyms.php")

if result.status_code != 200:
	sys.exit("Error accessing the url. Scraping aborted!!")
else:
	soup = BeautifulSoup(result.content, "html.parser")
	table = soup.find("div","list_box3")
	table_list = []
	for i,line in enumerate(table.find_all("li")):
		link = line.a["href"] # it is not used right now
		acr = line.a.string
		desc = line.contents[1]
		table_list.append(("%d: %s - %s\n" % (i, acr, desc)).encode('utf8'))
	acr_list = table_list[65:] # numeric acronyms are discarded right now
	shuffle(acr_list)

	with open('acronyms.txt', 'w') as f:
		f.writelines(acr_list)
		

