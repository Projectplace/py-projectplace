from requests_oauthlib import OAuth2Session

BASE_URL = 'https://service.projectplace.com/'
AUTHORIZE_URL = BASE_URL + 'oauth2/authorize'
TOKEN_URL = BASE_URL + 'oauth2/access_token'

API_URL = 'https://api.projectplace.com/'


class PPClient(OAuth2Session):
    """ Base class for Projectplace API oauth2 access """

    def authorization_url(self):
        """ Override and set authorize url """
        return super(PPClient, self).authorization_url(AUTHORIZE_URL)

    def fetch_token(self, client_secret, authorization_response):
        """ Override and set access_token url """
        return super(PPClient, self).fetch_token(TOKEN_URL,
                                                 client_secret=client_secret,
                                                 authorization_response=authorization_response)

    def get(self, path):
        """ Allows for sending path instead of full url """
        if path[0:4] != 'http':
            path = API_URL + path

        return super(PPClient, self).get(path)
