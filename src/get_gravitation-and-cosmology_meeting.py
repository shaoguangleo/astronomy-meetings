#!/usr/bin/env python
# coding=utf-8
#
###############################################################################
# Copyright (C) 2010 - 2019
# Division of Radio Astronomy Science and Technology
# SHAO (Shanghai Astronomical Observatory) <http://www.shao.ac.cn>
# CAS (Chinese Academy of Sciences)
# Postal adress: 80# Nandan Road , Xuhui District, Shanghai, 200030 P. R. China
###############################################################################
#
#-------------------------------------------------------------------------------
# File Name   :   get_gravitation-and-cosmology_meeting.py
# Purpose     :
#
# Author      :   Shaoguang Guo (SHAO)
# Email       :   sgguo@shao.ac.cn
# Created     :   2019-02-10 15:59:58
#-------------------------------------------------------------------------------
#

import requests
from bs4 import BeautifulSoup

url = 'https://www.conference-service.com/conferences/gravitation-and-cosmology.html'

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'html.parser')

# find all the sub_titles
sub_titles = soup.find_all('div',class_='sub_title')


titles = []
for i in sub_titles:
	titles.append(str(i).split('conflist_title">')[-1].split('<')[0])

dates_locs = []
# find all the dates and location
dates_locations = soup.find_all('div',class_='dates_location')
for i in dates_locations:
	dates_locs.append(str(i).split('conflist_value">')[-1].split('<')[0])


# find all the websites
website = soup.find_all('a',class_='external_link')

websites = []

for i in website:
	websites.append(str(i).split('href="')[-1].split('"')[0])

dates = []
locs = []

for i in dates_locs:
	#tmp = i.split('â\x80¢')
	tmp = i.split('\xc3\xa2\xc2\x80\xc2\xa2')
	#print(tmp)
	dates.append(tmp[0])
	locs.append(tmp[1])

dates_start = []
dates_end = []

for i in dates:
	tmp_date = i.split('-')
	dates_start.append(tmp_date[0])
	if (len(tmp_date) > 1):
		dates_end.append(tmp_date[1])
	else:
		dates_end.append(' ')

for i,v in enumerate(titles):
	print(('|{start}| {end} | {title} | {loc} | {website} |').format(start=dates_start[i],end=dates_end[i],loc=locs[i],title=titles[i],website=websites[i]))
