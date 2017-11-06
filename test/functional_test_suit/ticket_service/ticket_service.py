import unittest
from test.functional_test_suit.common.config import TICKET_SERVICE_URL
from test.shared.rest_framework import RestAPIHeader, RequestType
from test.functional_test_suit.common.payloads import TicketServicePayload

ticket_service_obj = RestAPIHeader()


class TicketService(unittest.TestCase):
    """ To update the status of ticket"""

    def test_with_valid_ticket_id(self):
        """ Update the ticket with the valid ticket_id """
        out = ticket_service_obj.request(RequestType.PUT, TICKET_SERVICE_URL,
                                         payload=TicketServicePayload().
                                         update_ticket_payload())
        self.assertEquals(out.status_code, 200)

    def test_with_invalid_ticket_id(self):
        """ Update the ticket with the duplicate ticket_id """
        out = ticket_service_obj.request(RequestType.PUT, TICKET_SERVICE_URL,
                                         payload=TicketServicePayload().
                                         update_ticket_payload())
        self.assertEquals(out.status_code, 400)
