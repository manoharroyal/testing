import unittest
import httplib
from test.shared.rest_framework import RequestType, RestAPIHeader
from test.functional_test_suit.common.payloads import SeedJobServicePayload
from test.functional_test_suit.common.config import SEED_JOB_URL, \
    INVALID_SEED_JOB_URL, SEED_JOB_ID, seed_job_url, user_action_url, \
    TEMP_KEY, DELETE_JOB_ID, agent_api_url

job_service_customer = RestAPIHeader(utype='customer')
job_service_sysops = RestAPIHeader(utype='sysops')
job_service_agent = RestAPIHeader(utype='agent')


class JobServiceTestCases(unittest.TestCase):
    """ Test cases to Creation of seed job """

    def test_create_job_with_valid_details(self):
        """ Testing the creation of seed_job with all valid details """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload())
        create_job_response_dict = create_job_response.json()
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 201,
            msg="Expected code is 201 and got is %s (%s)" %
                (create_job_response.status_code,
                 httplib.responses[create_job_response.status_code]))
        self.assertIn(
            'job_id', create_job_response_dict.keys(),
            msg="Expected %s in %s" %
                ('job_id', create_job_response_dict.keys()))

    def test_create_job_with_invalid_source_system_id(self):
        """ Testing the creation of seed_job with invalid source_system_id """

        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (source_system_id=TEMP_KEY))
        create_job_response_dict = create_job_response.json()
        error_message = "Failed to create Job as failed to fetch system"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" %
                (create_job_response.status_code,
                 httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_with_invalid_target_system_id(self):
        """ Testing the creation of seed_job with invalid target_system_id """

        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (target_system_id=TEMP_KEY))
        create_job_response_dict = create_job_response.json()
        error_message = "Failed to create Job as failed to fetch system"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" %
                (create_job_response.status_code,
                 httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_with_invalid_address_title(self):
        """ Testing the creation of seed_job with invalid address_title """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (address_title='address_title'))
        create_job_response_dict = create_job_response.json()
        error_message = "Failed to create Job as " \
                        "failed to fetch address address_title"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_with_invalid_max_data_size(self):
        """ Testing the creation of seed_job with invalid max_data_size """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (max_data_size='-100'))
        create_job_response_dict = create_job_response.json()
        error_message = "Failed to create Job as " \
                        "failed to fetch address address_title"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_seed_job_name(self):
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (seed_job_name=''))
        create_job_response_dict = create_job_response.json()
        error_message = "Job name must be provided"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            create_job_response_dict['message'], error_message,
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_job_type(self):
        """ Testing the creation of seed_job without job_type """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (job_type=''))
        create_job_response_dict = create_job_response.json()
        error_message = "Job type must be provided"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            create_job_response_dict['message'], error_message,
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_source_system_id(self):
        """ Testing the creation of seed_job without source_system_id """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (source_system_id=''))
        create_job_response_dict = create_job_response.json()
        error_message = "Source System Id should be present"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            create_job_response_dict['message'], error_message,
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_target_system_id(self):
        """ Testing the creation of seed_job without target_system_id """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (target_system_id=''))
        create_job_response_dict = create_job_response.json()
        error_message = "Target System Id should be present"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            create_job_response_dict['message'], error_message,
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_with_empty_address_title(self):
        """ Testing the creation of seed_job without address_title """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (address_title=''))
        create_job_response_dict = create_job_response.json()
        error_message = "Address Title should be present"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            create_job_response_dict['message'], error_message,
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_with_empty_description(self):
        """ Testing the creation of seed_job without description """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (description=''))
        create_job_response_dict = create_job_response.json()
        error_message = "Job description must be provided"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            create_job_response_dict['message'], error_message,
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_with_empty_max_data_size(self):
        """ Testing the creation of seed_job without max_data_size """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (max_data_size=''))
        create_job_response_dict = create_job_response.json()
        error_message = "Data Size must be provided"
        print "Expected is", error_message
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            create_job_response_dict['message'], error_message,
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_email_id(self):
        """ Testing the creation of seed_job without email_id """

        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (email_id=''))
        expected_dict = SeedJobServicePayload().expected_payload()
        create_job_response_dict = create_job_response.json()
        print "Expected is", expected_dict
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertItemsEqual(
            create_job_response_dict, expected_dict,
            msg="Expected %s in %s" %
                (expected_dict, create_job_response_dict['message']))

    def test_create_job_without_optional_email_id(self):
        """ Testing the creation of seed_job without optional_email_id """
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (optional_email_id=''))
        expected_dict = SeedJobServicePayload().expected_payload()
        create_job_response_dict = create_job_response.json()
        print "Expected is", expected_dict
        print "Response is", create_job_response
        self.assertEquals(
            create_job_response.status_code, 201,
            msg="Expected code is 201 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn('job_id', create_job_response_dict.keys(),
            msg="Expected %s in %s" % (
            'job_id', create_job_response_dict.keys()))


        # GET: get list of seed jobs
    """ Test cases to get the list of seed jobs """

    def test_list_seed_jobs_with_valid_url(self):
        """ Testing with the valid url to get the list of seed jobs """
        job_lists_response = job_service_customer.request(
            RequestType.GET, SEED_JOB_URL)
        print "Response is", job_lists_response
        self.assertEquals(
            job_lists_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                job_lists_response.status_code,
                httplib.responses[job_lists_response.status_code]))
        self.assertIn(
            'jobs', job_lists_response.json().keys(),
            msg="Expected %s in %s" %
                ('jobs', job_lists_response.json().keys()))

    def test_list_seed_job_with_invalid_url(self):
        """ Testing with the invalid url to get the list of seed jobs """
        job_lists_response = job_service_customer.request(
            RequestType.GET, INVALID_SEED_JOB_URL)
        print "Response is", job_lists_response
        self.assertEquals(
            job_lists_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" %
                (job_lists_response.status_code,
                 httplib.responses[job_lists_response.status_code]))
        self.assertIn(
            'message', job_lists_response.json().keys(),
            msg="Expected %s in %s" %
                ('message', job_lists_response.json().keys()))

    # GET: get the details of job
    """ Test cases to get the details of particular seed job"""

    def test_job_details_with_valid_job_id(self):
        """ Testing with the valid job_id to get the details of the seed job """
        job_details_response = job_service_customer.request(
            RequestType.GET, seed_job_url(SEED_JOB_ID))
        print "Response is", job_details_response
        self.assertEquals(
            job_details_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                job_details_response.status_code,
                httplib.responses[job_details_response.status_code]))
        self.assertIn(
            'timeline_status', job_details_response.json().keys(),
            msg="Expected %s in %s" %
                ('timeline_status', job_details_response.json().keys()))

    def test_job_detail_with_invalid_job_id(self):
        """ Testing with the invalid job_id to get the details
        of the seed job """
        job_details_response = job_service_customer.request(
            RequestType.GET, seed_job_url(TEMP_KEY))
        error_message = "Seed Job does not exists"
        print "Expected is", error_message
        print "Response is", job_details_response
        self.assertEquals(
            job_details_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                job_details_response.status_code,
                httplib.responses[job_details_response.status_code]))
        self.assertEquals(
            job_details_response.json()['message'], error_message,
            msg="Expected %s in %s" % (error_message,
                                       job_details_response.json()['message']))

    # PUT: update the job
    """ Test cases to Update the seed job """

    def test_job_update_with_valid_job_id(self):
        """ Testing with the valid job_id to update the details of seed_job """
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(SEED_JOB_ID),
            payload=SeedJobServicePayload().update_seed_job_payload())
        print "Response is", job_update_response
        self.assertEquals(
            job_update_response.status_code, 202,
            msg="Expected code is 202 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))

    def test_job_update_with_invalid_job_id(self):
        """ Testing with the invalid job_id to update
        the details of seed_job """
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(TEMP_KEY),
            payload=SeedJobServicePayload().update_seed_job_payload())
        job_update_response_dict = job_update_response.json()
        message = "Resource with id %s does not exists" % TEMP_KEY
        print "Expected is", message
        print "Response is", job_update_response
        self.assertEquals(
            job_update_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))
        self.assertEquals(
            job_update_response_dict['message'], message,
            msg="Expected %s equals %s" %
                (job_update_response_dict['message'], message))

    def test_job_update_without_job_id(self):
        """ Testing without job_id to update the details of seed_job """
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(''),
            payload=SeedJobServicePayload().update_seed_job_payload())
        job_update_response_dict = job_update_response.json()
        print "Response is", job_update_response
        self.assertEquals(
            job_update_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))
        self.assertIn(
            'message', job_update_response_dict.keys(),
            msg="Expected %s in %s" %
                ('message', job_update_response_dict.keys()))

    def test_job_update_with_invalid_source_system_id(self):
        """ Testing with invalid source_system_id to
        update the details of seed_job """
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(SEED_JOB_ID),
            payload=SeedJobServicePayload().update_seed_job_payload
            (source_system_id='26xv762 @'))
        job_update_response_dict = job_update_response.json()
        print "Response is", job_update_response
        self.assertEquals(
            job_update_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))
        self.assertIn('message', job_update_response_dict.keys(),
            msg="Expected %s in %s" % (
            'message', job_update_response_dict.keys()))

    def test_job_update_with_invalid_target_system_id(self):
        """ Testing with the invalid target_system_id to
        update the details of seed_job """
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(SEED_JOB_ID),
            payload=SeedJobServicePayload().update_seed_job_payload
            (target_system_id="dvwy27@"))
        job_update_response_dict = job_update_response.json()
        print "Response is", job_update_response
        self.assertEquals(
            job_update_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))
        self.assertIn('message', job_update_response_dict.keys(),
            msg="Expected %s in %s" % (
            'message', job_update_response_dict.keys()))

    # DELETE: delete the job
    """ Delete the seed job with job id"""

    def test_delete_job_with_valid_job_id(self):
        """ Testing with the valid job_id to delete seed_job """
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(DELETE_JOB_ID))
        job_delete_response_dict = job_delete_response.json()
        message = "Seed Job is deleted"
        print "Expected is", message
        print "Response is", job_delete_response
        self.assertEquals(
            job_delete_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                job_delete_response.status_code,
                httplib.responses[job_delete_response.status_code]))
        self.assertEquals(
            job_delete_response_dict['message'], message,
            msg="Expected %s in %s" %
                (message, job_delete_response_dict['message']))

    def test_delete_job_with_invalid_job_id(self):
        """ Testing with the invalid job_id to delete seed_job """
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(TEMP_KEY))
        job_delete_response_dict = job_delete_response.json()
        error_message = "Resource with id %s does not exists" % TEMP_KEY
        print "Expected is", error_message
        print "Response is", job_delete_response
        self.assertEquals(
            job_delete_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                job_delete_response.status_code,
                httplib.responses[job_delete_response.status_code]))
        self.assertEquals(
            job_delete_response_dict['message'], error_message,
            msg="Expected %s in %s" %
                (error_message, job_delete_response_dict['message']))

    def test_delete_job_without_job_id(self):
        """ Testing without job_id to delete seed_job """
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(''))
        job_delete_response_dict = job_delete_response.json()
        print "Response is", job_delete_response
        self.assertEquals(
            job_delete_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" % (
                job_delete_response.status_code,
                httplib.responses[job_delete_response.status_code]))
        self.assertIn(
            'message', job_delete_response_dict.keys(),
            msg="Expected %s in %s" %
                ('message', job_delete_response_dict.keys()))

    def test_delete_job_with_deleted_job_id(self):
        """ Testing without job_id to delete seed_job """
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(DELETE_JOB_ID))
        job_delete_response_dict = job_delete_response.json()
        message = "Resource with id %s does not exists" % DELETE_JOB_ID
        print "Expected is", message
        print "Response is", job_delete_response
        self.assertEquals(job_delete_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                    job_delete_response.status_code,
                    httplib.responses[job_delete_response.status_code]))
        self.assertEquals(
            message, job_delete_response_dict['message'],
            msg="Expected %s and got is %s" %
                (message, job_delete_response_dict['message']))

    # PUT : take an action on job by user
    """ Test cases As a user take an action on job """

    def test_action_with_valid_id(self):
        """ Testing with the valid job_id to take an action on job by user """
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(SEED_JOB_ID, 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        print "Response is", user_action_response
        self.assertEquals(
            user_action_response.status_code, 202,
            msg="Expected code is 202 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))

    def test_action_with_invalid_id(self):
        """ Testing with the invalid job_id to take an action on job by user """
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(TEMP_KEY, 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        user_action_response_dict = user_action_response.json()
        print (user_action_url(TEMP_KEY, 'test_conn_source'))
        message = "Resource with id %s does not exists" % TEMP_KEY
        print "Expected is", message
        print "Response is", user_action_response
        self.assertEquals(
            user_action_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))
        self.assertEquals(
            user_action_response_dict['message'], message,
            msg="Expected %s in %s" %
                (message, user_action_response_dict['message']))

    def test_action_with_empty_id(self):
        """ Testing without job_id to take an action on job by user """
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url('', 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        user_action_response_dict = user_action_response.json()
        message = "Failed to get item :" \
                  "One or more parameter values were invalid: " \
                  "An AttributeValue may not contain an empty string"
        print "Expected is", message
        print "Response is", user_action_response
        self.assertEquals(
            user_action_response.status_code, 500,
            msg="Expected code is 500 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))
        self.assertEquals(
            user_action_response_dict['message'], message,
            msg="Expected %s in %s" %
                (message, user_action_response_dict['message']))

    def test_action_with_incorrect_db_user_name(self):
        """ Testing with incorrect database user name to
        take an action on job by user """
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(SEED_JOB_ID, 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials
            (db_user_name='dbc1'))
        user_action_response_dict = user_action_response.json()
        print user_action_response
        self.assertEquals(
            user_action_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))
        self.assertIn(
            'message', user_action_response_dict.keys(),
            msg="Expected %s in %s" %
                ('message', user_action_response_dict.keys()))

    def test_action_with_incorrect_db_password(self):
        """ Testing with incorrect database password to take
        an action on job by user """
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(SEED_JOB_ID, 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials
            (db_user_password='dbc123'))
        user_action_response_dict = user_action_response.json()
        print user_action_response
        self.assertEquals(
            user_action_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))
        self.assertIn('message', user_action_response_dict.keys(),
            msg="Expected %s in %s" % (
            'message', user_action_response_dict.keys()))

        # # PATCH: take action by an agent
    """ PATCH Method Test cases to take an action by an agent on job """

    def test_agent_action_with_valid_job_id(self):
        """ Testing with valid job_id to take an action on job by an agent """
        agent_action_response = job_service_agent.request(
            RequestType.PATCH, agent_api_url(SEED_JOB_ID,
                                             'test_conn_source_success'),
            payload=SeedJobServicePayload().update_job_logs())
        print agent_action_response
        self.assertEquals(
            agent_action_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                agent_action_response.status_code,
                httplib.responses[agent_action_response.status_code]))

    def test_agent_action_with_invalid_job_id(self):
        """ Testing with invalid job_id to take an action on job by an agent """
        agent_action_response = job_service_agent.request(
            RequestType.PATCH, agent_api_url(TEMP_KEY,
                                             'test_conn_source_success'),
            payload=SeedJobServicePayload().update_job_logs())
        agent_action_response_dict = agent_action_response.json()
        message = "Resource with id 1d4986d3-b2d8-41ed-865c-" \
                  "13ad524335c3123 does not exists"
        print "Expected is", message
        print "Response is", agent_action_response
        self.assertEquals(
            agent_action_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" %
                (agent_action_response.status_code,
                 httplib.responses[agent_action_response.status_code]))
        self.assertEquals(
            agent_action_response_dict['message'], message,
            msg="Expected %s in %s" %
                (message, agent_action_response_dict['message']))

    def test_agent_action_without_source_objects(self):
        """ Testing without source objects to take an
        action on job by an agent """
        agent_action_response = job_service_agent.request(
            RequestType.PATCH, agent_api_url(SEED_JOB_ID,
                                             'test_conn_source_success'),
            payload=SeedJobServicePayload().update_job_logs(source_objects={}))
        agent_action_response_dict = agent_action_response.json()
        message = "for action test_conn_source_success db objects required"
        print "Expected is", message
        print "Response is", agent_action_response
        self.assertEquals(
            agent_action_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                agent_action_response.status_code,
                httplib.responses[agent_action_response.status_code]))
        self.assertEquals(
            agent_action_response_dict['message'], message,
            msg="Expected %s in %s" %
                (message, agent_action_response_dict['message']))
