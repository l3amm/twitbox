from bs4 import BeautifulSoup
from pylons import app_globals
from pytube import YouTube
import urllib
import random
import re
import glob
import os

from dropbox import client, rest, session

class TwitterParser():
    
    ACCESS_KEY = 'l7t4ujaqntowwff'
    ACCESS_SECRET = 'cq29txoi4pkt3r3'
    ACCESS_TYPE = 'app_folder'
    
    def __init__(self):
        # grab keys from the user database, in the meantime use above
        self.DROPBOX_APP_KEY = app_globals.DROPBOX_APP_KEY
        self.DROPBOX_APP_SECRET = app_globals.DROPBOX_APP_SECRET
        self.sess = session.DropboxSession(
            self.DROPBOX_APP_KEY, 
            self.DROPBOX_APP_SECRET, 
            self.ACCESS_TYPE
        )
        self.sess.set_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        self.drop_client = client.DropboxClient(self.sess)
    
    def instagram_parser(self, html):
        soup = BeautifulSoup(html)
        for img in soup.find_all('img', class_='photo'):
            resp = urllib.urlretrieve(img['src'])
            f = open(resp[0])
            self.drop_client.put_file(str(random.randint(1,100))+'.jpeg', f)
    
    def youtube_parser(self, url):
        yt = YouTube()
        yt.url = url
        yt.videos[0].download('/tmp/')
        f = open(glob.glob('/tmp/'+yt.filename+'*')[0])
        self.drop_client.put_file(os.path.basename(f.name), f)
    
    def parse(self, url, content):
        if re.search('instagram', url):
            self.instagram_parser(content)
        elif re.search('youtube', url):
            self.youtube_parser(url)
        else:
            print " nothing to see here"
        