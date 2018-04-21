# This code collects message information from yahoo groups.
# If group is private use  cookie settings at about  lines 12-13.

import pandas as pd
from pandas import Series, DataFrame
from bs4 import BeautifulSoup
import requests
import json
import datetime
import time

# Cookies stored here. FireFox cookie manager can retireve these.
cookie_T = 'z=Op.1aBO9l6aBFfljx.zrGOQNDA3MQY2NjYwNDAwNDY3&a=YAE&sk=DAACxYWaehFv0R&ks=EAASU447lh02MkU1HxDoKFH8A--~G&kt=EAAUtB0_6Mel3q8vK6Nu0qZ0A--~I&ku=FAAG3xuQVmRzp6jLgLmJ6gBDR4__SFxiarOmQq.5j9urVIZfkBUmF9aJMTB2lcTeeOQZUF4KbPczloF7NtDaggS7gxzWfTB35wLLmSUBPALvWvI3ZKEq.3h7SudUomPEz2d5JC6ImcIj7OMNyaAaqoRsBKLaHxEFc2VqjS3yqBdr4g-~A&d=bnMBeWFob28BZwFLTUxDNVo0VVQzRk00WE1UWk1EQlBSNkhUWQFzbAFNemN3TmdFeE1URTNNemMzTXpFdwFhAVlBRQFhYwFBTnk2SUU1WQFvawFaVzAtAWNzAQFhbAFhZGFtcm9zc25lbHNvbgFzYwFkZXNrdG9wX3dlYgFmcwFleUZpZmtCYTEucE8BenoBT3AuMWFCQTdF&af=JnRzPTE1MjQwOTk2NjImcHM9bDBfbjhXX21ZcXFfYU1BdGxBanhrZy0t'
cookie_Y = 'v=1&n=6j7iukl0k318i&l=38h42jehd4bied/o&p=m2g1ke500000000&jb=24|68|null&r=b2&lg=en-US&intl=us'

# for i in range(32811,242,-1):
# for i in range(32781,242,-1):
# for i in range(32681,242,-1):
# for i in range(32658,242,-1):
# for i in range(32513,242,-1):
# for i in range(32171,242,-1):
# for i in range(25443,242,-1):
# for i in range(22888,0,-1):
# for i in range(22451,0,-1):
# for i in range(22100,0,-1):
# for i in range(18290,0,-1):
# for i in range(18021,0,-1):
# for i in range(16478,0,-1):
# for i in range(16148,0,-1):
# for i in range(15129,0,-1):
# for i in range(15109,0,-1):
# for i in range(14902,0,-1):
# for i in range(14582,0,-1):
# for i in range(14339,0,-1):
# for i in range(13402,0,-1):
# for i in range(11833,0,-1):
# for i in range(11769,0,-1):
# for i in range(10865,0,-1):
# for i in range(9791,0,-1):
# for i in range(9296,0,-1):
# for i in range(8257,0,-1):
# for i in range(6338,0,-1):
# for i in range(6307,0,-1):
# for i in range(5847,0,-1):
for i in range(3544,0,-1):
    print('Working on message {}. Going backwards from 32811.'.format(str(i)))
    post = requests.get(
        ''.join((r'https://groups.yahoo.com/api/v1/groups/studentjudicial/messages/', str(i), r'/')),
         cookies={'T': cookie_T, 'Y': cookie_Y})
    
    post_parsed = json.loads(post.text)
    
    try:
        soup = BeautifulSoup(post_parsed['ygData']['messageBody'], 'html.parser')
        soupstring = soup.get_text()
        # pullstring = soupstring[soupstring.find('<!--'):soupstring.find('-->')+3]
        # cleanstring = soupstring.replace(pullstring,'')
        post_file = open(r'msgs\asca_' + str(i) + r'_post.txt', 'w', encoding='utf-8')
        # post_file.write(cleanstring)
        post_file.write(soupstring)
        post_file.close()
        
        json_file = open(r'msgs\asca_' + str(i) + r'_json.json', 'w', encoding='utf-8')
        json_file.write(post.text)
        json_file.close()
    except KeyError:
        print('There is no message number {}. MOVING along to the next message'.format(str(i)))
    
