from bs4 import BeautifulSoup
from pylons import app_globals

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
            print img['src']
            
    def test(self):
        files = self.drop_client.metadata("/")["contents"]
        media = []
        for f in files:
            media.append(self.drop_client.media(f['path'])['url'])
            
        return media
            