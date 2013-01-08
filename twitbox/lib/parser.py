from HTMLParser import HTMLParser

class TwitterParser(HTMLParser):
    
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            print "!!!!!!!!!", tag, attrs
