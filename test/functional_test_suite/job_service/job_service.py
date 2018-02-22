""" Functional Test cases for Job Service """
import logging
import unittest
import pytest
import httplib
from test.shared.rest_framework import RequestType, RestAPI, path
from test.functional_test_suite.job_service.job_service_payloads import SeedJobServicePayload
from test.functional_test_suite.common.config import SEED_JOB_URL,\
    seed_job_url, user_action_url, TEMP_KEY, agent_action_url, initialize_logger

job_service_customer = RestAPI(utype='customer')
job_service_sysops = RestAPI(utype='sysops')
job_service_invalid = RestAPI(utype='invalid')
job_service_agent = RestAPI(utype='agent')
initialize_logger(path + '/../../logs/job_service.log')

job_id = 0


class JobServiceTestCases(unittest.TestCase):
    """ Test cases of Job Service"""

    """ POST: Test cases to Creation of seed job """

    @pytest.mark.run(order=1)
    def test_create_job_with_valid_details(self):
        """ Create job with valid details """

        global job_id

        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload())
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

    def test_create_job_with_invalid_token(self):
        """ Testing the creation of seed_job with invalid token """

        error_message = "Unauthorized"

        # Create job with invalid source system
        create_job_response = job_service_invalid.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload())
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_with_invalid_token')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s',
                     SeedJobServicePayload().create_seed_job_payload())
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 401,
            msg="Expected code is 401 and got is %s (%s)" %
                (create_job_response.status_code,
                 httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_with_invalid_source_system_id(self):
        """ Testing the creation of seed_job with invalid source_system_id """

        error_message = "Failed to create Job as failed to fetch " \
                        "SOURCE_SYSTEM system %s" % TEMP_KEY

        # Create job with invalid source system
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (source_system_id=TEMP_KEY))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_with_invalid_source_system_id')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(source_system_id=TEMP_KEY))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" %
                (create_job_response.status_code,
                 httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_with_invalid_target_system_id(self):
        """ Testing the creation of seed_job with invalid target_system_id """

        error_message = "Failed to create Job as failed to " \
                        "fetch TARGET_SYSTEM system %s" % TEMP_KEY

        # Create job with invalid target system
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (target_system_id=TEMP_KEY))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_with_invalid_target_system_id')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(target_system_id=TEMP_KEY))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" %
                (create_job_response.status_code,
                 httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_with_invalid_address_title(self):
        """ Testing the creation of seed_job with invalid address_title """

        error_message = "Failed to create Job as failed to fetch address"

        # Create job with invalid address title
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (address_title='address_title'))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_with_invalid_address_title')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(address_title='address_title'))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_with_invalid_max_data_size(self):
        """ Testing the creation of seed_job with invalid max_data_size """

        error_message = "Data size can not be more than 60"

        # Create job with invalid max data size
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (max_data_size='100'))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_with_invalid_max_data_size')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(max_data_size='100'))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_without_source_system_id(self):
        """ Testing the creation of seed_job without source_system_id """

        error_message = "Failed to create Job as failed to fetch SOURCE_SYSTEM system "

        # Create job without source system id
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (source_system_id=''))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_without_source_system_id')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(source_system_id=''))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_without_target_system_id(self):
        """ Testing the creation of seed_job without target_system_id """

        error_message = "Failed to create Job as failed to fetch TARGET_SYSTEM system "

        # Create job without source system id
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (target_system_id=''))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_without_target_system_id')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(target_system_id=''))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_without_address_title(self):
        """ Testing the creation of seed_job without address_title """

        error_message = "Failed to create Job as failed to fetch address"

        # Create job without address title
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (address_title=''))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_without_address_title')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(address_title=''))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_without_max_data_size(self):
        """ Testing the creation of seed_job without max_data_size """

        error_message = "Internal server error"

        # Create job without max data size
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (max_data_size=''))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_without_max_data_size')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(max_data_size=''))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 500,
            msg="Expected code is 500 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    """ GET: Test cases to get the list of seed jobs """

    def test_list_seed_jobs_with_valid_url(self):
        """ Testing with the valid url to get the list of seed jobs """

        # Get list of seed jobs with valid url
        job_lists_response = job_service_customer.request(
            RequestType.GET, SEED_JOB_URL)
        logging.info('test_list_seed_jobs_with_valid_url')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Response is %s', job_lists_response.text)
        self.assertEquals(
            job_lists_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                job_lists_response.status_code,
                httplib.responses[job_lists_response.status_code]))
        self.assertIn(
            'jobs', job_lists_response.json().keys(),
            msg="Expected %s in %s" %
                ('jobs', job_lists_response.json().keys()))
        logging.info('test case executed successfully')

    def test_list_seed_job_with_invalid_token(self):
        """ Testing with the invalid url to get the list of seed jobs """

        expected_message = "Unauthorized"

        # Get list of seed jobs with invalid token
        job_lists_response = job_service_invalid.request(
            RequestType.GET, SEED_JOB_URL)
        job_lists_response_dict = job_lists_response.json()
        logging.info('test_list_seed_job_with_invalid_token')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Response is %s', job_lists_response.text)
        self.assertEquals(
            job_lists_response.status_code, 401,
            msg="Expected code is 401 and got is %s (%s)" %
                (job_lists_response.status_code,
                 httplib.responses[job_lists_response.status_code]))
        self.assertEquals(
            expected_message, job_lists_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, job_lists_response_dict['message']))
        logging.info('test case executed successfully')

    """ GET: Test cases to get the details of particular seed job """

    def test_job_details_with_valid_job_id(self):
        """ Testing with the valid job_id to get the details of the seed job """

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
        print "inside function"
        self.assertTrue(1,2)
        logging.info('test case executed successfully')

    def test_job_detail_with_invalid_job_id(self):
        """ Testing with the invalid job_id to get the details
        of the seed job """

        error_message = "Resource with id %s does not exists" % TEMP_KEY

        # Get the details of seed job with invalid job id
        job_details_response = job_service_customer.request(
            RequestType.GET, seed_job_url(TEMP_KEY))
        logging.info('test_job_detail_with_invalid_job_id')
        logging.info('Url is %s', seed_job_url(TEMP_KEY))
        logging.info('Response is %s', job_details_response.text)
        self.assertEquals(
            job_details_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                job_details_response.status_code,
                httplib.responses[job_details_response.status_code]))
        self.assertIn(
            error_message, job_details_response.json()['message'],
            msg="Expected %s in %s" %
                (error_message, job_details_response.json()['message']))
        logging.info('test case executed successfully')

    def test_job_detail_with_invalid_token(self):
        """ Testing with the invalid job_id to get the details
        of the seed job """

        error_message = "Unauthorized"

        # Get the details of seed job with invalid job id
        job_details_response = job_service_invalid.request(
            RequestType.GET, seed_job_url(job_id))
        logging.info('test_job_detail_with_invalid_token')
        logging.info('Url is %s', seed_job_url(job_id))
        logging.info('Response is %s', job_details_response.text)
        self.assertEquals(
            job_details_response.status_code, 401,
            msg="Expected code is 401 and got is %s (%s)" % (
                job_details_response.status_code,
                httplib.responses[job_details_response.status_code]))
        self.assertEquals(
            error_message, job_details_response.json()['message'],
            msg="Expected %s in %s" %
                (error_message, job_details_response.json()['message']))
        logging.info('test case executed successfully')

    """ PUT: Test cases to Update the seed job """

    def test_job_update_with_valid_job_id(self):
        """ Testing with the valid job_id to update the details of seed_job """

        # Update the seed job with valid job id

        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(job_id),
            payload=SeedJobServicePayload().update_seed_job_payload())
        logging.info('test_job_update_with_valid_job_id')
        logging.info('Url is %s', seed_job_url(job_id))
        logging.info('Request is %s', SeedJobServicePayload().
                     update_seed_job_payload())
        logging.info('Response is %s', job_update_response.text)
        self.assertEquals(
            job_update_response.status_code, 202,
            msg="Expected code is 202 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))
        logging.info('test case executed successfully')

    def test_job_update_with_invalid_job_id(self):
        """ Testing with the invalid job_id to update
        the details of seed_job """

        message = "Resource with id %s does not exists" % TEMP_KEY

        # Update the seed job with invalid job id
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(TEMP_KEY),
            payload=SeedJobServicePayload().update_seed_job_payload())
        job_update_response_dict = job_update_response.json()
        logging.info('test_job_update_with_invalid_job_id')
        logging.info('Url is %s', seed_job_url(TEMP_KEY))
        logging.info('Request is %s', SeedJobServicePayload().
                     update_seed_job_payload())
        logging.info('Response is %s', job_update_response.text)
        self.assertEquals(
            job_update_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))
        self.assertEquals(
            message, job_update_response_dict['message'],
            msg="Expected %s equals %s" %
                (message, job_update_response_dict['message']))
        logging.info('test case executed successfully')

    def test_job_update_with_invalid_token(self):
        """ Testing with invalid token to update the details of seed_job """

        expected_message = "Unauthorized"

        # Update the seed job without job id
        job_update_response = job_service_invalid.request(
            RequestType.PUT, seed_job_url(job_id),
            payload=SeedJobServicePayload().update_seed_job_payload())
        job_update_response_dict = job_update_response.json()
        logging.info('test_job_update_with_invalid_token')
        logging.info('Url is %s', seed_job_url(job_id))
        logging.info('Request is %s', SeedJobServicePayload().
                     update_seed_job_payload())
        logging.info('Response is %s', job_update_response.text)
        self.assertEquals(
            job_update_response.status_code, 401,
            msg="Expected code is 401 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))
        self.assertEquals(
            expected_message, job_update_response_dict['message'],
            msg="Expected %s in %s" %
                (expected_message, job_update_response_dict['message']))
        logging.info('test case executed successfully')

    """ PUT: Test cases As a user take an action on job """

    def test_action_with_valid_id(self):
        """ Testing with the valid job_id to take an action on job by user """

        # Action on job with valid job id
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(
                job_id, action='test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        logging.info('test_action_with_valid_id')
        logging.info('Url is %s', user_action_url(
            job_id, action='test_conn_source'))
        logging.info('Request is %s', SeedJobServicePayload().
                     system_credentials())
        logging.info('Response is %s', user_action_response.text)
        self.assertEquals(
            user_action_response.status_code, 202,
            msg="Expected code is 202 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))
        logging.info('test case executed successfully')

    def test_action_with_invalid_id(self):
        """ Testing with the invalid job_id to take an action on job by user """

        message = "Resource with id %s does not exists" % TEMP_KEY

        # Action on job with valid job id
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(
                TEMP_KEY, action='test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        user_action_response_dict = user_action_response.json()
        logging.info('test_action_with_invalid_id')
        logging.info('Url is %s', user_action_url(
            TEMP_KEY, action='test_conn_source'))
        logging.info('Request is %s',
                     SeedJobServicePayload().system_credentials())
        logging.info('Response is %s', user_action_response.text)
        self.assertEquals(
            user_action_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))
        self.assertEquals(
            message, user_action_response_dict['message'],
            msg="Expected %s in %s" %
                (message, user_action_response_dict['message']))
        logging.info('test case executed successfully')

    def test_action_with_invalid_token(self):
        """ Testing without job_id to take an action on job by user """

        expected_message = "Unauthorized"

        # Action on job without job id
        user_action_response = job_service_invalid.request(
            RequestType.PUT, user_action_url(job_id, action='test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        user_action_response_dict = user_action_response.json()
        logging.info('test_action_with_invalid_token')
        logging.info('Url is %s', user_action_url(
            job_id, action='test_conn_source'))
        logging.info('Request is %s', SeedJobServicePayload().
                     system_credentials())
        logging.info('Response is %s', user_action_response.text)
        self.assertEquals(
            user_action_response.status_code, 401,
            msg="Expected code is 401 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))
        self.assertEquals(
            expected_message, user_action_response_dict['message'],
            msg="Expected %s in %s" %
                (expected_message, user_action_response_dict['message']))
        logging.info('test case executed successfully')

        # PATCH: take action by an agent
    """ PATCH: Method Test cases to take an action by an agent on job """

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

    def test_agent_action_with_invalid_job_id(self):
        """ Testing with invalid job_id to take an action on job by an agent """

        message = "Resource with id %s does not exists" % TEMP_KEY

        # Agent action with invalid job id
        agent_action_response = job_service_agent.request(
            RequestType.PATCH,
            agent_action_url(job_id=TEMP_KEY,
                             action='test_conn_source_success'),
            payload=SeedJobServicePayload().update_job_logs())
        agent_action_response_dict = agent_action_response.json()
        logging.info('test_agent_action_with_invalid_job_id')
        logging.info('Url is %s', agent_action_url(
            job_id=TEMP_KEY, action='test_conn_source_success'))
        logging.info('Request is %s', SeedJobServicePayload().update_job_logs())
        logging.info('Response is %s', agent_action_response.text)
        self.assertEquals(
            agent_action_response.status_code, 503,
            msg="Expected code is 503 and got is %s (%s)" %
                (agent_action_response.status_code,
                 httplib.responses[agent_action_response.status_code]))
        self.assertEquals(
            message, agent_action_response_dict['message'],
            msg="Expected %s in %s" %
                (message, agent_action_response_dict['message']))
        logging.info('test case executed successfully')

    def test_agent_action_without_source_objects(self):
        """ Testing without source objects to take an
        action on job by an agent """

        message = "for action test_conn_source_success db objects required"
        # Agent action without source objects
        agent_action_response = job_service_agent.request(
            RequestType.PATCH,
            agent_action_url(job_id=job_id,
                             action='test_conn_source_success'),
            payload=SeedJobServicePayload().update_job_logs(source_objects={}))
        agent_action_response_dict = agent_action_response.json()
        logging.info('test_agent_action_without_source_objects')
        logging.info('Url is %s', agent_action_url(
            job_id=job_id, action='test_conn_source_success'))
        logging.info('Request is %s', SeedJobServicePayload().
                     update_job_logs(source_objects={}))
        logging.info('Response is %s', agent_action_response.text)
        self.assertEquals(
            agent_action_response.status_code, 503,
            msg="Expected code is 503 and got is %s (%s)" % (
                agent_action_response.status_code,
                httplib.responses[agent_action_response.status_code]))
        self.assertEquals(
            message, agent_action_response_dict['message'],
            msg="Expected %s in %s" %
                (message, agent_action_response_dict['message']))
        logging.info('test case executed successfully')

    """ DELETE: Delete the seed job with job id"""

    @pytest.mark.last
    def test_delete_job_with_valid_job_id(self):
        """ Testing with the valid job_id to delete seed_job """

        message = "Seed Job is deleted"
        # Delete the seed job with valid job id
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(job_id))
        job_delete_response_dict = job_delete_response.json()
        logging.info('test_delete_job_with_valid_job_id')
        logging.info('Url is %s', seed_job_url(job_id))
        logging.info('Response is %s', job_delete_response.text)
        self.assertEquals(
            job_delete_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                job_delete_response.status_code,
                httplib.responses[job_delete_response.status_code]))
        self.assertEquals(
            message, job_delete_response_dict['message'],
            msg="Expected %s in %s" %
                (message, job_delete_response_dict['message']))
        logging.info('test case executed successfully')

    def test_delete_job_with_invalid_job_id(self):
        """ Testing with the invalid job_id to delete seed_job """

        error_message = "Resource with id %s does not exists" % TEMP_KEY

        # Delete the seed job with invalid job id
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(TEMP_KEY))
        job_delete_response_dict = job_delete_response.json()
        logging.info('test_delete_job_with_invalid_job_id')
        logging.info('Url is %s', seed_job_url(TEMP_KEY))
        logging.info('Response is %s', job_delete_response.text)
        self.assertEquals(
            job_delete_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                job_delete_response.status_code,
                httplib.responses[job_delete_response.status_code]))
        self.assertEquals(
            error_message, job_delete_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, job_delete_response_dict['message']))
        logging.info('test case executed successfully')

    def test_delete_job_with_invalid_token(self):
        """ Testing with the invalid job_id to delete seed_job """

        error_message = "Unauthorized"

        # Delete the seed job with invalid job id
        job_delete_response = job_service_invalid.request(
            RequestType.DELETE, seed_job_url(job_id))
        job_delete_response_dict = job_delete_response.json()
        logging.info('test_delete_job_with_invalid_token')
        logging.info('Url is %s', seed_job_url(job_id))
        logging.info('Response is %s', job_delete_response.text)
        self.assertEquals(
            job_delete_response.status_code, 401,
            msg="Expected code is 401 and got is %s (%s)" % (
                job_delete_response.status_code,
                httplib.responses[job_delete_response.status_code]))
        self.assertEquals(
            error_message, job_delete_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, job_delete_response_dict['message']))
        logging.info('test case executed successfully')
