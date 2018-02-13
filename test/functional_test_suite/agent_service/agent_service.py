""" Functional Test cases for Agent Service """

import logging
import unittest
import httplib
from test.functional_test_suite.agent_service.agent_service_payloads import AgentServicePayload
from test.shared.rest_framework import RestAPI, RequestType, path
from test.functional_test_suite.common.config import AGENT_SERVICE_URL, \
    agent_task_url, agent_id, task_id, agent_details_url, register_agent_url, \
    list_agent_tasks_url, initialize_logger

agent_service_customer = RestAPI(utype='customer')
agent_service_sysops = RestAPI(utype='sysops')
agent_service_agent = RestAPI(utype='agent')
agent_service_invalid = RestAPI(utype='invalid')
initialize_logger(path + '/../../logs/agent_service.log')


class AgentServiceTestCases(unittest.TestCase):
    """ Test cases of agent service """

    """ GET: Test cases to get the list agents """

    def test_list_agents_with_valid_url(self):
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

    def test_list_agent_with_invalid_token(self):
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

    """ GET: Test cases to get the list agent tasks """

    def test_list_agent_tasks_with_valid_agent_id(self):
        """ Testing with the valid agent id to get the list agent tasks """

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
            RequestType.GET, agent_task_url(task_id=task_id))
        agent_task_details_response_dict = agent_task_details_response.json()
        logging.info('test_agent_task_details_with_valid_task_id')
        logging.info('Url is %s', agent_task_url(task_id=task_id))
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
            RequestType.PUT, agent_task_url(task_id=task_id),
            payload=AgentServicePayload().update_agent_task_status(
                status='update', message='updated'))
        logging.info('test_update_agent_task_with_valid_task_id')
        logging.info('Url is %s', agent_task_url(task_id=task_id))
        logging.info('Request is %s', AgentServicePayload().
                     update_agent_task_status(status='update',
                                              message='updated'))
        logging.info('Response is %s', update_agent_task_response.text)
        self.assertEquals(
            update_agent_task_response.status_code, 202,
            msg="Expected response code is 202 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        logging.info('test case executed successfully')

    def test_update_agent_task_with_invalid_task_id(self):
        """ Testing with the invalid task id to update the agent task status """

        expected_message = "status string of task is not recognized"

        # Update the agent task with invalid task id
        update_agent_task_response = agent_service_agent.request(
            RequestType.PUT, agent_task_url(task_id='task_id'),
            payload=AgentServicePayload().update_agent_task_status())
        update_agent_task_response_dict = update_agent_task_response.json()
        logging.info('test_update_agent_task_with_invalid_task_id')
        logging.info('Url is %s', agent_task_url(task_id='task_id'))
        logging.info('Request is %s', AgentServicePayload().
                     update_agent_task_status())
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
            payload=AgentServicePayload().update_agent_task_status(status=status))
        update_agent_task_response_dict = update_agent_task_response.json()
        logging.info('test_update_agent_task_with_invalid_status')
        logging.info('Url is %s', agent_task_url(task_id='task_id'))
        logging.info('Request is %s', AgentServicePayload().
                     update_agent_task_status(status='su'))
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

    def test_register_agent_with_valid_agent_id(self):
        """ Testing with valid url to register an agent """

        # Register an agent with valid agent id
        register_agent_response = agent_service_agent.request(
            RequestType.PUT, register_agent_url(agent_id))
        logging.info('test_register_agent_with_valid_agent_id')
        logging.info('Url is %s', register_agent_url(agent_id))
        logging.info('Response is %s', register_agent_response.text)
        self.assertEquals(
            register_agent_response.status_code, 202,
            msg="Expected response code is 202 and got is %s (%s)" % (
                register_agent_response.status_code,
                httplib.responses[register_agent_response.status_code]))
        logging.info('test case executed successfully')

    def test_register_agent_with_invalid_agent_id(self):
        """ Testing with invalid url to register an agent """

        # Register an agent with invalid agent id
        register_agent_response = agent_service_agent.request(
            RequestType.PUT, register_agent_url(agent_id='sbh'))
        register_agent_response_dict = register_agent_response.json()
        logging.info('test_register_agent_with_invalid_agent_id')
        logging.info('Url is %s', register_agent_url(agent_id='sbh'))
        logging.info('Response is %s', register_agent_response.text)
        self.assertEquals(
            register_agent_response.status_code, 404,
            msg="Expected response code is 404 and got is %s (%s)" % (
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
            RequestType.PUT, register_agent_url(agent_id=agent_id))
        register_agent_response_dict = register_agent_response.json()
        logging.info('test_register_agent_with_invalid_token')
        logging.info('Url is %s', register_agent_url(agent_id=agent_id))
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
