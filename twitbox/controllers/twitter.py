import logging
import tweepy
import urllib2
import re

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
        
        for tweet in tweets:
            m = re.search('http.*(\s+|$)', tweet.text)
            if m:
                response = urllib2.urlopen(m.group(0))
                html = response.read()
                
            resp += tweet.text
            resp += "\n"
        # resp = urllib2.urlopen('http://instagr.am/p/UIcpAETN73/')
        # html = resp.read()
        
        return resp