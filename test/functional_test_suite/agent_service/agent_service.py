""" Functional Test cases for Agent Service """

import logging
import unittest
import httplib
import time
from test.shared.rest_framework import RestAPI, RequestType, path
from test.functional_test_suite.common.config import AGENT_SERVICE_URL
from test.functional_test_suite.common.config import agent_task_url
from test.functional_test_suite.common.config import agent_details_url
from test.functional_test_suite.common.config import register_agent_url
from test.functional_test_suite.common.config import list_system
from test.functional_test_suite.common.config import list_system_url
from test.functional_test_suite.common.config import INVENTORY_SERVICE_URL
from test.functional_test_suite.common.config import SEED_JOB_URL
from test.functional_test_suite.common.config import CUSTOMER_PROFILE_URL
from test.functional_test_suite.common.config import list_agent_tasks_url
from test.functional_test_suite.common.config import current_tickets_url
from test.functional_test_suite.common.config import seed_job_url
from test.functional_test_suite.common.config import agent_action_url
from test.functional_test_suite.common.config import update_ticket_url
from test.functional_test_suite.common.config import initialize_logger
from test.functional_test_suite.agent_service.agent_service_payloads import AgentServicePayload
from test.functional_test_suite.customer_profile_service.customer_profile_service_payloads import CustomerProfileServicePayload
from test.functional_test_suite.job_service.job_service_payloads import SeedJobServicePayload
from test.functional_test_suite.inventory_service.inventory_service_payloads import InventoryServicePayload
from test.functional_test_suite.ticket_service.ticket_service_payloads import TicketServicePayload

job_service_customer = RestAPI(utype='customer')
job_service_agent = RestAPI(utype='agent')
inventory_service = RestAPI(utype='sysops')
agent_service_customer = RestAPI(utype='customer')
agent_service_sysops = RestAPI(utype='sysops')
ticket_service = RestAPI(utype='sysops')
agent_service_agent = RestAPI(utype='agent')
agent_service_invalid = RestAPI(utype='invalid')
job_service = RestAPI(utype='customer')
initialize_logger(path + '/../../logs/agent_service.log')

address_title = job_service.request(
    RequestType.PUT, CUSTOMER_PROFILE_URL,
    payload=CustomerProfileServicePayload().customer_profile_payload()).json()['shipping_addresses'][0]['title']
source_system_id = job_service.request(
    RequestType.GET, list_system_url(list_system, system_type='source')).json()['systems'][0]['id']
target_system_id = job_service.request(
    RequestType.GET, list_system_url(list_system, system_type='target')).json()['systems'][0]['siteId']

job_id = 0
agent_id = 0
task_id = 0


class AgentServiceTestCases(unittest.TestCase):
    """ Test cases of agent service """

    """ GET: Test cases to get the list agents """

    def test___add_item_with_valid_details(self):
        """ Adding an item with all valid parameters into the inventory """

        # Add an item with valid details
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=InventoryServicePayload().inventory_additem_payload())
        add_item_response_dict = add_item_response.json()
        logging.info('test_add_item_with_valid_details')
        logging.info('Url is %s', INVENTORY_SERVICE_URL)
        logging.info('Request is %s',
                     InventoryServicePayload().inventory_additem_payload())
        logging.info('Response is %s', add_item_response.text)
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertIn(
            'created_at', add_item_response_dict.keys(),
            msg="Expected %s in %s" %
                ('created_at', add_item_response_dict.keys()))
        logging.info('test case executed successfully')

    def test___create_job_with_valid_details(self):
        """ Create job with valid details """

        global job_id
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload(
                address_title=address_title, source_system_id=source_system_id,
                target_system_id=target_system_id))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_with_valid_details')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s',
                     SeedJobServicePayload().create_seed_job_payload())
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 201,
            msg="Expected 201 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            'job_id', create_job_response_dict.keys(),
            msg=" Expected %s in %s" % (
                'job_id', create_job_response_dict.keys()))
        job_id = create_job_response_dict['job_id']
        logging.info('test case executed successfully')

    def test___current_ticket_details_with_valid_job_id(self):
        """ Testing with the valid job_id to get the details of the seed job """
        global ticket_id
        # Get the seed job details with valid job id
        job_details_response = job_service_customer.request(
            RequestType.GET, current_tickets_url(
                job_id, value='current_ticket'))
        job_details_response_dict = job_details_response.json()
        logging.info('test_job_details_with_valid_job_id')
        logging.info('Url is %s', current_tickets_url(
            job_id, value='current_ticket'))
        logging.info('Response is %s', job_details_response.text)
        self.assertEquals(
            job_details_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                job_details_response.status_code,
                httplib.responses[job_details_response.status_code]))
        self.assertIn(
            'job_id', job_details_response.json().keys(),
            msg="Expected %s in %s" %
                ('job_id', job_details_response.json().keys()))
        ticket_id = job_details_response_dict['current_ticket']
        logging.info('test case executed successfully')

    def test___current_ticket_update_with_valid_ticket_id(self):
        """ Update the ticket with the valid ticket_id """

        expected_message = "Updated Ticket id %s" % ticket_id

        # Update the ticket with valid ticket id
        ticket_response = ticket_service.request(
            RequestType.PUT, update_ticket_url(ticket_id=ticket_id),
            payload=TicketServicePayload().update_ticket_payload(
                ticket_status='CLOSED_COMPLETE'))
        ticket_response_dict = ticket_response.json()
        logging.info('test_update_ticket_with_valid_ticket_id')
        logging.info('Url is %s', update_ticket_url(ticket_id=ticket_id))
        logging.info('Request is %s',
                     TicketServicePayload().update_ticket_payload(
                         ticket_status='CLOSED_COMPLETE'))
        logging.info('Response is %s', ticket_response.text)
        self.assertEquals(
            ticket_response.status_code, 200,
            msg="Expected 200 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))
        self.assertEquals(
            expected_message, ticket_response_dict['message'],
            msg="%s is equal to %s" %
                (expected_message, ticket_response_dict['message']))
        logging.info('test case executed successfully')

    def test___job_details_with_valid_job_id(self):
        """ Testing with the valid job_id to get the details of the seed job """
        time.sleep(120)

        global agent_id

        # Get the seed job details with valid job id
        job_details_response = job_service_customer.request(
            RequestType.GET, seed_job_url(job_id))
        logging.info('test_job_details_with_valid_job_id')
        logging.info('Url is %s', seed_job_url(job_id))
        logging.info('Response is %s', job_details_response.text)
        self.assertEquals(
            job_details_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                job_details_response.status_code,
                httplib.responses[job_details_response.status_code]))
        self.assertIn(
            'job_id', job_details_response.json().keys(),
            msg="Expected %s in %s" %
                ('job_id', job_details_response.json().keys()))
        agent_id = job_details_response.json()['agent_id']
        logging.info('test case executed successfully')

    def test__list_agents_with_valid_url(self):
        """ Testing with the valid url to get the list agents """

        # Get list agents with valid url
        list_agents_response = agent_service_sysops.request(
            RequestType.GET, AGENT_SERVICE_URL)
        list_agents_response_dict = list_agents_response.json()
        logging.info('test_list_agents_with_valid_url')
        logging.info('Url is %s', AGENT_SERVICE_URL)
        logging.info('Request is %s', )
        logging.info('Response is %s', list_agents_response.text)
        self.assertEquals(
            list_agents_response.status_code, 200,
            msg="Expected response code is 200 and got is %s (%s)" % (
                list_agents_response.status_code,
                httplib.responses[list_agents_response.status_code]))
        self.assertIn('agents', list_agents_response_dict.keys(),
                      msg="Expected %s in and got is %s" % (
                          'message', list_agents_response_dict.keys()))
        logging.info('test case executed successfully')

    def test__list_agent_with_invalid_token(self):
        """ Testing with the invalid token to get the list agents """

        expected_message = "Unauthorized"

        # Get list agents with invalid url
        list_agents_response = agent_service_invalid.request(
            RequestType.GET, AGENT_SERVICE_URL)
        list_agents_response_dict = list_agents_response.json()
        logging.info('test_list_agent_with_invalid_token')
        logging.info('Url is %s', AGENT_SERVICE_URL)
        logging.info('Response is %s', list_agents_response.text)
        self.assertEquals(
            list_agents_response.status_code, 401,
            msg="Expected response code is 401 and got is %s (%s)" % (
                list_agents_response.status_code,
                httplib.responses[list_agents_response.status_code]))
        self.assertIn(
            expected_message, list_agents_response_dict['message'],
            msg="Expected %s in and got is %s" %
                (expected_message, list_agents_response_dict['message']))
        logging.info('test case executed successfully')

    """ GET: To get the details of an agent """

    def test_agent_details_with_valid_agent_id(self):
        """ Testing with valid agent id to get the details of an agent """

        key = "agent_id"

        # Get the details of an agent with valid agent id
        agent_details_response = agent_service_agent.request(
            RequestType.GET, agent_details_url(agent_id))
        agent_details_response_dict = agent_details_response.json()
        logging.info('test_agent_details_with_valid_agent_id')
        logging.info('Url is %s', agent_details_url(agent_id))
        logging.info('Response is %s', agent_details_response.text)
        self.assertEquals(
            agent_details_response.status_code, 200,
            msg="Expected response code is 200 and got is %s (%s)" % (
                agent_details_response.status_code,
                httplib.responses[agent_details_response.status_code]))
        self.assertIn(
            key, agent_details_response_dict.keys(),
            msg="Expected %s in %s" %
                (key, agent_details_response_dict.keys()))
        logging.info('test case executed successfully')

    def test_agent_details_with_invalid_agent_id(self):
        """ Testing with invalid agent id to get the details of an agent """

        expected_message = 'does not exists'

        # Get the details of an agent with invalid agent id
        agent_details_response = agent_service_agent.request(
            RequestType.GET, agent_details_url(agent_id="asd"))
        agent_details_response_dict = agent_details_response.json()
        logging.info('test_agent_details_with_invalid_agent_id')
        logging.info('Url is %s', agent_details_url(agent_id="asd"))
        logging.info('Response is %s', agent_details_response.text)
        self.assertEquals(
            agent_details_response.status_code, 404,
            msg="Expected response code is 404 and got is %s (%s)" % (
                agent_details_response.status_code,
                httplib.responses[agent_details_response.status_code]))
        self.assertIn(
            expected_message, agent_details_response_dict['message'],
            msg="Expected %s in %s" %
                (expected_message, agent_details_response_dict['message']))
        logging.info('test case executed successfully')

    def test_agent_action_with_valid_job_id(self):
        """ Testing with valid job_id to take an action on job by an agent """

        # Agent action with valid job id

        agent_action_response = job_service_agent.request(
            RequestType.PATCH,
            agent_action_url(job_id=job_id,
                             action='test_conn_source_success'),
            payload=SeedJobServicePayload().update_job_logs())
        logging.info('test_agent_action_with_valid_job_id')
        logging.info('Url is %s', agent_action_url(
            job_id=job_id, action='test_conn_source_success'))
        logging.info('Request is %s', SeedJobServicePayload().update_job_logs())
        logging.info('Response is %s', agent_action_response.text)
        self.assertEquals(
            agent_action_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                agent_action_response.status_code,
                httplib.responses[agent_action_response.status_code]))
        logging.info('test case executed successfully')

    """ GET: Test cases to get the list agent tasks """

    def test_agent_task__list_with_valid_agent_id(self):
        """ Testing with the valid agent id to get the list agent tasks """

        global task_id

        # Get list agent tasks  with valid url
        list_agents_tasks_response = agent_service_agent.request(
            RequestType.GET, list_agent_tasks_url(agent_id))
        list_agents_tasks_response_dict = list_agents_tasks_response.json()
        logging.info('test_list_agent_tasks_with_valid_agent_id')
        logging.info('Url is %s', list_agent_tasks_url(agent_id))
        logging.info('Response is %s', list_agents_tasks_response.text)
        self.assertEquals(
            list_agents_tasks_response.status_code, 200,
            msg="Expected response code is 200 and got is %s (%s)" % (
                list_agents_tasks_response.status_code,
                httplib.responses[list_agents_tasks_response.status_code]))
        self.assertIn('tasks', list_agents_tasks_response_dict.keys(),
                      msg="Expected %s in and got is %s" % (
                          'message', list_agents_tasks_response_dict.keys()))
        task_id = list_agents_tasks_response_dict['tasks'][0]['task_id']
        logging.info('test case executed successfully')

    def test_list_agent_tasks_with_invalid_agent_id(self):
        """ Testing with the invalid agent id to get the list agent tasks """

        expected_message = "Resource with id asd does not exists"

        # Get list agent tasks with invalid url
        list_agents_tasks_response = agent_service_agent.request(
            RequestType.GET, list_agent_tasks_url(agent_id="asd"))
        list_agents_tasks_response_dict = list_agents_tasks_response.json()
        logging.info('test_list_agent_tasks_with_invalid_agent_id')
        logging.info('Url is %s', list_agent_tasks_url(agent_id="asd"))
        logging.info('Response is %s', list_agents_tasks_response.text)
        self.assertEquals(
            list_agents_tasks_response.status_code, 404,
            msg="Expected response code is 404 and got is %s (%s)" % (
                list_agents_tasks_response.status_code,
                httplib.responses[list_agents_tasks_response.status_code]))
        self.assertEquals(
            expected_message, list_agents_tasks_response_dict['message'],
            msg="Expected %s in and got is %s" %
                (expected_message, list_agents_tasks_response_dict.keys()))
        logging.info('test case executed successfully')

    """ GET: To get the agent task details """

    def test_agent_task_details_with_valid_task_id(self):
        """ Testing with the valid task id to get the task details """

        # Get the agent task details with valid task id
        agent_task_details_response = agent_service_customer.request(
            RequestType.GET, agent_task_url(task_id))
        agent_task_details_response_dict = agent_task_details_response.json()
        logging.info('test_agent_task_details_with_valid_task_id')
        logging.info('Url is %s', agent_task_url(task_id))
        logging.info('Response is %s', agent_task_details_response.text)
        self.assertEquals(
            agent_task_details_response.status_code, 200,
            msg="Expected response code is 200 and got is %s (%s)" % (
                agent_task_details_response.status_code,
                httplib.responses[agent_task_details_response.status_code]))
        self.assertIn(
            'task_status', agent_task_details_response_dict.keys(),
            msg="Expected %s in and got is %s" % (
                'task_status', agent_task_details_response_dict.keys()))
        logging.info('test case executed successfully')

    def test_agent_task_details_with_invalid_task_id(self):
        """ Testing with the invalid task id to get the task details """

        taskid = '123asd'
        message = "Resource with id %s does not exists" % taskid

        # Get the agent task details with invalid task id
        agent_task_details_response = agent_service_customer.request(
            RequestType.GET, agent_task_url(task_id=taskid))
        agent_task_details_response_dict = agent_task_details_response.json()
        logging.info('test_agent_task_details_with_invalid_task_id')
        logging.info('Url is %s', agent_task_url(task_id=taskid))
        logging.info('Response is %s', agent_task_details_response.text)
        self.assertEquals(
            agent_task_details_response.status_code, 404,
            msg="Expected response code is 404 and got is %s" %
                httplib.responses[agent_task_details_response.status_code])
        self.assertEquals(
            message, agent_task_details_response_dict['message'],
            msg="Expected %s equals %s" %
                (message, agent_task_details_response_dict['message']))
        logging.info('test case executed successfully')

    def test_agent_task_details_with_invalid_token(self):
        """ Testing with the invalid task id to get the task details """

        message = "Unauthorized"

        # Get the agent task details with invalid task id
        agent_task_details_response = agent_service_invalid.request(
            RequestType.GET, agent_task_url(task_id=task_id))
        logging.info('test_agent_task_details_with_invalid_token')
        logging.info('Url is %s', agent_task_url(task_id=task_id))
        logging.info('Response is %s', agent_task_details_response.text)
        agent_task_details_response_dict = agent_task_details_response.json()
        self.assertEquals(
            agent_task_details_response.status_code, 401,
            msg="Expected response code is 401 and got is %s" %
                httplib.responses[agent_task_details_response.status_code])
        self.assertEquals(
            message, agent_task_details_response_dict['message'],
            msg="Expected %s equals %s" %
                (message, agent_task_details_response_dict['message']))
        logging.info('test case executed successfully')

    """ PUT: Test cases to update the agent task status """

    def test_update_agent_task_with_valid_task_id(self):
        """ Testing with the valid task id to update the agent task status """

        # Update the agent task with valid task id
        update_agent_task_response = agent_service_agent.request(
            RequestType.PUT, agent_task_url(task_id),
            payload=AgentServicePayload().update_agent_task_status())
        logging.info('test_update_agent_task_with_valid_task_id')
        logging.info('Url is %s', agent_task_url(task_id))
        logging.info('Request is %s', AgentServicePayload().
                     update_agent_task_status())
        logging.info('Response is %s', update_agent_task_response.text)
        self.assertEquals(
            update_agent_task_response.status_code, 200,
            msg="Expected response code is 200 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        logging.info('test case executed successfully')

    def test_update_agent_task_with_invalid_task_id(self):
        """ Testing with the invalid task id to update the agent task status """

        taskid = '1234'
        expected_message = "Resource with id %s does not exists" % taskid

        # Update the agent task with invalid task id
        update_agent_task_response = agent_service_agent.request(
            RequestType.PUT, agent_task_url(taskid),
            payload=AgentServicePayload().update_agent_task_status())
        update_agent_task_response_dict = update_agent_task_response.json()
        logging.info('test_update_agent_task_with_invalid_task_id')
        logging.info('Url is %s', agent_task_url(taskid))
        logging.info('Request is %s', AgentServicePayload().
                     update_agent_task_status())
        logging.info('Response is %s', update_agent_task_response.text)
        self.assertEquals(
            update_agent_task_response.status_code, 404,
            msg="Expected response code is 404 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        self.assertIn(
            expected_message, update_agent_task_response_dict['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, update_agent_task_response_dict['message']))
        logging.info('test case executed successfully')

    def test_update_agent_task_with_invalid_token(self):
        """ Testing with the invalid token to update the agent task status """

        expected_message = "Unauthorized"

        # Update the agent task with invalid token
        update_agent_task_response = agent_service_invalid.request(
            RequestType.PUT, agent_task_url(task_id=task_id),
            payload=AgentServicePayload().update_agent_task_status())
        update_agent_task_response_dict = update_agent_task_response.json()
        logging.info('test_update_agent_task_with_invalid_token')
        logging.info('Url is %s', agent_task_url(task_id=task_id))
        logging.info('Request is %s', AgentServicePayload().
                     update_agent_task_status())
        logging.info('Response is %s', update_agent_task_response.text)
        self.assertEquals(
            update_agent_task_response.status_code, 401,
            msg="Expected response code is 401 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        self.assertIn(
            expected_message, update_agent_task_response_dict['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, update_agent_task_response_dict['message']))
        logging.info('test case executed successfully')

    def test_update_agent_task_with_invalid_status(self):
        """ Testing with the invalid status to update the agent task status """
        status = 'excepted'
        expected_message = "status %s of task is not recognized" % status

        # Update the agent task with invalid status
        update_agent_task_response = agent_service_agent.request(
            RequestType.PUT, agent_task_url(task_id=task_id),
            payload=AgentServicePayload().update_agent_task_status(status))
        update_agent_task_response_dict = update_agent_task_response.json()
        logging.info('test_update_agent_task_with_invalid_status')
        logging.info('Url is %s', agent_task_url(task_id='task_id'))
        logging.info('Request is %s', AgentServicePayload().
                     update_agent_task_status(status))
        logging.info('Response is %s', update_agent_task_response.text)
        self.assertEquals(
            update_agent_task_response.status_code, 400,
            msg="Expected response code is 400 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        self.assertIn(
            expected_message, update_agent_task_response_dict['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, update_agent_task_response_dict['message']))
        logging.info('test case executed successfully')

    def test_update_agent_task_without_status(self):
        """ Testing without status to update the agent task status """

        expected_message = "status  of task is not recognized "

        # Update the agent task without status
        update_agent_task_response = agent_service_agent.request(
            RequestType.PUT, agent_task_url(task_id='task_id'),
            payload=AgentServicePayload().update_agent_task_status(status=''))
        update_agent_task_response_dict = update_agent_task_response.json()
        logging.info('test_update_agent_task_without_status')
        logging.info('Url is %s', agent_task_url(task_id='task_id'))
        logging.info('Request is %s', AgentServicePayload().
                     update_agent_task_status(status=''))
        logging.info('Response is %s', update_agent_task_response.text)
        self.assertEquals(
            update_agent_task_response.status_code, 400,
            msg="Expected response code is 400 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        self.assertIn(
            expected_message, update_agent_task_response_dict['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, update_agent_task_response_dict['message']))
        logging.info('test case executed successfully')

    """ PUT: Test cases to Register an agent by passing input parameters """

    def test_agent_register_with_valid_agent_id(self):
        """ Testing with valid url to register an agent """

        expected_message = "Crane Agent is registered successfully."

        # Register an agent with valid agent id
        register_agent_response = agent_service_agent.request(
            RequestType.PUT, register_agent_url(agent_id),
            payload=AgentServicePayload().register_agent())
        register_agent_response_dict = register_agent_response.json()
        logging.info('test_register_agent_with_valid_agent_id')
        logging.info('Url is %s', register_agent_url(agent_id))
        logging.info('Request is %s', AgentServicePayload().register_agent())
        logging.info('Response is %s', register_agent_response.text)
        self.assertEquals(
            register_agent_response.status_code, 202,
            msg="Expected response code is 202 and got is %s (%s)" % (
                register_agent_response.status_code,
                httplib.responses[register_agent_response.status_code]))
        self.assertEquals(
            expected_message, register_agent_response_dict['message'],
            msg="Expected %s equals %s" % (
                expected_message, register_agent_response_dict['message']))
        logging.info('test case executed successfully')

    def test_register_agent_with_invalid_agent_id(self):
        """ Testing with invalid url to register an agent """

        # Register an agent with invalid agent id
        register_agent_response = agent_service_agent.request(
            RequestType.PUT, register_agent_url(agent_id='sbh'),
            payload=AgentServicePayload().register_agent())
        register_agent_response_dict = register_agent_response.json()
        logging.info('test_register_agent_with_invalid_agent_id')
        logging.info('Url is %s', register_agent_url(agent_id='sbh'))
        logging.info('Request is %s', AgentServicePayload().register_agent())
        logging.info('Response is %s', register_agent_response.text)
        self.assertEquals(
            register_agent_response.status_code, 500,
            msg="Expected response code is 500 and got is %s (%s)" % (
                register_agent_response.status_code,
                httplib.responses[register_agent_response.status_code]))
        self.assertIn(
            'message', register_agent_response_dict.keys(),
            msg="Expected %s in %s" %
                ('message', register_agent_response_dict.keys()))
        logging.info('test case executed successfully')

    def test_register_agent_with_invalid_token(self):
        """ Testing with invalid url to register an agent """

        expected_message = "Unauthorized"

        # Register an agent with invalid token
        register_agent_response = agent_service_invalid.request(
            RequestType.PUT, register_agent_url(agent_id=agent_id),
            payload=AgentServicePayload().register_agent())
        register_agent_response_dict = register_agent_response.json()
        logging.info('test_register_agent_with_invalid_token')
        logging.info('Url is %s', register_agent_url(agent_id=agent_id))
        logging.info("Request is %s", AgentServicePayload().register_agent())
        logging.info('Response is %s', register_agent_response.text)
        self.assertEquals(
            register_agent_response.status_code, 401,
            msg="Expected response code is 401 and got is %s (%s)" % (
                register_agent_response.status_code,
                httplib.responses[register_agent_response.status_code]))
        self.assertEquals(
            expected_message, register_agent_response_dict['message'],
            msg="Expected %s in %s" %
                (expected_message, register_agent_response_dict['message']))
        logging.info('test case executed successfully')
