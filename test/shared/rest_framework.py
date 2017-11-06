import json
import requests
import jwt

""" Helper functions are goes here """
from enum import Enum


class RequestType(Enum):
    """ Enumeration for the Request Types """
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'
    PATCH = 'PATCH'


class RestAPIHeader(object):
    """ The helper class for api calling """

    def __init__(self, utype='user'):
        self.response = None
        if utype == 'user':
            self.token, self.cust_id = self.generate_user_token()
        if utype == 'admin':
            self.token, self.cust = self.generate_admin_token()
        if utype == 'agent':
            self.token, self.cust_id = self.generate_agent_token()
        if utype == 'un user':
            self.token, self.cust_id = self.generate_invalid_token()
        self.token = "Bearer " + str(self.token)

    def generate_user_token(self):
        """ Generation of user_token """
        user = "customer.one"
        password = "pass@word1"
        user_url = \
            "https://k0zvnnx44k.execute-api.us-west-2.amazonaws.com/" \
            "dev/auth/login/user"
        data = {"username": user, "password": password}
        response = requests.post(user_url, data=json.dumps(data))
        return response.json()['token'], response.json()['customer_id']

    def generate_admin_token(self):
        """ Generation of admin_token """
        admin_user = "sys.ops"
        admin_password = "pass@word1"
        admin_url = \
            "https://g3micih5t0.execute-api.us-west-2.amazonaws.com/" \
            "im186014dev/auth/login/user"
        data = {"username": admin_user, "password": admin_password}
        response = requests.post(admin_url, data=json.dumps(data))
        return response.json()['token'], response.json()

    def generate_agent_token(self):
        """ Generation of agent_token """

        agent_user = "7d4dff18-fb0b-4be4-aeb0-a6e2c015cb99"
        agent_password = "B7C76twh"
        agent_url = \
            "https://k0zvnnx44k.execute-api.us-west-2.amazonaws.com/dev/" \
            "auth/login/agent"
        data = {"username": agent_user, "password": agent_password}
        response = requests.post(agent_url, data=json.dumps(data))
        return response.json()['token'], response.json()['customer_id']

    def generate_invalid_token(self):
        """ Function to generate invalid token """
        token_url, cust_id = self.generate_user_token()
        jwt_dict = jwt.decode(token_url, verify=False)
        jwt_dict['customer_id'] = '1' + cust_id + '234'
        cust_id = '1' + cust_id + '234'
        token_url = jwt.encode(jwt_dict, 'secret', algorithm='HS256')
        return token_url, cust_id

    def generate_token_for_invalid_customer(self):
        """ Function to generate token for invalid customer """
        user = "jeyanthi@teradata.com"
        pwd = "jeyanthi@123"
        url = \
            'https://g3micih5t0.execute-api.us-west-2.amazonaws.com/' \
            'im186014dev/auth/login/user'
        data = {"username": user, "password": pwd}
        response = requests.post(url, data=json.dumps(data))
        return response.json()['token'], response.json()

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
