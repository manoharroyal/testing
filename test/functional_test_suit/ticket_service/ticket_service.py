import unittest
import httplib
from test.functional_test_suit.common.config import TICKET_SERVICE_URL, \
    TICKETS_URL
from test.shared.rest_framework import RestAPIHeader, RequestType
from test.functional_test_suit.common.payloads import TicketServicePayload

ticket_service_obj = RestAPIHeader(utype='sysops')


class TicketService(unittest.TestCase):
    """ To update the status of ticket"""

    def test_with_valid_ticket_id(self):
        """ Update the ticket with the valid ticket_id """
        ticket_response = ticket_service_obj.request(
            RequestType.PUT, TICKET_SERVICE_URL,
            payload=TicketServicePayload().update_ticket_payload())
        self.assertEquals(
            ticket_response.status_code, 200,
            msg="Expected 200 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))

    def test_with_invalid_ticket_id(self):
        """ Update the ticket with the duplicate ticket_id """
        ticket_response = ticket_service_obj.request(
            RequestType.PUT, TICKET_SERVICE_URL,
            payload=TicketServicePayload().update_ticket_payload())
        self.assertEquals(
            ticket_response.status_code, 400,
            msg="Expected 400 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))

        """ GET: To get the list of tickets """

    def test_get_list_tickets_with_valid_url(self):
        """ Get the list of tickets """
        list_tickets_response = ticket_service_obj.request(
            RequestType.GET, TICKETS_URL)
        self.assertEqual(
            list_tickets_response.status_code, 200,
            msg="Expected 200 and got is %s (%s)" %
                (list_tickets_response.status_code,
                 httplib.responses(list_tickets_response.status_code)))

    def test_get_list_tickets_with_invalid_url(self):
        """ Get the list of tickets """
        list_tickets_response = ticket_service_obj.request(
            RequestType.GET, TICKETS_URL)
        self.assertEqual(
            list_tickets_response.status_code, 400,
            msg="Expected 400 and got is %s (%s)" %
                (list_tickets_response.status_code,
                 httplib.responses(list_tickets_response.status_code)))

    def test_get_list_tickets_without_url(self):
        """ Get the list of tickets """
        list_tickets_response = ticket_service_obj.request(
            RequestType.GET, TICKETS_URL)
        self.assertEqual(
            list_tickets_response.status_code, 403,
            msg="Expected 403 and got is %s (%s)" %
                (list_tickets_response.status_code,
                 httplib.responses(list_tickets_response.status_code)))
