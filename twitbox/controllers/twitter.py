import logging
import tweepy
import requests
import re
import twitbox.lib.helpers as h

from pylons import request, response, session, tmpl_context as c, url
from pylons import app_globals
from pylons.controllers.util import abort, redirect
from twitbox.lib.parser import TwitterParser

from twitbox.lib.base import BaseController, render

log = logging.getLogger(__name__)

class TwitterController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/twitter.mako')
        # or, return a string
        return 'Hello World'

    def view(self, id):
        if id:
            tweets = tweepy.api.user_timeline(id)
        else:
            abort(404)
        resp = ''
        parser = TwitterParser()
        for tweet in tweets:
<<<<<<< HEAD
            m = re.search('http.*(\s+|$)', tweet.text)
            if m:
                r = requests.get(m.group(0))
                print r.text
                
=======
            # m = re.search('http.*(\s+|$)', tweet.text)
            # if m:
            #     response = urllib2.urlopen(m.group(0))
            #     html = response.read()
>>>>>>> a782ec2e414d3c1ae61ad560baf3861eacb89a01
                
            resp += tweet.text
            resp += "\n"
        # resp = urllib2.urlopen('http://instagr.am/p/UIcpAETN73/')
        # html = resp.read()
        
        return render("/view.html", extra_vars={'tweets': tweets})
