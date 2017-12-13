""" Functional test cases for ticket service """
import logging
import unittest
import httplib
from test.functional_test_suite.common.config import TICKET_SERVICE_URL, \
    ticket_detail_url, initialize_logger
from test.shared.rest_framework import RestAPI, RequestType, path
from test.functional_test_suite.ticket_service.ticket_service_payload import TicketServicePayload

ticket_service = RestAPI(utype='sysops')
ticket_service_invalid = RestAPI(utype='invalid')
initialize_logger(path + '/logs/ticket_service.log')


class TicketService(unittest.TestCase):
    """ To update the status of ticket"""

    """ GET: To get the list of tickets """

    def test_get_list_tickets_with_valid_url(self):
        """ Get the list of tickets """

        # Get the list of all tickets with valid url
        list_tickets_response = ticket_service.request(
            RequestType.GET, TICKET_SERVICE_URL)
        logging.info('Response is %s', list_tickets_response.text)
        self.assertEqual(
            list_tickets_response.status_code, 200,
            msg="Expected 200 and got is %s (%s)" %
                (list_tickets_response.status_code,
                 httplib.responses(list_tickets_response.status_code)))

    def test_get_list_tickets_with_invalid_token(self):
        """ Get the list of tickets """

        expected_message = "Unauthorized"

        # Get the list of all tickets with invalid url
        list_tickets_response = ticket_service_invalid.request(
            RequestType.GET, TICKET_SERVICE_URL)
        list_tickets_response_dict = list_tickets_response.json()
        logging.info('Response is %s', list_tickets_response.text)
        self.assertEqual(
            list_tickets_response.status_code, 401,
            msg="Expected 401 and got is %s (%s)" %
                (list_tickets_response.status_code,
                 httplib.responses[list_tickets_response.status_code]))
        self.assertEquals(
            expected_message, list_tickets_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, list_tickets_response_dict['message']))

    """ PUT: update the ticket status """

    def test_update_ticket_with_valid_ticket_id(self):
        """ Update the ticket with the valid ticket_id """

        # Update the ticket with valid ticket id
        ticket_response = ticket_service.request(
            RequestType.PUT, ticket_detail_url(ticket_id='wbcsjis'),
            payload=TicketServicePayload().update_ticket_payload())
        logging.info('Response is %s', ticket_response.text)
        self.assertEquals(
            ticket_response.status_code, 200,
            msg="Expected 200 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))

    def test_update_ticket_with_invalid_ticket_id(self):
        """ Update the ticket with the duplicate ticket_id """

        message = "No ticket found for provided ticket id"

        # Update the ticket with invalid ticket id
        ticket_response = ticket_service.request(
            RequestType.PUT, ticket_detail_url('asdf'),
            payload=TicketServicePayload().update_ticket_payload())
        ticket_response_dict = ticket_response.json()
        logging.info('Response is %s', ticket_response.text)
        self.assertEquals(
            ticket_response.status_code, 400,
            msg="Expected 400 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))
        self.assertEquals(
            message, ticket_response_dict['message'],
            msg="Expected %s in %s" %
                (message, ticket_response_dict['message']))

    def test_update_ticket_with_invalid_token(self):
        """ Update the ticket with the duplicate ticket_id """

        # Update the ticket without ticket id
        ticket_response = ticket_service_invalid.request(
            RequestType.PUT, ticket_detail_url(''),
            payload=TicketServicePayload().update_ticket_payload())
        ticket_response_dict = ticket_response.json()
        logging.info('Response is %s', ticket_response.text)
        self.assertEquals(
            ticket_response.status_code, 401,
            msg="Expected 401 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))
        self.assertIn(
            'message', ticket_response_dict.keys(),
            msg="Expected %s in %s" %
                ('message', ticket_response_dict.keys()))
