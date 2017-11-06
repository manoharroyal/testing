import unittest
import httplib
from api_functional_testing.test.functional_test_suit.common.config import \
    TICKET_SERVICE_URL
from api_functional_testing.test.shared.rest_framework import RestAPIHeader, \
    RequestType
from api_functional_testing.test.functional_test_suit.common.payloads import \
    TicketServicePayload

ticket_service_obj = RestAPIHeader()


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
            msg="Expected 200 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))
