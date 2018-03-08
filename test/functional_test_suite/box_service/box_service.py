import logging
import unittest
import httplib
from test.shared.rest_framework import RequestType, RestAPI, path
from test.functional_test_suite.common.config import BOX_SERVICE_URL, \
    initialize_logger, box_action_url, get_box_url
from test.functional_test_suite.box_service.box_service_payloads import BoxServicePayloads

box_service = RestAPI(utype='sysops')
box_service_invalid_token = RestAPI(utype='invalid')
box_service_agent = RestAPI(utype='agent')
job_id = "a55313f1-4810-452c-b920-db62b24dc90b"
initialize_logger(path + "/../../logs/box_service.log")


class BoxServiceTestCases(unittest.TestCase):
    """ test cases for box service """

    """ GET: test cases """

    def test_get_box_details_with_valid_job_id(self):
        """ test cases for get method """

        box_service_response = box_service.request(
            RequestType.GET, get_box_url(job_id))
        box_service_response_dict = box_service_response.json()
        logging.info('test_get_box_details_with_valid_id')
        logging.info('Url is %s', BOX_SERVICE_URL)
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 200,
            msg='Expected code is 200 and got is %s (%s)' %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
        self.assertIn(
            'boxes', box_service_response_dict.keys(),
            msg="%s in %s" % ('boxes', box_service_response_dict.keys()))
        logging.info('test case executed successfully')

    def test_get_box_details_with_invalid_token(self):
        """ testing with invalid token to get box details """

        expected_message = 'Unauthorized'

        box_service_response = box_service_invalid_token.request(
            RequestType.GET, get_box_url(job_id=job_id))
        box_service_response_dict = box_service_response.json()
        logging.info('test_get_box_details_with_invalid_token')
        logging.info('Url is %s', BOX_SERVICE_URL)
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 401,
            msg="Expected 401 and got is %s (%s)" %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
        self.assertEquals(
            expected_message, box_service_response_dict['message'],
            msg="Expected message %s is equals to %s" %
                (expected_message, box_service_response_dict['message']))
        logging.info('test case executed successfully')

    def test_get_box_details_with_invalid_job_id(self):
        """ testing with invalid token to get box details """

        expected_message = "No results found"

        box_service_response = box_service.request(
            RequestType.GET, get_box_url(job_id='1234'))
        box_service_response_dict = box_service_response.json()
        logging.info('test_get_box_details_with_invalid_token')
        logging.info('Url is %s', BOX_SERVICE_URL)
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 200,
            msg="Expected 200 and got is %s (%s)" %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
        self.assertEquals(
            expected_message, box_service_response_dict['message'],
            msg="Expected message %s is equals to %s" %
                (expected_message, box_service_response_dict['message']))
        logging.info('test case executed successfully')

    """ PUT: test cases """

    def test_update_box_with_valid_details(self):
        """ testing with valid details to update the box """
        box_service_response = box_service_agent.request(
            RequestType.PUT, BOX_SERVICE_URL,
            payload=BoxServicePayloads().update_box_payload())
        logging.info('test_update_box_with_valid_details')
        logging.info('Url is %s', BOX_SERVICE_URL)
        logging.info('Request is %s', BoxServicePayloads().update_box_payload())
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
        logging.info('test case executed successfully')

    def test_update_box_with_invalid_details(self):
        """ testing with valid details to update the box """
        box_service_response = box_service_agent.request(
            RequestType.PUT, BOX_SERVICE_URL,
            payload=BoxServicePayloads().update_box_payload(customer_id='1234'))
        logging.info('test_update_box_with_invalid_details')
        logging.info('Url is %s', BOX_SERVICE_URL)
        logging.info('Request is %s',
                     BoxServicePayloads().update_box_payload(
                         customer_id='1234'))
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
        logging.info('test case executed successfully')

    def test_update_box_with_invalid_token(self):
        """ testing with valid details to update the box """

        expected_message = 'Unauthorized'

        box_service_response = box_service_invalid_token.request(
            RequestType.PUT, BOX_SERVICE_URL,
            payload=BoxServicePayloads().update_box_payload())
        box_service_response_dict = box_service_response.json()
        logging.info('test_update_box_with_invalid_details')
        logging.info('Url is %s', BOX_SERVICE_URL)
        logging.info('Request is %s',
                     BoxServicePayloads().
                     update_box_payload(customer_id='asjhc'))
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 401,
            msg='Expected 401 and got %s (%s)' %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
        self.assertEquals(
            expected_message, box_service_response_dict['message'],
            msg="Expected %s equals %s" % (
                expected_message, box_service_response_dict['message']))
        logging.info('test case executed successfully')

    """ PATCH: test cases """

    def test_action_on_box_with_valid_box_id(self):
        """ test cases for get method """

        box_service_response = box_service_agent.request(
            RequestType.PATCH,
            box_action_url(box_id='1234'),
            payload=BoxServicePayloads().action_box_payload())
        logging.info('test_action_on_box_with_valid_box_id')
        logging.info('Url is %s', box_action_url(box_id='1234'))
        logging.info('Request is %s', BoxServicePayloads().action_box_payload())
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 200,
            msg='Expected code is 200 and got is %s (%s)' %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
        logging.info('test case executed successfully')

    def test_action_on_box_with_invalid_token(self):
        """ testing action on box with invalid token """

        expected_message = 'Unauthorized'

        box_service_response = box_service_invalid_token.request(
            RequestType.PATCH,
            box_action_url(box_id='1234'),
            payload=BoxServicePayloads().action_box_payload())
        box_service_response_dict = box_service_response.json()
        logging.info('test_action_on_box_with_invalid_token')
        logging.info('Url is %s', box_action_url(box_id='1234'))
        logging.info('Request is %s', BoxServicePayloads().action_box_payload())
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 401,
            msg="Expected 401 and got is %s (%s)" %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
        self.assertEquals(
            expected_message, box_service_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, box_service_response_dict['message']))
        logging.info('test case executed successfully')

    def test_action_on_box_with_invalid_box_id(self):

        box_service_response = box_service_agent.request(
            RequestType.PATCH,
            box_action_url(box_id='xyz'),
            payload=BoxServicePayloads().action_box_payload())
        logging.info('test_action_on_box_with_invalid_box_id')
        logging.info('Url is %s', box_action_url(box_id='xyz'))
        logging.info('Request is %s',
                     BoxServicePayloads().action_box_payload())
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 404,
            msg="Expected 404 and got is %s (%s)" %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
        logging.info('test case executed successfully')
