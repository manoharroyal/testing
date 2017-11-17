""" Functional Test cases for Job Service """

import unittest2
import httplib
from test.shared.rest_framework import RequestType, RestAPIHeader
from test.functional_test_suit.common.payloads import SeedJobServicePayload
from test.functional_test_suit.common.config import SEED_JOB_URL, \
    INVALID_SEED_JOB_URL, SEED_JOB_ID, seed_job_url, user_action_url, \
    TEMP_KEY, DELETE_JOB_ID, agent_api_url

job_service_customer = RestAPIHeader(utype='customer')
job_service_sysops = RestAPIHeader(utype='sysops')
job_service_agent = RestAPIHeader(utype='agent')


class JobServiceTestCases(unittest2.TestCase):
    """ Test cases to Creation of seed job """

    def test_create_job_with_valid_details(self):
        """ Testing the creation of seed_job with all valid details """

        # Create job with all valid details
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload())
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
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

        error_message = "Failed to create Job as failed to fetch system"

        # Create job with invalid source system
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (source_system_id=TEMP_KEY))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
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

        error_message = "Failed to create Job as failed to fetch system"

        # Create job with invalid target system
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (target_system_id=TEMP_KEY))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
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

        error_message = "Failed to create Job as " \
                        "failed to fetch address address_title"

        # Create job with invalid address title
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (address_title='address_title'))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
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

        error_message = "Failed to create Job as " \
                        "failed to fetch address address_title"

        # Create job with invalid max data size
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (max_data_size='-100'))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
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
        """ Testing the creation of seed_job without seed job name """

        error_message = "Job name must be provided"

        # Create job without seed job name
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (seed_job_name=''))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_job_type(self):
        """ Testing the creation of seed_job without job_type """

        error_message = "Job type must be provided"

        # Create job without job type
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (job_type=''))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_source_system_id(self):
        """ Testing the creation of seed_job without source_system_id """

        error_message = "Source System Id should be present"

        # Create job without source system id
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (source_system_id=''))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_target_system_id(self):
        """ Testing the creation of seed_job without target_system_id """

        error_message = "Target System Id should be present"

        # Create job without source system id
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (target_system_id=''))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_address_title(self):
        """ Testing the creation of seed_job without address_title """

        error_message = "Address Title should be present"

        # Create job without address title
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (address_title=''))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_description(self):
        """ Testing the creation of seed_job without description """

        error_message = "Job description must be provided"

        # Create job without description
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (description=''))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_max_data_size(self):
        """ Testing the creation of seed_job without max_data_size """

        error_message = "Data Size must be provided"

        # Create job without max data size
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (max_data_size=''))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertEquals(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))

    def test_create_job_without_email_id(self):
        """ Testing the creation of seed_job without email_id """

        expected_dict = SeedJobServicePayload().expected_payload()

        # Create job without email id
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (email_id=''))
        create_job_response_dict = create_job_response.json()
        print "Response while creating: ", create_job_response.text
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertItemsEqual(
            expected_dict, create_job_response_dict,
            msg="Expected %s in %s" %
                (expected_dict, create_job_response_dict))

    def test_create_job_without_optional_email_id(self):
        """ Testing the creation of seed_job without optional_email_id """

        # create job without optional email id
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (optional_email_id=''))
        create_job_response_dict = create_job_response.json()
        print "Response is: ", create_job_response.text
        self.assertEquals(
            create_job_response.status_code, 201,
            msg="Expected code is 201 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn('job_id', create_job_response_dict.keys(),
            msg="Expected %s in %s" % (
            'job_id', create_job_response_dict.keys()))

    """ Test cases to get the list of seed jobs """

    def test_list_seed_jobs_with_valid_url(self):
        """ Testing with the valid url to get the list of seed jobs """

        # Get list of seed jobs with valid url
        job_lists_response = job_service_customer.request(
            RequestType.GET, SEED_JOB_URL)
        print "Response is: ", job_lists_response.text
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

        # Get list of seed jobs with invalid url
        job_lists_response = job_service_customer.request(
            RequestType.GET, INVALID_SEED_JOB_URL)
        print "Response is: ", job_lists_response.text
        self.assertEquals(
            job_lists_response.status_code, 403,
            msg="Expected code is 403 and got is %s (%s)" %
                (job_lists_response.status_code,
                 httplib.responses[job_lists_response.status_code]))
        self.assertIn(
            'message', job_lists_response.json().keys(),
            msg="Expected %s in %s" %
                ('message', job_lists_response.json().keys()))

    """ Test cases to get the details of particular seed job"""

    def test_job_details_with_valid_job_id(self):
        """ Testing with the valid job_id to get the details of the seed job """

        # Get the seed job details with valid job id
        job_details_response = job_service_customer.request(
            RequestType.GET, seed_job_url(SEED_JOB_ID))
        print "Response is: ", job_details_response.text
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

        error_message = "Seed Job does not exists"

        # Get the details of seed job with invalid job id
        job_details_response = job_service_customer.request(
            RequestType.GET, seed_job_url(TEMP_KEY))
        print "Response is: ", job_details_response.text
        self.assertEquals(
            job_details_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                job_details_response.status_code,
                httplib.responses[job_details_response.status_code]))
        self.assertEquals(
            error_message, job_details_response.json()['message'],
            msg="Expected %s in %s" %
                (error_message, job_details_response.json()['message']))

    """ Test cases to Update the seed job """

    def test_job_update_with_valid_job_id(self):
        """ Testing with the valid job_id to update the details of seed_job """

        # Update the seed job with valid job id
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(SEED_JOB_ID),
            payload=SeedJobServicePayload().update_seed_job_payload())
        print "Response is: ", job_update_response.text
        self.assertEquals(
            job_update_response.status_code, 202,
            msg="Expected code is 202 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))

    def test_job_update_with_invalid_job_id(self):
        """ Testing with the invalid job_id to update
        the details of seed_job """

        message = "Resource with id %s does not exists" % TEMP_KEY

        # Update the seed job with invalid job id
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(TEMP_KEY),
            payload=SeedJobServicePayload().update_seed_job_payload())
        job_update_response_dict = job_update_response.json()
        print "Response is: ", job_update_response.text
        self.assertEquals(
            job_update_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                job_update_response.status_code,
                httplib.responses[job_update_response.status_code]))
        self.assertEquals(
            message, job_update_response_dict['message'],
            msg="Expected %s equals %s" %
                (message, job_update_response_dict['message']))

    def test_job_update_without_job_id(self):
        """ Testing without job_id to update the details of seed_job """

        # Update the seed job without job id
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(''),
            payload=SeedJobServicePayload().update_seed_job_payload())
        job_update_response_dict = job_update_response.json()
        print "Response is: ", job_update_response.text
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

        # Update the seed job with invalid source system id
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(SEED_JOB_ID),
            payload=SeedJobServicePayload().update_seed_job_payload
            (source_system_id='26xv762 @'))
        job_update_response_dict = job_update_response.json()
        print "Response is: ", job_update_response.text
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

        # Update the seed job with invalid target system id
        job_update_response = job_service_customer.request(
            RequestType.PUT, seed_job_url(SEED_JOB_ID),
            payload=SeedJobServicePayload().update_seed_job_payload
            (target_system_id="dvwy27@"))
        job_update_response_dict = job_update_response.json()
        print "Response is: ", job_update_response.text
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

        message = "Seed Job is deleted"

        # Delete the seed job with valid job id
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(DELETE_JOB_ID))
        job_delete_response_dict = job_delete_response.json()
        print "Response is: ", job_delete_response.text
        self.assertEquals(
            job_delete_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                job_delete_response.status_code,
                httplib.responses[job_delete_response.status_code]))
        self.assertEquals(
            message, job_delete_response_dict['message'],
            msg="Expected %s in %s" %
                (message, job_delete_response_dict['message']))

    def test_delete_job_with_invalid_job_id(self):
        """ Testing with the invalid job_id to delete seed_job """

        error_message = "Resource with id %s does not exists" % TEMP_KEY

        # Delete the seed job with invalid job id
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(TEMP_KEY))
        job_delete_response_dict = job_delete_response.json()
        print "Response is: ", job_delete_response.text
        self.assertEquals(
            job_delete_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                job_delete_response.status_code,
                httplib.responses[job_delete_response.status_code]))
        self.assertEquals(
            error_message, job_delete_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, job_delete_response_dict['message']))

    def test_delete_job_without_job_id(self):
        """ Testing without job_id to delete seed_job """

        # Delete the seed job without job id
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(''))
        job_delete_response_dict = job_delete_response.json()
        print "Response is: ", job_delete_response.text
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

        message = "Resource with id %s does not exists" % DELETE_JOB_ID

        # Delete the seed job with deleted job id
        job_delete_response = job_service_customer.request(
            RequestType.DELETE, seed_job_url(DELETE_JOB_ID))
        job_delete_response_dict = job_delete_response.json()
        print "Response is: ", job_delete_response.text
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

        # Action on job with valid job id
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(SEED_JOB_ID, 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        print "Response is: ", user_action_response.text
        self.assertEquals(
            user_action_response.status_code, 202,
            msg="Expected code is 202 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))

    def test_action_with_invalid_id(self):
        """ Testing with the invalid job_id to take an action on job by user """

        message = "Resource with id %s does not exists" % TEMP_KEY

        # Action on job with valid job id
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(TEMP_KEY, 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        user_action_response_dict = user_action_response.json()
        print "Response is: ", user_action_response.text
        self.assertEquals(
            user_action_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))
        self.assertEquals(
            message, user_action_response_dict['message'],
            msg="Expected %s in %s" %
                (message, user_action_response_dict['message']))

    def test_action_without_job__id(self):
        """ Testing without job_id to take an action on job by user """

        message = "Failed to get item :" \
                  "One or more parameter values were invalid: " \
                  "An AttributeValue may not contain an empty string"

        # Action on job without job id
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url('', 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        user_action_response_dict = user_action_response.json()
        print "Response is: ", user_action_response.text
        self.assertEquals(
            user_action_response.status_code, 500,
            msg="Expected code is 500 and got is %s (%s)" % (
                user_action_response.status_code,
                httplib.responses[user_action_response.status_code]))
        self.assertEquals(
            message, user_action_response_dict['message'],
            msg="Expected %s in %s" %
                (message, user_action_response_dict['message']))

    def test_action_with_incorrect_db_user_name(self):
        """ Testing with incorrect database user name to
        take an action on job by user """

        # Action on job with incorrect database user name
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(SEED_JOB_ID, 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials
            (db_user_name='dbc1'))
        user_action_response_dict = user_action_response.json()
        print "Response is: ", user_action_response.text
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

        # Action on job with incorrect database password
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(SEED_JOB_ID, 'test_conn_source'),
            payload=SeedJobServicePayload().system_credentials
            (db_user_password='dbc123'))
        user_action_response_dict = user_action_response.json()
        print "Response is: ", user_action_response.text
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

        # Agent action with valid job id
        agent_action_response = job_service_agent.request(
            RequestType.PATCH, agent_api_url(SEED_JOB_ID,
                                             'test_conn_source_success'),
            payload=SeedJobServicePayload().update_job_logs())
        print "Response is: ", agent_action_response.text
        self.assertEquals(
            agent_action_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                agent_action_response.status_code,
                httplib.responses[agent_action_response.status_code]))

    def test_agent_action_with_invalid_job_id(self):
        """ Testing with invalid job_id to take an action on job by an agent """

        message = "Resource with id %s does not exists" % TEMP_KEY

        # Agent action with invalid job id
        agent_action_response = job_service_agent.request(
            RequestType.PATCH, agent_api_url(TEMP_KEY,
                                             'test_conn_source_success'),
            payload=SeedJobServicePayload().update_job_logs())
        agent_action_response_dict = agent_action_response.json()
        print "Response is: ", agent_action_response.text
        self.assertEquals(
            agent_action_response.status_code, 404,
            msg="Expected code is 404 and got is %s (%s)" %
                (agent_action_response.status_code,
                 httplib.responses[agent_action_response.status_code]))
        self.assertEquals(
            message, agent_action_response_dict['message'],
            msg="Expected %s in %s" %
                (message, agent_action_response_dict['message']))

    def test_agent_action_without_source_objects(self):
        """ Testing without source objects to take an
        action on job by an agent """

        message = "for action test_conn_source_success db objects required"

        # Agent action without source objects
        agent_action_response = job_service_agent.request(
            RequestType.PATCH, agent_api_url(SEED_JOB_ID,
                                             'test_conn_source_success'),
            payload=SeedJobServicePayload().update_job_logs(source_objects={}))
        agent_action_response_dict = agent_action_response.json()
        print "Response is: ", agent_action_response.text
        self.assertEquals(
            agent_action_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                agent_action_response.status_code,
                httplib.responses[agent_action_response.status_code]))
        self.assertEquals(
            message, agent_action_response_dict['message'],
            msg="Expected %s in %s" %
                (message, agent_action_response_dict['message']))
