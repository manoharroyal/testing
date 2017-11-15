import os
import yaml

path = os.environ['PYTHONPATH']
with open(path + "/env/configuration.yaml", 'r') as stream:
    try:
       config_data = yaml.load(stream)
    except yaml.YAMLError as exc:
        print("Cannot able to access input configuration")


""" All Constants goes here """

CUSTOMER_SERVICE_URL = config_data['BASE_URL'].format(config_data['CUSTOMER_SERVICE_API_ID']) + "/customer-profiles/"
INVENTORY_SERVICE_URL = config_data['BASE_URL'].format(config_data['INVENTORY_SERVICE_API_ID']) + "/inventory/items"
SYSTEM_SERVICE_URL = config_data['BASE_URL'].format(config_data['SYSTEM_SERVICE_API_ID']) + "/system"
SEED_JOB_URL = config_data['BASE_URL'].format(config_data['SEED_JOB_API_ID']) + "/seed-jobs/"
AGENT_SERVICE_URL = config_data['BASE_URL'].format(config_data['AGENT_SERVICE_API_ID']) + "/agent"
TICKET_SERVICE_URL = config_data['BASE_URL'].format(config_data['TICKET_SERVICE_API_ID']) + "/tickets"

SYSTEM_SERVICE = config_data['BASE_URL'].format(config_data['SYSTEM_SERVICE_API_ID'])
SOURCE_SYSTEM_ID = "86dc65e4-42a0-4ee8-91e8-f201678f53aa"
TEMP_KEY = config_data['TEMP_KEY']
SEED_JOB_ID = config_data['SEED_JOB_ID']
DELETE_JOB_ID = config_data['DELETE_JOB_ID']

""" Setting up the parameters with urls """


def get_items_url(param, val):
    """ Url for checking the item availability in the inventory"""
    return '%s?%s=%s' % (INVENTORY_SERVICE_URL, param, val)


def update_url(val):
    """ Url for updating the item status in the inventory by item id """
    return '%s/%s' % (INVENTORY_SERVICE_URL, val)


def list_system_url(list_system, system_type):
    """ Url to get the list of systems """
    return '%s%s' % (list_system, system_type)


list_system = SYSTEM_SERVICE_URL + "/?type="
source_system = SYSTEM_SERVICE_URL + "/source/"
target_system = SYSTEM_SERVICE_URL + "/target/"


def source_system_url(source_system, system_id):
    """ Url to get the details of source system """
    return '%s%s' % (source_system, system_id)


def target_system_url(target_system, site_id):
    """ Url to get the details of target system"""
    return '%s%s' % (target_system, site_id)

agent_id = '6be1b3d7-b9e9-4808-b8d2-1b0197d848e7'
LIST_AGENT_TASK_URL = AGENT_SERVICE_URL + '/tasks'
REGISTER_AGENT_URL = AGENT_SERVICE_URL + '/register'
INVALID_SEED_JOB_URL = config_data['BASE_URL'].format(config_data['SEED_JOB_API_ID']) + "/seed-jobs1/"
TICKETS_URL = TICKET_SERVICE_URL + "/{ticket_id}"


def update_agent_task_url(task_id):
    """ Url to update the agent task status """
    return '%s/%s' % (LIST_AGENT_TASK_URL, task_id)


def agent_details_url(agent_id):
    """ Get the details agent """
    return '%s/%s' % (AGENT_SERVICE_URL, agent_id)


def seed_job_url(seed_job_id):
    """ Url to GET details of seed job and update the seed job and
    DELETE the seed job with job id """
    return '%s%s' % (SEED_JOB_URL, seed_job_id)


def user_action_url(seed_job_id, action):
    """ Url for giving an action by user """
    return '%s%s/job?action=%s' % (SEED_JOB_URL, seed_job_id, action)


def admin_action_url(seedjobid, action):
    """ Url for giving an action by admin """
    return '%s/admin/%s?action=%s' % (SEED_JOB_URL, seedjobid, action)


def update_job_logs_url(val):
    """ Url for update job logs by an agent """
    return '%s/agent/%s' % (SEED_JOB_URL, val)


def agent_api_url(val, value):
    """ Url for agent api on seed job """
    return '%sagent/%s?action=%s' % (SEED_JOB_URL, val, value)


def ticket_detail_url(value):
    """ url to get the details of ticket """
    return '%s/%s' % (TICKET_SERVICE_URL, value)
