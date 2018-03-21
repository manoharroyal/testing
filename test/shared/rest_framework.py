import json
import os
import sys
import requests
import jwt
import yaml
from enum import Enum
path = os.path.dirname(os.path.realpath(__file__))
with open(path + "/../../env/configuration.yaml", 'r') as stream:
    try:
        config_data = yaml.load(stream)
    except yaml.YAMLError as exc:
        print "Cannot able to access input configuration"

LOGIN_URL = config_data['LOGIN_URL']

""" Pre Function """


def pre_check(key):
    if config_data.get(key) != None:
        pass
    elif os.environ.get(key) != None:
        config_data[key] = os .environ[key]
    else:
        print "[Error] set %s in env file or shell using export" % key
        sys.exit(1)


""" checking ..."""
pre_check('customer_password')
pre_check('sysops_password')
pre_check('agent_password')

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
            "audience": config_data["audience"],
            "grant_type": config_data['grant_type'],
            "username": config_data['customer_username'],
            "password": config_data['customer_password'],
            "realm": config_data['customer_realm'],
            "scope": config_data['scope']
        }

        header = {
            "Content-Type": "application/json"
        }
        response = requests.post(LOGIN_URL, data=json.dumps(data),
                                 headers=header)
        try:
            encode = str(response.json()['access_token'])

        except:
            print "Cannot able to parse the token in Login"
            sys.exit(1)
        decode = jwt.decode(encode, 'secret', algorithm=['RS256'], verify=False)
        customer_id = decode['https://dev.teradatacloud.io/customerId']
        return encode, customer_id

    def generate_customer_invalid_token(self):
        """ Function to generate invalid token """
        encode, customer_id = self.generate_customer_token()
        encode = "as" + encode + 'as'
        return encode, customer_id

    def generate_sysops_token(self):

        data = {
            "client_id": config_data['client_id'],
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
            "audience": config_data["audience"],
            "grant_type": config_data['grant_type'],
            "username": config_data['agent_username'],
            "password": config_data['agent_password'],
            "realm": config_data['agent_realm'],
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
                self.response = requests.get(
                    url, headers=header, timeout=30)
            elif method == RequestType.POST:
                self.response = requests.post(
                    url, headers=header, timeout=30, data=json.dumps(payload))
            elif method == RequestType.PUT:
                self.response = requests.put(
                    url, headers=header, timeout=30, data=json.dumps(payload))
            elif method == RequestType.DELETE:
                self.response = requests.delete(
                    url, headers=header, timeout=30)
            elif method == RequestType.PATCH:
                self.response = requests.patch(
                    url, headers=header, timeout=30, data=json.dumps(payload))
            return self.response

        except:
            raise
