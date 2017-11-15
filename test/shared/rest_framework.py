import os
import json
import sys
import requests
import jwt
from enum import Enum
import yaml
path = os.environ["PYTHONPATH"]
with open(path + "/env/configuration.yaml", 'r') as stream:
    try:
       config_data = yaml.load(stream)
    except yaml.YAMLError as exc:
        print("Cannot able to access input configuration")

LOGIN_URL = config_data['LOGIN_URL']
AGENT_LOGIN_URL = config_data['AGENT_URL']

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

    def __init__(self, utype='invalid'):
        self.response = None
        self.id_token = None
        if utype == 'customer':
            self.id_token, self.customerId = self.generate_customer_token()
        if utype == 'invalid':
            self.id_token, self.customerId = self.generate_invalid_token()
        if utype == 'sysops':
            self.id_token, self.customerId = self.generate_sysops_token()
        if utype == 'agent':
            self.id_token, self.customerId = self.generate_agent_token()
        self.id_token = "Bearer " + self.id_token

    def generate_sysops_token(self):
        data = {
            "client_id": config_data['client_id'],
            "username": config_data['sysops_username'],
            "password": config_data['sysops_password'],
            "connection": config_data['connection'],
            "grant_type": config_data['grant_type'],
            "scope": config_data['scope']
        }

        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(LOGIN_URL, data=json.dumps(data),
                                 headers=header)
        try:
            encode = str(response.json()['id_token'])
        except:
            print "response is " + response.text
            print "Cannot able to parse the token in Login"
            sys.exit(1)
        return str(response.json()['id_token']), response.json()

    def generate_agent_token(self):
        """ Generation of agent_token """

        agent_user = config_data['agent_username']
        agent_password = config_data['agent_password']
        data = {"username": agent_user, "password": agent_password}
        response = requests.post(AGENT_LOGIN_URL, data=json.dumps(data))
        return response.json()['token'], response.json()['customer_id']

    def generate_customer_token(self):
        """ Generation of token """

        data = {
            "client_id": config_data['client_id'],
            "username": config_data['customer_username'],
            "password": config_data['customer_password'],
            "connection": config_data['connection'],
            "grant_type": config_data['grant_type'],
            "scope": config_data['scope']
        }

        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(LOGIN_URL, data=json.dumps(data),
                                 headers=header)
        try:
            encode = str(response.json()['id_token'])
        except:
            print "response is " + response.text
            print "Cannot able to parse the token in Login"
            sys.exit(1)
        decode = jwt.decode(encode, 'secret', algorithm=['RS256'], verify=False)
        customerId = (decode['customerId'])
        # print "response.json()['id_token']", response.json()['id_token']
        print (customerId)
        return str(response.json()['id_token']), customerId

    def generate_invalid_token(self):
        """ Function to generate invalid token """
        token_url, customerId = self.generate_customer_token()
        jwt_dict = jwt.decode(token_url, verify=False)
        jwt_dict['customerId'] = customerId + '234'
        customer_id = customerId + '234'
        token_url = jwt.encode(jwt_dict, 'secret', algorithm='HS256')
        print (token_url, customerId)
        print (customer_id)
        return token_url, customerId

    def request(self, method=None, url=None, payload=None):
        """ Do the actual request with validation """
        header = {
            'authorization': self.id_token,
            'content-type': "application/json"
        }

        try:

            if method == RequestType.GET:
                self.response = requests.get(url, headers=header, timeout=10)

            elif method == RequestType.POST:
                header['Content-Type'] = "application/json"
                self.response = requests.post(url, headers=header, timeout=10,
                                              data=json.dumps(payload))
            elif method == RequestType.PUT:
                header['content-type'] = "application/json"
                self.response = requests.put(url, headers=header, timeout=10,
                                             data=json.dumps(payload))
            elif method == RequestType.DELETE:
                self.response = requests.delete(url, headers=header, timeout=10)

            elif method == RequestType.PATCH:
                self.response = requests.patch(url, headers=header, timeout=10,
                                               data=json.dumps(payload))
            return self.response

        except:
            raise
