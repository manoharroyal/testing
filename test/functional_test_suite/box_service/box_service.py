import httplib
import logging
import unittest
from test.shared.rest_framework import RequestType, RestAPI, path
from test.functional_test_suite.common.config import BOX_SERVICE_URL, \
    initialize_logger, box_details_url
from test.functional_test_suite.box_service.box_service_payloads import BoxServicePayloads
box_service = RestAPI(utype='sysops')
box_service_invalid_token = RestAPI(utype='invalid')

initialize_logger(path + "/../../logs/box_service.log")


class BoxServiceTestCases(unittest.TestCase):
    """ test cases for box service """
    """ PUT: test cases """
    def test_with_valid_details(self):
        """ testing with valid details to update the box """
        box_service_response = box_service.request(
            RequestType.PUT, BOX_SERVICE_URL,
            BoxServicePayloads.update_box_payload)
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))

    def test_with_invalid_details(self):
        """ testing with valid details to update the box """
        box_service_response = box_service.request(
            RequestType.PUT, BOX_SERVICE_URL,
            BoxServicePayloads.update_box_payload)
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))

    """ GET: test cases """

    def test_with_valid_url(self):
        """ test cases for get method """

        box_service_response = box_service.request(
            RequestType.GET, BOX_SERVICE_URL)
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 200,
            msg='Expected code is 200 and got is %s (%s)' %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))

    def test_with_invalid_token(self):

        box_service_response = box_service_invalid_token.request(
            RequestType.GET, BOX_SERVICE_URL)
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 401,
            msg="Expected 401 and got is %s (%s)" %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))

    """ PATCH: test cases """

    def test_box_with_valid_box_id(self):
        """ test cases for get method """

        box_service_response = box_service.request(
            RequestType.PATCH, box_details_url(box_id='1234'))
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 200,
            msg='Expected code is 200 and got is %s (%s)' %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))

    def test_box_with_invalid_token(self):

        box_service_response = box_service_invalid_token.request(
            RequestType.PATCH, box_details_url(box_id=''))
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 401,
            msg="Expected 401 and got is %s (%s)" %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))

    def test_box_with_invald_box_id(self):

        box_service_response = box_service_invalid_token.request(
            RequestType.PATCH, box_details_url(box_id=''))
        logging.info('Response is %s' % box_service_response.text)
        self.assertEquals(
            box_service_response.status_code, 401,
            msg="Expected 401 and got is %s (%s)" %
                (box_service_response.status_code,
                 httplib.responses[box_service_response.status_code]))
