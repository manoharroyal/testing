""" Functional Test cases for Job Service """

import unittest
from common.payloads import SeedJobServicePayload
from common.rest_framework import RestAPIHeader
from common.helper_function import RequestType
from common.config import SEED_JOB_URL, INVALID_SEED_JOB_URL, SEED_JOB_ID, \
    seed_job_url, user_action_url, TEMP_KEY, DELETE_JOB_ID, admin_action_url, \
    agent_api_url, update_job_logs_url


job_service = RestAPIHeader()
job_service_admin = RestAPIHeader(utype='admin')
job_service_agent = RestAPIHeader(utype='agent')


class CreateJob(unittest.TestCase):
    """ Test cases to Creation of seed job """

    def test_with_valid_details(self):
        """ Testing the creation of seed_job with all valid details """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload())
        expected_dict = SeedJobServicePayload().expected_payload()
        out_dict = out.json()
        self.assertEquals(out.status_code, 403)
        self.assertIn(out_dict.keys, expected_dict.keys)

    def test_with_invalid_source_system_id(self):
        """ Testing the creation of seed_job with invalid source_system_id """

        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload
                                  (source_system_id=TEMP_KEY))
        out_dict = out.json()
        error_message = "Failed to create Job as failed to fetch system"
        self.assertEquals(out.status_code, 403)
        self.assertIn(error_message, out_dict['message'])

    def test_with_invalid_target_system_id(self):
        """ Testing the creation of seed_job with invalid target_system_id """

        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload
                                  (target_system_id=TEMP_KEY))
        out_dict = out.json()
        error_message = "Failed to create Job as failed to fetch system"
        self.assertEquals(out.status_code, 403)
        self.assertIn(error_message, out_dict['message'])

    def test_with_invalid_address_title(self):
        """ Testing the creation of seed_job with invalid address_title """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload
                                  (address_title='address_title'))
        out_dict = out.json()
        message = "Failed to create Job as " \
                  "failed to fetch address address_title"
        self.assertEquals(out.status_code, 403)
        self.assertIn(message, out_dict['message'])

    def test_with_invalid_max_data_size(self):
        """ Testing the creation of seed_job with invalid max_data_size """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload
                                  (max_data_size='-100'))
        self.assertEquals(out.status_code, 403)

    def test_with_empty_seed_job_name(self):
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload(seed_job_name=''))
        out_dict = out.json()
        error_message = "Job name must be provided"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_empty_job_type(self):
        """ Testing the creation of seed_job without job_type """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload(job_type=''))
        out_dict = out.json()
        error_message = "Job type must be provided"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_empty_source_system_id(self):
        """ Testing the creation of seed_job without source_system_id """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload(source_system_id=''))
        out_dict = out.json()
        error_message = "Source System Id should be present"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_empty_target_system_id(self):
        """ Testing the creation of seed_job without target_system_id """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload(target_system_id=''))
        out_dict = out.json()
        error_message = "Target System Id should be present"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_empty_address_title(self):
        """ Testing the creation of seed_job without address_title """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload(address_title=''))
        out_dict = out.json()
        error_message = "Address Title should be present"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_empty_description(self):
        """ Testing the creation of seed_job without description """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload(description=''))
        out_dict = out.json()
        error_message = "Job description must be provided"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_empty_max_data_size(self):
        """ Testing the creation of seed_job without max_data_size """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload(max_data_size=''))
        out_dict = out.json()
        error_message = "Data Size must be provided"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_email_id(self):
        """ Testing the creation of seed_job without email_id """

        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload(email_id=''))
        self.assertEquals(out.status_code, 400)

    def test_without_optional_email_id(self):
        """ Testing the creation of seed_job without optional_email_id """
        out = job_service.request(RequestType.POST, SEED_JOB_URL,
                                  payload=SeedJobServicePayload().
                                  create_seed_job_payload(optional_email_id=''))
        expected_dict = SeedJobServicePayload().expected_payload()
        out_dict = out.json()
        self.assertEquals(out.status_code, 201)
        self.assertItemsEqual(out_dict, expected_dict)


class GetListSeedJobsTestcases(unittest.TestCase):
    """ Test cases to get the list of seed jobs """

    def test_with_valid_url(self):
        """ Testing with the valid url to get the list of seed jobs """
        out = job_service.request(RequestType.GET, SEED_JOB_URL)
        self.assertEquals(out.status_code, 200)
        self.assertIn('jobs', out.json().keys())

    def test_with_invalid_url(self):
        """ Testing with the invalid url to get the list of seed jobs """
        out = job_service.request(RequestType.GET, INVALID_SEED_JOB_URL)
        self.assertEquals(out.status_code, 404)
        self.assertIn('message', out.json().keys())


class GetDetailsSeedJobTestcases(unittest.TestCase):
    """ Test cases to get the details of particular seed job"""

    def test_with_valid_job_id(self):
        """ Testing with the valid job_id to get the details of the seed job """
        out = job_service.request(RequestType.GET,
                                  seed_job_url(SEED_JOB_ID))
        self.assertEquals(out.status_code, 200)
        self.assertIn('timeline_status', out.json().keys())

    def test_with_invalid_job_id(self):
        """ Testing with the invalid job_id to get the details
        of the seed job """
        out = job_service.request(RequestType.GET, seed_job_url(TEMP_KEY))
        message = "Seed Job does not exists"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out.json()['message'], message)

    def test_without_job_id(self):
        """ Testing with the invalid job_id to get the details
        of the seed job """
        out = job_service.request(RequestType.GET, seed_job_url(''))
        message = "Seed Job does not exists"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out.json()['message'], message)


class UpdateSeedJob(unittest.TestCase):
    """ Test cases to Update the seed job """

    def test_with_valid_job_id(self):
        """ Testing with the valid job_id to update the details of seed_job """
        out = job_service.request(RequestType.PUT,
                                  seed_job_url(SEED_JOB_ID),
                                  payload=SeedJobServicePayload().
                                  update_seed_job_payload())
        self.assertEquals(out.status_code, 202)

    def test_with_invalid_job_id(self):
        """ Testing with the invalid job_id to update
        the details of seed_job """
        out = job_service.request(RequestType.PUT,
                                  seed_job_url(TEMP_KEY),
                                  payload=SeedJobServicePayload().
                                  update_seed_job_payload())
        self.assertEquals(out.status_code, 404)

    def test_without_job_id(self):
        """ Testing without job_id to update the details of seed_job """
        out = job_service.request(RequestType.PUT, seed_job_url(''),
                                  payload=SeedJobServicePayload().
                                  update_seed_job_payload())
        self.assertEquals(out.status_code, 403)

    def test_with_invalid_source_system_id(self):
        """ Testing with invalid source_system_id to
        update the details of seed_job """
        out = job_service.request(RequestType.PUT,
                                  seed_job_url(SEED_JOB_ID),
                                  payload=SeedJobServicePayload().
                                  update_seed_job_payload
                                  (source_system_id='26xv762 @'))
        self.assertEquals(out.status_code, 400)

    def test_with_invalid_target_system_id(self):
        """ Testing with the invalid target_system_id to
        update the details of seed_job """
        out = job_service.request(RequestType.PUT,
                                  seed_job_url(SEED_JOB_ID),
                                  payload=SeedJobServicePayload().
                                  update_seed_job_payload
                                  (target_system_id="dvwy27@"))
        self.assertEquals(out.status_code, 400)


class SeedJobDeleteTestcases(unittest.TestCase):
    """ Delete the seed job with job id"""

    def test_with_valid_job_id(self):
        """ Testing with the valid job_id to delete seed_job """
        out = job_service.request(RequestType.DELETE,
                                  seed_job_url(DELETE_JOB_ID))
        out_dict = out.json()
        message = "Seed Job is deleted"
        self.assertEquals(out.status_code, 200)
        self.assertEquals(out_dict['message'], message)

    def test_with_invalid_job_id(self):
        """ Testing with the invalid job_id to delete seed_job """
        out = job_service.request(RequestType.DELETE, seed_job_url(TEMP_KEY))
        out_dict = out.json()
        error_message = "does not exists"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_job_id(self):
        """ Testing without job_id to delete seed_job """
        out = job_service.request(RequestType.DELETE, seed_job_url(''))
        out_dict = out.json()
        self.assertEquals(out.status_code, 403)
        self.assertIn('message', out_dict.keys())


class TakeActionJobTestCases(unittest.TestCase):
    """ Test cases As a user take an action on job """

    def test_with_valid_id(self):
        """ Testing with the valid job_id to take an action on job by user """
        out = job_service.request(RequestType.PUT,
                                  user_action_url(SEED_JOB_ID,
                                                  'test_conn_source'),
                                  payload=SeedJobServicePayload().
                                  system_credentials())
        self.assertEquals(out.status_code, 202)

    def test_with_invalid_id(self):
        """ Testing with the invalid job_id to take an action on job by user """
        out = job_service.request(RequestType.PUT,
                                  user_action_url(TEMP_KEY, 'test_conn_source'),
                                  payload=SeedJobServicePayload().
                                  system_credentials)
        out_dict = out.json()
        message = "Resource with id ee5ca93d-a60f-4" \
                  "655-9bde-9fad3304cb0f12 does not exists"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out_dict['message'], message)

    def test_with_empty_id(self):
        """ Testing without job_id to take an action on job by user """
        out = job_service.request(RequestType.PUT,
                                  user_action_url('', 'test_conn_source'),
                                  payload=SeedJobServicePayload().
                                  system_credentials())
        out_dict = out.json()
        message = "Failed to get item :" \
                  "One or more parameter values were invalid: " \
                  "An AttributeValue may not contain an empty string"
        self.assertEquals(out.status_code, 403)
        self.assertEquals(out_dict['message'], message)

    def test_with_incorrect_db_user_name(self):
        """ Testing with incorrect database user name to
        take an action on job by user """
        out = job_service.request(RequestType.PUT,
                                  user_action_url(SEED_JOB_ID,
                                                  'test_conn_source'),
                                  payload=SeedJobServicePayload().
                                  system_credentials(db_user_name='dbc1'))
        out_dict = out.json()
        message = "action test_conn_source can not be performed on job " \
                  "ee5ca93d-a60f-4655-9bde-9fad3304cb0f as Box is " \
                  "still not connected to Network"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_with_incorrect_db_password(self):
        """ Testing with incorrect database password to take
        an action on job by user """
        out = job_service.request(RequestType.PUT,
                                  user_action_url(SEED_JOB_ID,
                                                  'test_conn_source'),
                                  payload=SeedJobServicePayload().
                                  system_credentials(db_user_password='dbc123'))
        out_dict = out.json()
        message = "action test_conn_source can not be performed on job " \
                  "ee5ca93d-a60f-4655-9bde-9fad3304cb0f as Box is still " \
                  "not connected to Network"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)


class ApproveSeedJobTestCases(unittest.TestCase):
    """ Test cases for the Admin has approve the action given by user """

    def test_with_valid_details(self):
        """ Testing with valid details to approve the seed job by admin """
        out = job_service_admin.request(RequestType.PUT,
                                        admin_action_url(SEED_JOB_ID,
                                                         'approve'),
                                        payload=SeedJobServicePayload().
                                        approve_payload())
        self.assertEquals(out.status_code, 200)

    def test_with_invalid_jobid(self):
        """ Testing with invalid job_id to approve the seedjob by admin """
        out = job_service_admin.request(RequestType.PUT,
                                        admin_action_url(TEMP_KEY, 'approve'),
                                        payload=SeedJobServicePayload().
                                        approve_payload())
        out_dict = out.json()
        message = "does not exists"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out_dict['message'], message)

    def test_with_empty_jobid(self):
        """ Testing without job_id to approve the seedjob by admin """
        out = job_service_admin.request(RequestType.PUT,
                                        admin_action_url('', 'approve'),
                                        payload=SeedJobServicePayload().
                                        approve_payload())
        out_dict = out.json()
        message = "User is not authorized to perform this action"
        self.assertEquals(out.status_code, 401)
        self.assertEquals(out_dict['message'], message)


class AgentActionJobTestCases(unittest.TestCase):
    """ PATCH Method Test cases to take an action by an agent on job """

    def test_with_valid_job_id(self):
        """ Testing with valid job_id to take an action on job by an agent """
        out = job_service_agent.request(RequestType.PATCH,
                                        agent_api_url
                                        (SEED_JOB_ID,
                                         'test_conn_source_success'),
                                        payload=SeedJobServicePayload().
                                        update_job_logs())
        self.assertEquals(out.status_code, 200)

    def test_with_invalid_job_id(self):
        """ Testing with invalid job_id to take an action on job by an agent """
        out = job_service_agent.request(RequestType.PATCH,
                                        agent_api_url
                                        (TEMP_KEY, 'test_conn_source_success'),
                                        payload=SeedJobServicePayload().
                                        update_job_logs())
        out_dict = out.json()
        message = "Resource with id 1d4986d3-b2d8-41ed-865c-" \
                  "13ad524335c3123 does not exists"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out_dict['message'], message)

    def test_without_source_objects(self):
        """ Testing without source objects to take an
        action on job by an agent """
        out = job_service_agent.request(RequestType.PATCH,
                                        agent_api_url
                                        (SEED_JOB_ID,
                                         'test_conn_source_success'),
                                        payload=SeedJobServicePayload().
                                        update_job_logs(source_objects={}))
        out_dict = out.json()
        message = "for action test_conn_source_success db objects required"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)


class UpdateJobLogsTestCases(unittest.TestCase):
    """ PUT method Test cases to update the job logs """

    def test_with_valid_job_id(self):
        """ Testing with the valid job_id to update the job logs """
        out = job_service_agent.request(RequestType.PUT,
                                        update_job_logs_url(SEED_JOB_ID),
                                        payload=SeedJobServicePayload().
                                        update_job_logs())
        out_dict = out.json()
        message = "Job Log updated"
        self.assertEquals(out.status_code, 202)
        self.assertEquals(out_dict['message'], message)

    def test_with_invalid_job_id(self):
        """ Testing with the invalid job_id to update the job logs """
        out = job_service_agent.request(RequestType.PUT,
                                        update_job_logs_url(TEMP_KEY),
                                        payload=SeedJobServicePayload().
                                        update_job_logs())
        self.assertEquals(out.status_code, 403)

if __name__ == '__main__':
    unittest.main()
