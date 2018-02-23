""" Functional test cases for ticket service """
import logging
import unittest
import httplib
from test.functional_test_suite.common.config import update_ticket_url, \
    initialize_logger, get_tickets_url
from test.shared.rest_framework import RestAPI, RequestType, path
from test.functional_test_suite.ticket_service.ticket_service_payloads import TicketServicePayload

ticket_service = RestAPI(utype='sysops')
ticket_service_invalid = RestAPI(utype='invalid')
initialize_logger(path + '/../../logs/ticket_service.log')
job_id = '86b8ffcf-54ff-49b3-b2fe-05ec13cb043c'
ticket_id = 'CHG0052068'


class TicketService(unittest.TestCase):
    """ To update the status of ticket"""

    """ GET: To get the list of tickets """

    def test_get_list_tickets_with_valid_job_id(self):
        """ Get the list of tickets """

        # Get the list of all tickets with valid url
        list_tickets_response = ticket_service.request(
            RequestType.GET, get_tickets_url(job_id=job_id))
        list_tickets_response_dict = list_tickets_response.json()
        logging.info('test_get_list_tickets_with_valid_url')
        logging.info('Url is %s', get_tickets_url(job_id=job_id))
        logging.info('Response is %s', list_tickets_response.text)
        self.assertEqual(
            list_tickets_response.status_code, 200,
            msg="Expected 200 and got is %s (%s)" %
                (list_tickets_response.status_code,
                 httplib.responses[list_tickets_response.status_code]))
        self.assertIn(
            "list", list_tickets_response_dict.keys(),
            msg="Expected %s in %s" % (
                "list", list_tickets_response_dict.keys()))
        logging.info('test case executed successfully')

    def test_get_list_tickets_with_invalid_token(self):
        """ Get the list of tickets """

        expected_message = "Unauthorized"

        # Get the list of all tickets with invalid url
        list_tickets_response = ticket_service_invalid.request(
            RequestType.GET, get_tickets_url(job_id=job_id))
        list_tickets_response_dict = list_tickets_response.json()
        logging.info('test_get_list_tickets_with_invalid_token')
        logging.info('Url is %s', get_tickets_url(job_id=job_id))
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
        logging.info('test case executed successfully')

    """ PUT: update the ticket status """

    def test_update_ticket_with_valid_ticket_id(self):
        """ Update the ticket with the valid ticket_id """
        expected_message = "Updated Ticket id %s" % ticket_id
        # Update the ticket with valid ticket id
        ticket_response = ticket_service.request(
            RequestType.PUT, update_ticket_url(ticket_id=ticket_id),
            payload=TicketServicePayload().update_ticket_payload())
        ticket_response_dict = ticket_response.json()
        logging.info('test_update_ticket_with_valid_ticket_id')
        logging.info('Url is %s', update_ticket_url(ticket_id=ticket_id))
        logging.info('Request is %s',
                     TicketServicePayload().update_ticket_payload())
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

    def test_update_ticket_with_invalid_ticket_id(self):
        """ Update the ticket with the duplicate ticket_id """

        message = "Exception from Ticket client while fetching the Ticket"

        # Update the ticket with invalid ticket id
        ticket_response = ticket_service.request(
            RequestType.PUT, update_ticket_url('1234'),
            payload=TicketServicePayload().update_ticket_payload())
        ticket_response_dict = ticket_response.json()
        logging.info('test_update_ticket_with_invalid_ticket_id')
        logging.info('Url is %s', update_ticket_url('1234'))
        logging.info('Request is %s',
                     TicketServicePayload().update_ticket_payload())
        logging.info('Response is %s', ticket_response.text)
        self.assertEquals(
            ticket_response.status_code, 500,
            msg="Expected 500 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))
        self.assertEquals(
            message, ticket_response_dict['message'],
            msg="Expected %s in %s" %
                (message, ticket_response_dict['message']))
        logging.info('test case executed successfully')

    def test_update_ticket_with_invalid_token(self):
        """ Update the ticket with the duplicate ticket_id """

        expected_message = "Unauthorized"

        # Update the ticket without ticket id
        ticket_response = ticket_service_invalid.request(
            RequestType.PUT, update_ticket_url(ticket_id=ticket_id),
            payload=TicketServicePayload().update_ticket_payload())
        ticket_response_dict = ticket_response.json()
        logging.info('test_update_ticket_with_invalid_token')
        logging.info('Url is %s', update_ticket_url(ticket_id=ticket_id))
        logging.info('Request is %s',
                     TicketServicePayload().update_ticket_payload())
        logging.info('Response is %s', ticket_response.text)
        self.assertEquals(
            ticket_response.status_code, 401,
            msg="Expected 401 and actual is %s (%s)" %
                (ticket_response.status_code,
                 httplib.responses[ticket_response.status_code]))
        self.assertEquals(
            expected_message, ticket_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, ticket_response_dict['message']))
        logging.info('test case executed successfully')
