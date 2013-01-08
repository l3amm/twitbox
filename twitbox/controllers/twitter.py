import logging
import tweepy
import requests
import re
import twitbox.lib.helpers as h
import twitbox.lib.parser as parser

from pylons import request, response, session, tmpl_context as c, url
from pylons import app_globals
from pylons.controllers.util import abort, redirect

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
        tparse = parser.TwitterParser()
        for tweet in tweets:
            m = re.search("http.([A-Za-z0-9\/\.]+)", tweet.text)
            if m:
                r = requests.get(m.group(0))
                tparse.parse(r.url, r.text)
            resp += tweet.text
            resp += "\n"
        # resp = urllib2.urlopen('http://instagr.am/p/UIcpAETN73/')
        # html = resp.read()
        
        
        return render("/view.html", extra_vars={'tweets': tweets})
