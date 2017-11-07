import json
import sys
import requests
import jwt
from enum import Enum

LOGIN_URL = "https://sso.teradatacloud.io/oauth/ro"

""" Helper functions are goes here """


class RequestType(Enum):
    """ Enumeration for the Request Types """
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'


class SystemType(Enum):
    """ Enumerations for the type of the system """
    source = 'source'
    target = 'target'


class RestAPIHeader(object):
    """ The helper class for api calling """

    def __init__(self, utype='valid'):
        self.response = None
        self.id_token = None
        if utype == 'valid':
            self.id_token, self.customerId = self.generate_token()
        if utype == 'invalid':
            self.id_token, self.customerId = self.generate_invalid_token()
        self.id_token = "Bearer " + self.id_token

    def generate_token(self):
        """ Generation of token """

        data = {
            "client_id": "h4psC1NTevUPYCJ6hTa76htrup4UNIyq",
            "username": "customer.one",
            "password": "pass@word1",
            "connection": "AD-DEV",
            "grant_type": "password",
            "scope": "openid profile roles customerId userId serviceNowUserId"
        }
        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(LOGIN_URL, data=json.dumps(data),
                                 headers=header)
        encode = str(response.json()['id_token'])
        decode = jwt.decode(encode, 'secret', algorithm=['RS256'], verify=False)
        customerId = (decode['customerId'])
        return str(response.json()['id_token']), customerId
        # else:
        #     print "login failure"
        #     sys.exit(1)

    def generate_invalid_token(self):
        """ Function to generate invalid token """
        token_url, customerId = self.generate_token()
        jwt_dict = jwt.decode(token_url, verify=False)
        jwt_dict['customerId'] = customerId + '234'
        customerId = customerId + '234'
        token_url = jwt.encode(jwt_dict, 'secret', algorithm='HS256')
        return token_url, customerId

    def request(self, method=None, url=None, payload=None):
        """ Do the actual request with validation """
        header = {
            'authorization': self.id_token,
            'content-type': "application/json"
        }

        if method == RequestType.GET:
            try:
                self.response = requests.get(url, headers=header, timeout=10)
            except:
                raise

        elif method == RequestType.POST:
            header['Content-Type'] = "application/json"
            try:
                self.response = requests.post(url, headers=header, timeout=10,
                                              data=json.dumps(payload))
            except:
                raise

        elif method == RequestType.PUT:
            header['content-type'] = "application/json"
            try:
                self.response = requests.put(url, headers=header, timeout=10,
                                             data=json.dumps(payload))
            except:
                raise

        elif method == RequestType.DELETE:
            try:
                self.response = requests.delete(url, headers=header, timeout=10)
            except:
                raise

        elif method == RequestType.PATCH:
            try:
                self.response = requests.patch(url, headers=header, timeout=10,
                                               data=json.dumps(payload))
            except:
                raise

        return self.response

if __name__ == '__main__':
    api = RestAPIHeader()
    api.generate_token()
