__doc__ = 'item crawler for https://rd.fharr.com'

import urllib2
import os
import time

# the base url, all the web pages are lead by this string
BASE_URL = 'https://rd.fharr.com/'

# this is the item number range
ITEM_MIN = 1
ITEM_MAX = 40000

# this is the saving folder
DEFAULT_PATH = os.getcwd()

def process():
    for item in range(ITEM_MIN, ITEM_MAX):
        print('Working on %s'%str(item))
        url = BASE_URL + 'item-%s.html'%str(item)
        response = urllib2.urlopen(url)
        s = response.read()
        saving_file = DEFAULT_PATH + '/fharr/%s.html'%str(item)
        with open(saving_file) as f:
            f.write(s)
        print('DONE')
        time.sleep(1)
    return None


