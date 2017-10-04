import unittest

from common.payloads import AgentServicePayload
from common.rest_framework import *
from common.config import AGENT_SERVICE_URL

agent_rest_obj_admin = RestAPIHeader(utype='admin')
agent_rest_obj_agent = RestAPIHeader(utype='agent')
LIST_AGENT_TASK_URL = AGENT_SERVICE_URL + '/tasks'
REGISTER_AGENT_URL = AGENT_SERVICE_URL + '/register'


def update_agent_task_url(task_id):
    """ Url to update the agent task status """

    return '%s/%s' % (LIST_AGENT_TASK_URL, task_id)


def agent_details_url(agent_id):
    """ Get the details agent """

    return '%s/%s' % (AGENT_SERVICE_URL, agent_id)


class GetListAgentTestCases(unittest.TestCase):
    """ To get the list agents """

    def test_with_valid_url(self):
        """ Testing with the valid url to get the list agents """

        out = agent_rest_obj_admin.request(RequestType.GET, AGENT_SERVICE_URL)
        out_dict = out.json()
        self.assertEquals(out.status_code, 200)
        self.assertIn('agents', out_dict.keys())

    def test_with_invalid_url(self):
        """ Testing with the invalid url to get the list agents """

        out = agent_rest_obj_admin.request(RequestType.GET, AGENT_SERVICE_URL +
                                           '12')
        out_dict = out.json()
        self.assertEquals(out.status_code, 403)
        self.assertIn('message', out_dict.keys())


class GetListAgentTaskTestcases(unittest.TestCase):
    """ To get the list agent tasks """

    def test_with_valid_url(self):
        """ Testing with the valid url to get the list agent tasks """

        out = agent_rest_obj_agent.request(RequestType.GET, LIST_AGENT_TASK_URL)
        out_dict = out.json()
        print(LIST_AGENT_TASK_URL)
        self.assertEquals(out.status_code, 200)
        self.assertIn('tasks', out_dict.keys())

    def test_with_invalid_url(self):
        """ Testing with the invalid url to get the list agent tasks """

        out = agent_rest_obj_agent.request(RequestType.GET, LIST_AGENT_TASK_URL
                                           + 'asq')
        out_dict = out.json()
        message = "Resource with id tasksasq does not exists"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(message, out_dict['message'])


class UpdateAgentTaskStatusTestcases(unittest.TestCase):
    """ To update the agent task status """

    def test_with_valid_task_id(self):
        """ Testing with the valid task id to update the agent task status """

        out = agent_rest_obj_agent.request(RequestType.PUT,
                                           update_agent_task_url('task_id'),
                                           payload=AgentServicePayload().
                                           update_agent_task_status
                                           (status='update', message='updated'))
        self.assertEquals(out.status_code, 202)

    def test_with_invalid_task_id(self):
        """ Testing with the invalid task id to update the agent task status """

        out = agent_rest_obj_agent.request(RequestType.PUT,
                                           update_agent_task_url('task_id'),
                                           payload=AgentServicePayload().
                                           update_agent_task_status())
        out_dict = out.json()
        message = "status string of task is not recognized"
        self.assertEquals(out.status_code, 400)
        self.assertIn(message, out_dict['message'])

    def test_with_invalid_status(self):
        """ Testing with the invalid status to update the agent task status """

        out = agent_rest_obj_agent.request(RequestType.PUT,
                                           update_agent_task_url('task_id'),
                                           payload=AgentServicePayload().
                                           update_agent_task_status
                                           (status='sxniu!'))
        out_dict = out.json()
        message = "task is not recognized"
        self.assertEquals(out.status_code, 400)
        self.assertIn(message, out_dict['message'])

    def test_with_invalid_message(self):
        """ Testing with the invalid message to update the agent task status """

        out = agent_rest_obj_agent.request(RequestType.PUT,
                                           update_agent_task_url('task_id'),
                                           payload=AgentServicePayload().
                                           update_agent_task_status
                                           (message='d @! h'))
        out_dict = out.json()
        message = "status string of task is not recognized"
        self.assertEquals(out.status_code, 400)
        self.assertIn(message, out_dict['message'])

    def test_without_status(self):
        """ Testing without status to update the agent task status """

        out = agent_rest_obj_agent.request(RequestType.PUT,
                                           update_agent_task_url('task_id'),
                                           payload=AgentServicePayload().
                                           update_agent_task_status(status=''))
        out_dict = out.json()
        message = "task is not recognized "
        self.assertEquals(out.status_code, 400)
        self.assertIn(message, out_dict['message'])

    def test_without_message(self):
        """ Testing without message to update the agent task status """

        out = agent_rest_obj_agent.request(RequestType.PUT,
                                           update_agent_task_url('asdf'),
                                           payload=AgentServicePayload().
                                           update_agent_task_status(message=''))
        out_dict = out.json()
        message = "status string of task is not recognized"
        self.assertEquals(out.status_code, 400)
        self.assertIn(message, out_dict['message'])


class RegisterAgentTestcases(unittest.TestCase):
    """ Register an agent """

    def test_with_valid_url(self):
        """ Testing with valid url to register an agent """

        out = agent_rest_obj_agent.request(RequestType.PUT, REGISTER_AGENT_URL)
        self.assertEquals(out.status_code, 202)

    def test_with_invalid_url(self):
        """ Testing with invalid url to register an agent """

        out = agent_rest_obj_agent.request(RequestType.PUT, REGISTER_AGENT_URL +
                                           'as')
        out_dict = out.json()
        self.assertEquals(out.status_code, 403)
        self.assertIn('message', out_dict.keys())


class GetAgentTaskDetailsTestcases(unittest.TestCase):
    """ To get the agent task details """

    def test_with_valid_task_id(self):
        """ Testing with the valid task id to get the task details """

        out = agent_rest_obj_agent.request(RequestType.GET,
                                           update_agent_task_url('task_id'))
        self.assertEquals(out.status_code, 200)

    def test_with_invalid_task_id(self):
        """ Testing with the invalid task id to get the task details """

        out = agent_rest_obj_agent.request(RequestType.GET,
                                           update_agent_task_url('182d8s'))
        self.assertEquals(out.status_code, 401)


class GetAgentDetailsTestcases(unittest.TestCase):
    """ To get the details of an agent """

    def test_with_valid_agent_id(self):
        """ Testing with valid agent id to get the details of an agent """

        out = agent_rest_obj_agent.request(RequestType.GET, agent_details_url(
            '7d4dff18-fb0b-4be4-aeb0-a6e2c015cb99'))
        self.assertEquals(out.status_code, 200)

    def test_with_invalid_agent_id(self):
        """ Testing with invalid agent id to get the details of an agent """

        out = agent_rest_obj_agent.request(RequestType.GET,
                                           agent_details_url('agent_id'))
        out_dict = out.json()
        message = 'does not exists'
        self.assertEquals(out.status_code, 404)
        self.assertIn(message, out_dict['message'])

    def test_without_agent_id(self):
        """ Testing without agent id to get the details of an agent """

        out = agent_rest_obj_agent.request(RequestType.GET,
                                           agent_details_url(''))
        out_dict = out.json()
        message = "User is not authorized to perform this action"
        self.assertEquals(out.status_code, 401)
        self.assertIn(message, out_dict['message'])

if __name__ == '__main__':
    unittest.main()
