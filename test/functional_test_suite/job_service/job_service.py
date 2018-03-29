""" Functional Test cases for Job Service """
import logging
import unittest
import httplib
import time
from test.shared.rest_framework import RequestType, RestAPI, path
from test.functional_test_suite.common.config import SEED_JOB_URL
from test.functional_test_suite.common.config import seed_job_url
from test.functional_test_suite.common.config import user_action_url
from test.functional_test_suite.common.config import TEMP_KEY
from test.functional_test_suite.common.config import agent_action_url
from test.functional_test_suite.common.config import agent_task_url
from test.functional_test_suite.common.config import list_agent_tasks_url
from test.functional_test_suite.common.config import agent_details_url
from test.functional_test_suite.common.config import current_tickets_url
from test.functional_test_suite.common.config import update_ticket_url
from test.functional_test_suite.common.config import INVENTORY_SERVICE_URL
from test.functional_test_suite.common.config import CUSTOMER_PROFILE_URL
from test.functional_test_suite.common.config import list_system
from test.functional_test_suite.common.config import list_system_url
from test.functional_test_suite.common.config import AGENT_SERVICE_URL
from test.functional_test_suite.common.config import register_agent_url
from test.functional_test_suite.common.config import initialize_logger
from test.functional_test_suite.job_service.job_service_payloads import SeedJobServicePayload
from test.functional_test_suite.ticket_service.ticket_service_payloads import TicketServicePayload
from test.functional_test_suite.inventory_service.inventory_service_payloads import InventoryServicePayload
from test.functional_test_suite.agent_service.agent_service_payloads import AgentServicePayload

job_service_customer = RestAPI(utype='customer')
job_service_invalid = RestAPI(utype='invalid')
job_service_agent = RestAPI(utype='agent')
inventory_service = RestAPI(utype='sysops')
ticket_service = RestAPI(utype='sysops')
agent_service = RestAPI(utype='agent')
agent_service_sysops = RestAPI(utype='sysops')
initialize_logger(path + '/../../logs/job_service.log')

address_title = job_service_customer.request(
    RequestType.GET, CUSTOMER_PROFILE_URL).json()['shipping_addresses'][0]['title']
source_system_id = job_service_customer.request(
    RequestType.GET, list_system_url(list_system, system_type='source')).json()['systems'][0]['id']
target_system_id = job_service_customer.request(
    RequestType.GET, list_system_url(list_system, system_type='target')).json()['systems'][0]['siteId']

job_id = 0
ticket_id = 0
agent_id = 0
task_id = 0


class JobServiceTestCases(unittest.TestCase):
    """ Test cases of Job Service"""

    """ POST: Test cases to Creation of seed job """

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
            (address_title=address_title, source_system_id=TEMP_KEY, job_name='test 25'))
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
            (source_system_id=source_system_id, target_system_id=TEMP_KEY, job_name='test 26'))
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
            (address_title='address_title', job_name='test 27'))
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

        error_message = "source_system_id must be provided"

        # Create job without source system id
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (source_system_id='', job_name='test 29'))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_without_source_system_id')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(source_system_id=''))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_without_target_system_id(self):
        """ Testing the creation of seed_job without target_system_id """

        error_message = "target_system_id must be provided"

        # Create job without source system id
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (target_system_id='', job_name='test 30'))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_without_target_system_id')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(target_system_id=''))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_without_address_title(self):
        """ Testing the creation of seed_job without address_title """

        error_message = "address_title must be provided"

        # Create job without address title
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (address_title='', job_name='test 31'))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_without_address_title')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(address_title=''))
        logging.info('Response is %s', create_job_response.text)
        self.assertEquals(
            create_job_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                create_job_response.status_code,
                httplib.responses[create_job_response.status_code]))
        self.assertIn(
            error_message, create_job_response_dict['message'],
            msg="Expected %s in %s" %
                (error_message, create_job_response_dict['message']))
        logging.info('test case executed successfully')

    def test_create_job_without_max_data_size(self):
        """ Testing the creation of seed_job without max_data_size """

        error_message = "max_data_size must be provided"

        # Create job without max data size
        create_job_response = job_service_customer.request(
            RequestType.POST, SEED_JOB_URL,
            payload=SeedJobServicePayload().create_seed_job_payload
            (max_data_size='', job_name='test 32'))
        create_job_response_dict = create_job_response.json()
        logging.info('test_create_job_without_max_data_size')
        logging.info('Url is %s', SEED_JOB_URL)
        logging.info('Request is %s', SeedJobServicePayload().
                     create_seed_job_payload(max_data_size=''))
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
        """ Testing with invalid job_id to get the details of the seed job """

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
            job_update_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
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

    def test__agent__details_with_valid_agent_id(self):
        """ Testing with valid agent id to get the details of an agent """

        key = "agent_id"
        # Get the details of an agent with valid agent id
        agent_details_response = job_service_agent.request(
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

    def test_agent_task__list_with_valid_agent_id(self):
        """ Testing with the valid agent id to get the list agent tasks """

        global task_id

        # Get list agent tasks  with valid url
        list_agents_tasks_response = job_service_agent.request(
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

    def test_agent_task_details_with_valid_task_id(self):
        """ Testing with the valid task id to get the task details """

        # Get the agent task details with valid task id
        agent_task_details_response = job_service_customer.request(
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

    def test__agent__eregister_with_valid_agent_id(self):
        """ Testing with valid url to register an agent """

        expected_message = "Crane Agent is registered successfully."

        # Register an agent with valid agent id
        register_agent_response = agent_service.request(
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

    def test__agent__job_details_with_valid_job_id(self):
        """ Testing with the valid job_id to get the details of the seed job """

        time.sleep(30)

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
        logging.info('test case executed successfully')

    def test__agent__user_action_with__valid_job_id(self):
        """ Testing with the valid job_id to take an action on job by user """
        time.sleep(30)
        task_status = 'CREATED'

        # Action on job with valid job id
        user_action_response = job_service_customer.request(
            RequestType.PUT, user_action_url(
                job_id, action='test_conn_source'),
            payload=SeedJobServicePayload().system_credentials())
        user_action_response_dict = user_action_response.json()
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
        self.assertEquals(
            task_status, user_action_response_dict['task_status'],
            msg="Expected %s equals %s" % (
                task_status, user_action_response_dict['task_status']))

    def test_action_with_invalid_job_id(self):
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

    def test_zdelete_job_with_valid_job_id(self):
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
