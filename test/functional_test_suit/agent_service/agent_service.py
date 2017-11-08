""" Functional Test cases for Agent Service """
import unittest
import httplib
from test.functional_test_suit.common.payloads import \
    AgentServicePayload
from test.shared.rest_framework import RestAPIHeader, \
    RequestType
from test.functional_test_suit.common.config import \
    AGENT_SERVICE_URL, LIST_AGENT_TASK_URL, \
    REGISTER_AGENT_URL, update_agent_task_url, agent_details_url

agent_service = RestAPIHeader()


class AgentServiceTestCases(unittest.TestCase):
    """ Test cases to get the list agents """

    def test_list_agents_with_valid_url(self):
        """ Testing with the valid url to get the list agents """
        list_agents_response = agent_service.request(
            RequestType.GET, AGENT_SERVICE_URL)
        list_agents_response_dict = list_agents_response.json()
        self.assertEquals(
            list_agents_response.status_code, 200,
            msg="Expected response code is 200 and got is %s (%s)" % (
                list_agents_response.status_code,
                httplib.responses[list_agents_response.status_code]))
        self.assertIn('agents', list_agents_response_dict.keys(),
                      msg="Expected %s in and got is %s" % (
                          'message', list_agents_response_dict.keys()))

    def test_list_agent_with_invalid_url(self):
        """ Testing with the invalid url to get the list agents """
        list_agents_response = agent_service.request(
            RequestType.GET, AGENT_SERVICE_URL + '12')
        list_agents_response_dict = list_agents_response.json()
        self.assertEquals(
            list_agents_response.status_code, 403,
            msg="Expected response code is 403 and got is %s (%s)" % (
                list_agents_response.status_code,
                httplib.responses[list_agents_response.status_code]))
        self.assertIn('message', list_agents_response_dict.keys(),
                      msg="Expected %s in and got is %s" % (
                          'message', list_agents_response_dict.keys()))

    # GET: To get list agent tasks
    """ Test cases to get the list agent tasks """

    def test_list_agent_tasks_with_valid_url(self):
        """ Testing with the valid url to get the list agent tasks """
        list_agents_tasks_response = agent_service.request(
            RequestType.GET, LIST_AGENT_TASK_URL)
        list_agents_tasks_response_dict = list_agents_tasks_response.json()
        self.assertEquals(
            list_agents_tasks_response.status_code, 200,
            msg="Expected response code is 200 and got is %s (%s)" % (
                list_agents_tasks_response.status_code,
                httplib.responses[list_agents_tasks_response.status_code]))
        self.assertIn('tasks', list_agents_tasks_response_dict.keys(),
                      msg="Expected %s in and got is %s" % (
                          'message', list_agents_tasks_response_dict.keys()))

    def test_list_agent_tasks_with_invalid_url(self):
        """ Testing with the invalid url to get the list agent tasks """
        list_agents_response = agent_service.request(
            RequestType.GET, LIST_AGENT_TASK_URL + 'asq')
        list_agents_tasks_response_dict = list_agents_response.json()
        message = "Resource with id tasksasq does not exists"
        self.assertEquals(
            list_agents_response.status_code, 404,
            msg="Expected response code is 404 and got is %s (%s)" % (
                list_agents_response.status_code,
                httplib.responses[list_agents_response.status_code]))
        self.assertEquals(message, list_agents_tasks_response_dict['message'],
                          msg="Expected %s in and got is %s" % (
                          'message', list_agents_tasks_response_dict.keys()))

    # PUT: Update agent task status
    """ Test cases to update the agent task status """

    def test_update_agent_task_with_valid_task_id(self):
        """ Testing with the valid task id to update the agent task status """
        update_agent_task_response = agent_service.request(
            RequestType.PUT, update_agent_task_url('task_id'),
            payload=AgentServicePayload().update_agent_task_status(
                status='update', message='updated'))
        self.assertEquals(
            update_agent_task_response.status_code, 202,
            msg="Expected response code is 202 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))

    def test_update_agent_task_with_invalid_task_id(self):
        """ Testing with the invalid task id to update the agent task status """
        update_agent_task_response = agent_service.request(
            RequestType.PUT, update_agent_task_url('task_id'),
            payload=AgentServicePayload().update_agent_task_status())
        update_agent_task_response_dict = update_agent_task_response.json()
        expected_message = "status string of task is not recognized"
        self.assertEquals(
            update_agent_task_response.status_code, 400,
            msg="Expected response code is 400 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        self.assertIn(
            expected_message, update_agent_task_response_dict['message'],
            msg="Expected message is %s and got %s" %
                (update_agent_task_response_dict['message'], expected_message))

    def test_update_agent_task_with_invalid_status(self):
        """ Testing with the invalid status to update the agent task status """
        update_agent_task_response = agent_service.request(
            RequestType.PUT, update_agent_task_url('task_id'),
            payload=AgentServicePayload().update_agent_task_status(status='su'))
        update_agent_task_response_dict = update_agent_task_response.json()
        expected_message = "task is not recognized"
        self.assertEquals(
            update_agent_task_response.status_code, 400,
            msg="Expected response code is 400 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        self.assertIn(
            expected_message, update_agent_task_response_dict['message'],
            msg="Expected message is %s and got %s" %
                (update_agent_task_response_dict['message'], expected_message))

    def test_update_agent_task_with_invalid_message(self):
        """ Testing with the invalid message to update the agent task status """
        update_agent_task_response = agent_service.request(
            RequestType.PUT, update_agent_task_url('task_id'),
            payload=AgentServicePayload().update_agent_task_status(
                message='dh'))
        update_agent_task_response_dict = update_agent_task_response.json()
        expected_message = "status string of task is not recognized"
        self.assertEquals(
            update_agent_task_response.status_code, 400,
            msg="Expected response code is 400 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        self.assertIn(
            expected_message, update_agent_task_response_dict['message'],
            msg="Expected message is %s and got %s" %
                (update_agent_task_response_dict['message'], expected_message))

    def test_update_agent_task_without_status(self):
        """ Testing without status to update the agent task status """
        update_agent_task_response = agent_service.request(
            RequestType.PUT, update_agent_task_url('task_id'),
            payload=AgentServicePayload().update_agent_task_status(status=''))
        update_agent_task_response_dict = update_agent_task_response.json()
        expected_message = "task is not recognized "
        self.assertEquals(
            update_agent_task_response.status_code, 400,
            msg="Expected response code is 400 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        self.assertIn(
            expected_message, update_agent_task_response_dict['message'],
            msg="Expected message is %s and got %s" %
                (update_agent_task_response_dict['message'], expected_message))

    def test_update_agent_task_without_message(self):
        """ Testing without message to update the agent task status """
        update_agent_task_response = agent_service.request(
            RequestType.PUT, update_agent_task_url('asdf'),
            payload=AgentServicePayload().update_agent_task_status(message=''))
        update_agent_task_response_dict = update_agent_task_response.json()
        expected_message = "status string of task is not recognized"
        self.assertEquals(
            update_agent_task_response.status_code, 400,
            msg="Expected response code is 400 and got is %s (%s)" % (
                update_agent_task_response.status_code,
                httplib.responses[update_agent_task_response.status_code]))
        self.assertIn(
            expected_message, update_agent_task_response_dict['message'],
            msg="Expected message is %s and got %s" %
                (update_agent_task_response_dict['message'], expected_message))

    # PUT: Register an agent
    """ Test cases to Register an agent by passing input parameters """

    def test_register_agent_with_valid_url(self):
        """ Testing with valid url to register an agent """
        register_agent_response = agent_service.request(
            RequestType.PUT, REGISTER_AGENT_URL)
        self.assertEquals(
            register_agent_response.status_code, 202,
            msg="Expected response code is 202 and got is %s (%s)" % (
                register_agent_response.status_code,
                httplib.responses[register_agent_response.status_code]))

    def test_register_agent_with_invalid_url(self):
        """ Testing with invalid url to register an agent """
        register_agent_response = agent_service.request(
            RequestType.PUT, REGISTER_AGENT_URL + 'as')
        register_agent_response_dict = register_agent_response.json()
        self.assertEquals(
            register_agent_response.status_code, 403,
            msg="Expected response code is 403 and got is %s (%s)" % (
                register_agent_response.status_code,
                httplib.responses[register_agent_response.status_code]))
        self.assertIn(
            'message', register_agent_response_dict.keys(),
            msg="Expected %s in %s" %
                ('message', register_agent_response_dict.keys()))

    # GET: Get the agent task details
    """ To get the agent task details """

    def test_agent_task_details_with_valid_task_id(self):
        """ Testing with the valid task id to get the task details """
        agent_task_details_response = agent_service.request(
            RequestType.GET, update_agent_task_url('task_id'))
        self.assertEquals(
            agent_task_details_response.status_code, 200,
            msg="Expected response code is 200 and got is %s (%s)" % (
                agent_task_details_response.status_code,
                httplib.responses[agent_task_details_response.status_code]))

    def test_agent_task_details_with_invalid_task_id(self):
        """ Testing with the invalid task id to get the task details """
        agent_task_details_response = agent_service.request(
            RequestType.GET, update_agent_task_url('182d8s'))
        self.assertEquals(
            agent_task_details_response.status_code, 401,
            msg="Expected response code is 401 and got is %s" %
                httplib.responses[agent_task_details_response.status_code])

    # GET: Get the details of an agent
    """ To get the details of an agent """

    def test_agent_details_with_valid_agent_id(self):
        """ Testing with valid agent id to get the details of an agent """
        agent_details_response = agent_service.request(
            RequestType.GET, agent_details_url(
                '7d4dff18-fb0b-4be4-aeb0-a6e2c015cb99'))
        self.assertEquals(
            agent_details_response.status_code, 200,
            msg="Expected response code is 200 and got is %s (%s)" % (
                agent_details_response.status_code,
                httplib.responses[agent_details_response.status_code]))

    def test_agent_details_with_invalid_agent_id(self):
        """ Testing with invalid agent id to get the details of an agent """
        agent_details_response = agent_service.request(
            RequestType.GET, agent_details_url('agent_id'))
        agent_details_response_dict = agent_details_response.json()
        expected_message = 'does not exists'
        self.assertEquals(
            agent_details_response.status_code, 404,
            msg="Expected response code is 404 and got is %s (%s)" % (
                agent_details_response.status_code,
                httplib.responses[agent_details_response.status_code]))
        self.assertIn(
            expected_message, agent_details_response_dict['message'],
            msg="Expected %s in %s" %
                (expected_message, agent_details_response_dict['message']))

    def test_agent_details_without_agent_id(self):
        """ Testing without agent id to get the details of an agent """
        agent_details_response = agent_service.request(
            RequestType.GET, agent_details_url(''))
        agent_details_response_dict = agent_details_response.json()
        expected_message = "User is not authorized to perform this action"
        self.assertEquals(
            agent_details_response.status_code, 401,
            msg="Expected response code is 401 and got is %s (%s)" % (
                agent_details_response.status_code,
                httplib.responses[agent_details_response.status_code]))
        self.assertIn(
            expected_message, agent_details_response_dict['message'],
            msg="Expected %s in %s" %
                (expected_message, agent_details_response_dict['message']))
