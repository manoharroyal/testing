import os
import yaml
import logging
from test.shared.rest_framework import RestAPI, RequestType
path = os.path.dirname(os.path.realpath(__file__))
with open(path + "/../../../env/configuration.yaml", 'r') as stream:
    try:
        config_data = yaml.load(stream)
    except yaml.YAMLError as exc:
        print "Cannot able to access input configuration"

end_point = RestAPI(utype='customer')


class EndPoints(object):
    """ class to get end points """

    def generate_customer_url(self):
        response = end_point.request(
            RequestType.GET, config_data['END_POINTS_URL']).json()
        return response['customer-profile-dev'][0]['endpoint']

    def generate_system_url(self):
        response = end_point.request(
            RequestType.GET, config_data['END_POINTS_URL']).json()
        return response['system-service-dev'][0]['endpoint']

    def generate_inventory_url(self):
        response = end_point.request(
            RequestType.GET, config_data['END_POINTS_URL']).json()
        return response['inventory-service-dev'][0]['endpoint']

    def generate_agent_url(self):
        response = end_point.request(
            RequestType.GET, config_data['END_POINTS_URL']).json()
        return response['agent-service-dev'][0]['endpoint']

    def generate_job_url(self):
        response = end_point.request(
            RequestType.GET, config_data['END_POINTS_URL']).json()
        return response['seedjob-service-dev'][0]['endpoint']

    def generate_ticket_url(self):
        response = end_point.request(
            RequestType.GET, config_data['END_POINTS_URL']).json()
        return response['ticket-service-dev'][0]['endpoint']

    def generate_auth_url(self):
        response = end_point.request(
            RequestType.GET, config_data['END_POINTS_URL']).json()
        return response['auth-dev'][0]['endpoint']


api = EndPoints()

""" All Constants goes here """
CUSTOMER_SERVICE_URL = api.generate_customer_url().replace("{customer_id}", "")
INVENTORY_SERVICE_URL = api.generate_inventory_url()
SYSTEM_SERVICE_URL = api.generate_system_url()
SEED_JOB_URL = api.generate_job_url()
AGENT_SERVICE_URL = api.generate_agent_url()
TICKET_SERVICE_URL = api.generate_ticket_url()
AUTH_SERVICE_URL = api.generate_auth_url()

TEMP_KEY = config_data['TEMP_KEY']
SEED_JOB_ID = config_data['SEED_JOB_ID']
DELETE_JOB_ID = config_data['DELETE_JOB_ID']

""" Setting up the parameters with urls """


def get_items_url(param, value):
    """ Url for checking the item availability in the inventory"""
    return '%s?%s=%s' % (INVENTORY_SERVICE_URL, param, value)


def update_item_url(item_id):
    """ Url for updating the item status in the inventory by item id """
    return '%s/%s' % (INVENTORY_SERVICE_URL, item_id)


def list_system_url(list_system, system_type):
    """ Url to get the list of systems """
    return '%s%s' % (list_system, system_type)


list_system = SYSTEM_SERVICE_URL + "/?type="
source_system = SYSTEM_SERVICE_URL + "/source/"
target_system = SYSTEM_SERVICE_URL + "/target/"
validate_auth_user_url = AUTH_SERVICE_URL + "/validate"


def delete_auth_user_url(user_id):
    """ Url to delete the user """
    return '%s/%s' % (AUTH_SERVICE_URL, user_id)


def source_system_url(system_id):
    """ Url to get the details of source system """
    return '%s%s' % (source_system, system_id)


def target_system_url(site_id):
    """ Url to get the details of target system"""
    return '%s%s' % (target_system, site_id)


agent_id = 'dd12082c-972e-49d7-a8ec-13d30a2f59b2'
TICKETS_URL = TICKET_SERVICE_URL + "/{ticket_id}"
LIST_AGENT_TASK_URL = AGENT_SERVICE_URL + '/tasks'


def list_agent_tasks_url(agent_id):
    """ Url to get the list agent tasks """
    return '%s/%s/tasks' % (AGENT_SERVICE_URL, agent_id)


def agent_details_url(agent_id):
    """ Get the details agent """
    return '%s/%s' % (AGENT_SERVICE_URL, agent_id)


def agent_task_url(task_id):
    """ Url to update the agent task status """
    return '%s/tasks/%s' % (AGENT_SERVICE_URL, task_id)


def register_agent_url(agent_id):
    """ Url to register an agent """
    return '%s/%s/register' % (AGENT_SERVICE_URL, agent_id)


def seed_job_url(seed_job_id):
    """ Url to GET details of seed job and update the seed job and
    DELETE the seed job with job id """
    return '%s/%s' % (SEED_JOB_URL, seed_job_id)


def user_action_url(seed_job_id, action):
    """ Url for giving an action by user """
    return '%s/%s/job?action=%s' % (SEED_JOB_URL, seed_job_id, action)


def agent_action_url(job_id, action):
    """ Url for agent api on seed job """
    return '%s/agent/%s?action=%s' % (SEED_JOB_URL, job_id, action)


def ticket_detail_url(ticket_id):
    """ url to get the details of ticket """
    return '%s/%s' % (TICKET_SERVICE_URL, ticket_id)


output_dir = path


def initialize_logger(output_dir):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to info
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create error file handler and set level to error
    handler = logging.FileHandler(os.path.join(output_dir, "error.log"), "w",
                                  encoding=None, delay="true")
    handler.setLevel(logging.ERROR)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # create debug file handler and set level to debug
    handler = logging.FileHandler(os.path.join(output_dir), "w")
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
