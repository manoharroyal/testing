""" Functional Test cases for order Service of DSS Micro Service Layer """
import logging
import unittest
import httplib
from test.shared.rest_framework import RestAPI, RequestType, path
from test.functional_test_suite.common.config import initialize_logger, \
    order_details_url

order_service = RestAPI(utype='sysops')
invalid_order_service = RestAPI(utype='invalid')
initialize_logger(path + '/../../logs/order_service.log')


class OrderServiceTestCases(unittest.TestCase):
    """ Test cases for order service """

    """ GET: To get the order details """

    def test_track_order_with_valid_order_id(self):
        """ testing with valid order to get order details """

        order_service_response = order_service.request(
            RequestType.GET, order_details_url(order_id='1234'))
        logging.info('test_track_order_with_valid_order_id')
        logging.info('Url is %s' % order_details_url(order_id='1234'))
        logging.info('Response is %s' % order_service_response.text)
        self.assertEquals(
            order_service_response.status_code, 200,
            msg='Expected code is 200 and got is %s (%s)' %
                (order_service_response.status_code,
                 httplib.responses[order_service_response.status_code]))
        logging.info('test case executed successfully')

    def test_track_order_with_invalid_order_id(self):
        """ testing with valid order to get order details """

        order_service_response = order_service.request(
            RequestType.GET, order_details_url(order_id='1234'))
        logging.info('test_track_order_with_valid_order_id')
        logging.info('Url is %s' % order_details_url(order_id='1234'))
        logging.info('Response is %s' % order_service_response.text)
        self.assertEquals(
            order_service_response.status_code, 400,
            msg='Expected code is 400 and got is %s (%s)' %
                (order_service_response.status_code,
                 httplib.responses[order_service_response.status_code]))
        logging.info('test case executed successfully')

    def test_track_order_with_invalid_token(self):
        """ testing with valid order to get order details """

        expected_message = "Unauthorized"

        order_service_response = invalid_order_service.request(
            RequestType.GET, order_details_url(order_id='1234'))
        order_service_response_dict = order_service_response.json()
        logging.info('test_track_order_with_valid_order_id')
        logging.info('Url is %s' % order_details_url(order_id='1234'))
        logging.info('Response is %s' % order_service_response.text)
        self.assertEquals(
            order_service_response.status_code, 401,
            msg='Expected code is 401 and got is %s (%s)' %
                (order_service_response.status_code,
                 httplib.responses[order_service_response.status_code]))
        self.assertEquals(
            expected_message, order_service_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, order_service_response_dict['message']))
        logging.info('test case executed successfully')
