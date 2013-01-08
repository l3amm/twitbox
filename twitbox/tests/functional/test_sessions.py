from twitbox.tests import *

class TestSessionsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='sessions', action='index'))
        # Test response...
