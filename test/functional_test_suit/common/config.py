import os
import yaml

path = os.environ['PYTHONPATH']

with open(path + "/env/configuration.yaml", 'r') as stream:
    try:
       config_data = yaml.load(stream)
    except yaml.YAMLError as exc:
        print("Cannot able to access input configuration")


""" All Constants goes here """

CUSTOMER_SERVICE_URL = config_data['CUSTOMER_SERVICE_URL']

INVENTORY_SERVICE_URL = config_data['INVENTORY_SERVICE_URL']

SYSTEM_SERVICE_URL = config_data['SYSTEM_SERVICE_URL']

SYSTEM_API_URL = config_data['SYSTEM_API_URL']

SEED_JOB_URL = config_data['SEED_JOB_URL']

AGENT_SERVICE_URL = config_data['AGENT_SERVICE_URL']

TICKET_SERVICE_URL = config_data['TICKET_SERVICE_URL']

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

LIST_AGENT_TASK_URL = AGENT_SERVICE_URL + '/tasks'
REGISTER_AGENT_URL = AGENT_SERVICE_URL + '/register'
INVALID_SEED_JOB_URL = SEED_JOB_URL+"234"

def update_agent_task_url(task_id):
    """ Url to update the agent task status """
    return '%s/%s' % (LIST_AGENT_TASK_URL, task_id)


def agent_details_url(agent_id):
    """ Get the details agent """
    return '%s/%s' % (AGENT_SERVICE_URL, agent_id)

def seed_job_url(seed_jobid):
    """ Url to GET details of seed job and update the seed job and
    DELETE the seed job with job id """
    return '%s%s' % (SEED_JOB_URL, seed_jobid)


def user_action_url(seed_job_id, action):
    """ Url for giving an action by user """
    return '%s/%s/job?action=%s' % (SEED_JOB_URL, seed_job_id, action)


def admin_action_url(seedjobid, action):
    """ Url for giving an action by admin """
    return '%s/admin/%s?action=%s' % (SEED_JOB_URL, seedjobid, action)


def update_job_logs_url(val):
    """ Url for update joblogs by an agent """
    return '%s/agent/%s' % (SEED_JOB_URL, val)


def agent_api_url(val, value):
    """ Url for agent api on seed job """
    return '%s/agent/%s?action=%s' % (SEED_JOB_URL, val, value)
