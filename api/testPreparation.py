import configparser
from api.APIRequests import APIRequests

class TestData:
    def __init__(self, config_file='config.ini'):
        # Parse the configuration
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        self.base_url = self.config['DEFAULT']['base_url']

        # Initialize our APIRequests with the base_url
        self.api_requests = APIRequests(self.base_url)
