import json
import requests
import jwt

""" Helper functions are goes here """
from enum import Enum

LOGIN_URL = "https://sso.teradatacloud.io/oauth/ro"


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
        if utype == 'valid':
            self.token, self.cust_id = self.generate_token()
        if utype == 'invalid':
            self.token, self.cust_id = self.generate_invalid_token()
        self.token = "Bearer " + str(self.token)


    def generate_token(self):
        """ Generation of agent_token """

        username = "customer.one"
        password = "pass@word1"
        agent_url = ""
        data = {"username": username, "password": password}
        response = requests.post(agent_url, data=json.dumps(data))
        return response.json()['token'], response.json()['customer_id']

    def generate_invalid_token(self):
        """ Function to generate invalid token """
        token_url, cust_id = self.generate_token()
        jwt_dict = jwt.decode(token_url, verify=False)
        jwt_dict['customer_id'] = '1' + cust_id + '234'
        cust_id = '1' + cust_id + '234'
        token_url = jwt.encode(jwt_dict, 'secret', algorithm='HS256')
        return token_url, cust_id

    def request(self, method=None, url=None, payload=None):
        """ Do the actual request with validation """
        header = {
            'authorization': self.token,
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
