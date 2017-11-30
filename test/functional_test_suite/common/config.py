import os
import yaml
path = os.environ['PYTHONPATH']
with open(path + "/env/configuration.yaml", 'r') as stream:
    try:
        config_data = yaml.load(stream)
    except yaml.YAMLError as exc:
        print "Cannot able to access input configuration"

""" All Constants goes here """

CUSTOMER_SERVICE_URL = config_data['BASE_URL'].format(config_data['CUSTOMER_SERVICE_API_ID']) + "/customer-profiles/"
INVENTORY_SERVICE_URL = config_data['BASE_URL'].format(config_data['INVENTORY_SERVICE_API_ID']) + "/inventory/items"
SYSTEM_SERVICE_URL = config_data['BASE_URL'].format(config_data['SYSTEM_SERVICE_API_ID']) + "/system"
SEED_JOB_URL = config_data['BASE_URL'].format(config_data['SEED_JOB_API_ID']) + "/jobs"
AGENT_SERVICE_URL = config_data['BASE_URL'].format(config_data['AGENT_SERVICE_API_ID']) + "/agents"
TICKET_SERVICE_URL = config_data['BASE_URL'].format(config_data['TICKET_SERVICE_API_ID']) + "/tickets"
AUTH_SERVICE_URL = config_data['BASE_URL'].format(config_data['AUTH_SERVICE_API_ID']) + "/auth/users"


SYSTEM_SERVICE = config_data['BASE_URL'].format(config_data['SYSTEM_SERVICE_API_ID'])
SOURCE_SYSTEM_ID = config_data['SOURCE_SYSTEM_ID']
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


def admin_action_url(seedjobid, action):
    """ Url for giving an action by admin """
    return '%s/admin/%s?action=%s' % (SEED_JOB_URL, seedjobid, action)


def update_job_logs_url(val):
    """ Url for update job logs by an agent """
    return '%s/agent/%s' % (SEED_JOB_URL, val)


def agent_api_url(val, value):
    """ Url for agent api on seed job """
    return '%s/agent/%s?action=%s' % (SEED_JOB_URL, val, value)


def ticket_detail_url(value):
    """ url to get the details of ticket """
    return '%s/%s' % (TICKET_SERVICE_URL, value)
