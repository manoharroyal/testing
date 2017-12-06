import json
import os
import sys
import requests
import jwt
from enum import Enum
import yaml
path = os.path.dirname(os.path.realpath(__file__))
with open(path + "/../../env/configuration.yaml", 'r') as stream:
    try:
        config_data = yaml.load(stream)
    except yaml.YAMLError as exc:
        print "Cannot able to access input configuration"

USER_LOGIN_URL = config_data['USER_LOGIN_URL']
LOGIN_URL = config_data['LOGIN_URL']

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


class RestAPI(object):
    """ The helper class for api calling """

    def __init__(self, utype='invalid'):
        self.response = None
        self.id_token = None
        if utype == 'customer':
            self.id_token, self.customerId = self.generate_customer_token()
        if utype == 'invalid':
            self.id_token, self.customerId = self.generate_customer_invalid_token()
        if utype == 'sysops':
            self.id_token, self.customerId = self.generate_sysops_token()
        if utype == 'agent':
            self.id_token, self.customerId = self.generate_agent_token()
        self.id_token = "Bearer " + self.id_token

    def generate_customer_token(self):
        """ Generation of token """

        data = {
            "client_id": config_data['client_id'],
            "username": config_data['customer_username'],
            "password": config_data['customer_password'],
            "connection": config_data['customer_connection'],
            "grant_type": config_data['customer_grant_type'],
            "scope": config_data['customer_scope']
        }

        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(USER_LOGIN_URL, data=json.dumps(data),
                                 headers=header)
        try:
            encode = str(response.json()['id_token'])

        except:
            print "Cannot able to parse the token in Login"
            sys.exit(1)
        decode = jwt.decode(encode, 'secret', algorithm=['RS256'], verify=False)
        customer_id = decode['customerId']
        return encode, customer_id

    def generate_customer_invalid_token(self):
        """ Function to generate invalid token """
        encode, customer_id = self.generate_customer_token()
        encode = encode + 'as'
        return encode, customer_id

    def generate_sysops_token(self):

        data = {
            "client_id": config_data['client_id'],
            "client_secret": config_data['client_secret'],
            "audience": config_data["audience"],
            "grant_type": config_data['grant_type'],
            "username": config_data['sysops_username'],
            "password": config_data['sysops_password'],
            "realm": config_data['sysops_realm'],
            "scope": config_data['scope']
        }

        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(LOGIN_URL, data=json.dumps(data), headers=header)
        try:
            encode = str(response.json()['access_token'])
        except:
            print "Cannot able to parse the token in Login"
            sys.exit(1)
        return encode, response.json()

    def generate_agent_token(self):
        """ Generation of agent_token """

        data = {
            "client_id": config_data['client_id'],
            "client_secret": config_data['client_secret'],
            "audience": config_data["audience"],
            "grant_type": config_data['grant_type'],
            "username": config_data['agent_username'],
            "password": config_data['agent_password'],
            "realm": config_data['realm'],
            "scope": config_data['scope']
        }

        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(LOGIN_URL, data=json.dumps(data), headers=header)
        try:
            encode = str(response.json()['access_token'])
        except:
            print "Cannot able to parse the token in Login"
            sys.exit(1)
        return encode, response.json()

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
                self.response = requests.post(url, headers=header, timeout=10,
                                              data=json.dumps(payload))
            elif method == RequestType.PUT:
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
