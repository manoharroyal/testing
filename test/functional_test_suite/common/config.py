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

""" All Constants goes here """
CUSTOMER_SERVICE_URL = end_point.request(
    RequestType.GET,
    config_data['END_POINTS_URL']).json()['customer-profile-dev'][0]['endpoint'].replace("{customer_id}", "")
INVENTORY_SERVICE_URL = end_point.request(
    RequestType.GET,
    config_data['END_POINTS_URL']).json()['inventory-service-dev'][0]['endpoint']
SYSTEM_SERVICE_URL = end_point.request(
    RequestType.GET,
    config_data['END_POINTS_URL']).json()['system-service-dev'][0]['endpoint']
SEED_JOB_URL = end_point.request(
    RequestType.GET,
    config_data['END_POINTS_URL']).json()['seedjob-service-dev'][0]['endpoint']
AGENT_SERVICE_URL = end_point.request(
    RequestType.GET,
    config_data['END_POINTS_URL']).json()['agent-service-dev'][0]['endpoint']
TICKET_SERVICE_URL = end_point.request(
    RequestType.GET,
    config_data['END_POINTS_URL']).json()['ticket-service-dev'][0]['endpoint']
AUTH_SERVICE_URL = end_point.request(
    RequestType.GET,
    config_data['END_POINTS_URL']).json()['auth-dev'][0]['endpoint']
BOX_SERVICE_URL = end_point.request(
    RequestType.GET,
    config_data['END_POINTS_URL']).json()['box-manager-dev'][-1]['endpoint']
ORDER_SERVICE_URL = end_point.request(
    RequestType.GET,
    config_data['END_POINTS_URL']).json()['order-manager-dev'][0]['endpoint'].replace("{order_id}/track", "")


TEMP_KEY = config_data['TEMP_KEY']
SEED_JOB_ID = config_data['SEED_JOB_ID']
DELETE_JOB_ID = config_data['DELETE_JOB_ID']

""" Setting up the parameters with urls """


def get_tickets_url(job_id):
    """ Url to get list of tickets of particular job """
    return '%s?job_id=%s' % (TICKET_SERVICE_URL, job_id)


def order_details_url(order_id):
    """ Url to get tracking details of an order """
    return '%s/%s/track' % (ORDER_SERVICE_URL, order_id)


def box_details_url(id):
    """ Url ti get the details of box """
    return '%s/%s' % (BOX_SERVICE_URL, id)


def box_action_url(box_id):
    """ Url to action on box """
    return '%s/%s' % (BOX_SERVICE_URL, box_id)


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


agent_id = '000f1fa0-fba6-44b9-9232-fcfab1f2b999'
task_id = '558ca2ce-957b-47a2-b851-128aba72224b'
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


def update_ticket_url(ticket_id):
    """ url to get the details of ticket """
    return '%s/%s' % (TICKET_SERVICE_URL, ticket_id)


""" logging function goes here """


def initialize_logger(output_dir):
    """ logging function to generate log reports """

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    fh = logging.FileHandler(os.path.join(output_dir), "w", encoding=None, delay=True)
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    logger.debug('This is a test log message.')
