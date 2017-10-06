""" All Constants goes here """

CUSTOMER_SERVICE_URL = "https://oywvlaayha.execute-api.us-west-2.amazonaws.com/dev/customer-profiles/"

INVENTORY_SERVICE_URL = "https://ipn2b7o6dj.execute-api.us-west-2.amazonaws.com/sb186123dev/inventory/items"

SYSTEM_SERVICE_URL = "https://tlgz19gbal.execute-api.us-west-2.amazonaws.com/dev/system"

SYSTEM_API_URL = "https://tlgz19gbal.execute-api.us-west-2.amazonaws.com/dev/"

SEED_JOB_URL = "https://ulqh6w1du6.execute-api.us-west-2.amazonaws.com/dev/seed-jobs/"

AGENT_SERVICE_URL = "https://4k0bte7z20.execute-api.us-west-2.amazonaws.com/dev/agent"

TICKET_SERVICE_URL = "https://wl0qnbvoqf.execute-api.us-west-2.amazonaws.com/vr186027dev/tickets/{ticket_id}"


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


def update_agent_task_url(task_id):
    """ Url to update the agent task status """
    return '%s/%s' % (LIST_AGENT_TASK_URL, task_id)


def agent_details_url(agent_id):
    """ Get the details agent """
    return '%s/%s' % (AGENT_SERVICE_URL, agent_id)

INVALID_SEED_JOB_URL = SEED_JOB_URL+"234"
TEMP_KEY = 'bb90c867-a02e-4868-bfff-a8ef9c5f68eb2'
SEED_JOB_ID = 'ee5ca93d-a60f-4655-9bde-9fad3304cb0f'
DELETE_JOB_ID = '30b93452-71c3-4522-909b-016ea82ee13d'


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

