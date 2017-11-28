""" Functional test cases for ticket service """
import logging
import unittest
import httplib
from test.functional_test_suite.common.config import TICKET_SERVICE_URL, \
    ticket_detail_url
from test.shared.rest_framework import RestAPI, RequestType
from test.functional_test_suite.common.payloads import TicketServicePayload

ticket_service_obj = RestAPI(utype='sysops')


class TicketService(unittest.TestCase):
    """ To update the status of ticket"""

    def test_with_valid_ticket_id(self):
        """ Update the ticket with the valid ticket_id """

        # Update the ticket with valid ticket id
        ticket_response = ticket_service_obj.request(
            RequestType.PUT, ticket_detail_url('wbcsjis'),
            payload=TicketServicePayload().update_ticket_payload())
        logging.info('Response is %s', ticket_response.text)
        self.assertEquals(
            ticket_response.status_code, 200,
            msg="Expected 200 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))

    def test_with_invalid_ticket_id(self):
        """ Update the ticket with the duplicate ticket_id """

        message = "No ticket found for provided ticket id"

        # Update the ticket with invalid ticket id
        ticket_response = ticket_service_obj.request(
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

    def test_without_ticket_id(self):
        """ Update the ticket with the duplicate ticket_id """

        # Update the ticket without ticket id
        ticket_response = ticket_service_obj.request(
            RequestType.PUT, ticket_detail_url(''),
            payload=TicketServicePayload().update_ticket_payload())
        ticket_response_dict = ticket_response.json()
        logging.info('Response is %s', ticket_response.text)
        self.assertEquals(
            ticket_response.status_code, 403,
            msg="Expected 403 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))
        self.assertIn(
            'message', ticket_response_dict.keys(),
            msg="Expected %s in %s" %
                ('message', ticket_response_dict.keys()))

        """ GET: To get the list of tickets """

    def test_get_list_tickets_with_valid_url(self):
        """ Get the list of tickets """

        # Get the list of all tickets with valid url
        list_tickets_response = ticket_service_obj.request(
            RequestType.GET, TICKET_SERVICE_URL)
        logging.info('Response is %s', list_tickets_response.text)
        self.assertEqual(
            list_tickets_response.status_code, 200,
            msg="Expected 200 and got is %s (%s)" %
                (list_tickets_response.status_code,
                 httplib.responses(list_tickets_response.status_code)))

    def test_get_list_tickets_with_invalid_url(self):
        """ Get the list of tickets """

        # Get the list of all tickets with invalid url
        list_tickets_response = ticket_service_obj.request(
            RequestType.GET, TICKET_SERVICE_URL)
        logging.info('Response is %s', list_tickets_response.text)
        self.assertEqual(
            list_tickets_response.status_code, 400,
            msg="Expected 400 and got is %s (%s)" %
                (list_tickets_response.status_code,
                 httplib.responses(list_tickets_response.status_code)))
