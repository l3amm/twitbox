"""The application's Globals object"""

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self, config):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.DROPBOX_APP_KEY = "jtnr5188cxxn120"
        self.DROPBOX_APP_SECRET = "yz9rwnfkby86geu"
        self.TEMP_KEY = 'l7t4ujaqntowwff'
        self.TEMP_SECRET = 'cq29txoi4pkt3r3'
        self.cache = CacheManager(**parse_cache_config_options(config))
