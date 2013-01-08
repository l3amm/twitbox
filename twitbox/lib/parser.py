from bs4 import BeautifulSoup
from pylons import app_globals

class TwitterParser():
    
    ACCESS_KEY = '3wb901hul40n4ml'
    ACCESS_SECRET = 'ciovxthyqc2zxu2'
    ACCESS_TYPE = 'app_folder'
    
    def __init__(self):
        # grab keys from the user database, in the meantime use above
        print app_globals
        # self.DROPBOX_APP_KEY = app_globals['DROPBOX_APP_KEY']
        # self.DROPBOX_APP_SECRET = app_globals['DROPBOX_APP_SECRET']
        # self.sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
    
    def instagram_parser(self, html):
        soup = BeautifulSoup(html)
        for img in soup.find_all('img', class_='photo'):
            print img['src']