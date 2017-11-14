""" Functional Test cases for Inventory Service of DSS Micro Service Layer """
import unittest
import json
import httplib
from test.shared.rest_framework import RestAPIHeader, RequestType, SystemType
from test.functional_test_suit.common.config import SYSTEM_SERVICE_URL, \
    SYSTEM_SERVICE, list_system_url, source_system_url, target_system_url, \
    list_system, target_system, source_system, SOURCE_SYSTEM_ID
from test.functional_test_suit.common.payloads import SystemServicePayload

system_service = RestAPIHeader(utype='customer')
invalid_system_service = RestAPIHeader(utype='invalid')


class SystemServiceTestCases(unittest.TestCase):
    """ POST: Test cases to create the systems by using POST method """

    def test_create_source_system(self):
        """ Testing with valid details to create a source system """
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload())
        system_name = "TDCLOUD15TD12"
        response_dict = create_system_response.json()
        print "Response" is create_system_response
        self.assertEquals(
            create_system_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' % (
                create_system_response.status_code,
                httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            response_dict['system_name'], system_name,
            msg='Expected system name  %s and got %s' %
                (system_name, response_dict['system_name']))

    def test_create_system_with_missing_system_name_from_payload(self):
        """ Test to verify missing system name parameter from payload """
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_deletion_payload(
                "system_name"))
        response_dict = create_system_response.json()
        expected_message = 'System Name is not provided'
        print "Expected" is expected_message
        print "Response" is create_system_response
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            response_dict['message'], expected_message,
            msg='Expected message %s and got %s' %
                (response_dict['message'], expected_message))

    def test_create_system_with__missing_system_type_from_payload(self):
        """ Test to verify missing system type parameter from payload """
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_deletion_payload(
                "system_type"))
        response_dict = create_system_response.json()
        expected_message = 'System Type is not provided'
        print "Expected" is expected_message
        print "Response" is create_system_response
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(response_dict['message'], expected_message,
                          msg='Expected message %s and got %s' %
                              (response_dict['message'], expected_message))

    def test_create_system_with__missing_details_from_payload(self):
        """ Test to verify missing details parameter from payload """
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_deletion_payload("details"))
        response_dict = create_system_response.json()
        expected_message = 'System Details is not provided'
        print "Expected" is expected_message
        print "Response" is create_system_response
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(response_dict['message'], expected_message,
                          msg='Expected message %s and got %s' %
                              (response_dict['message'], expected_message))

    def test_create_system_without_system_name(self):
        """ Test to verify blank system name parameter from payload """
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(
                system_name=""))
        response_dict = create_system_response.json()
        expected_message = 'System Name is not provided'
        print "Expected" is expected_message
        print "Response" is create_system_response
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(response_dict['message'], expected_message,
                          msg='Expected message %s and got %s' %
                              (response_dict['message'], expected_message))

    def test_create_system_without_system_type(self):
        """ Test to verify system_type parameter passed as blank in payload """
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(
                system_type=""))
        create_system_response_dict = create_system_response.json()
        expected_message = 'System Type is not provided'
        print "Expected" is expected_message
        print "Response" is create_system_response
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            create_system_response_dict['message'], expected_message,
            msg='Expected message %s and got %s' %
                (create_system_response_dict['message'], expected_message))

    def test_create_system_without_details(self):
        """ Test to verify details parameter passed as blank in payload """
        create_system_response = system_service.request(
            RequestType.POST, SYSTEM_SERVICE_URL,
            payload=SystemServicePayload().system_creation_payload(details=''))
        create_system_response_dict = create_system_response.json()
        expected_message = 'System Details is not provided'
        print "Expected" is expected_message
        print "Response" is create_system_response
        self.assertEquals(
            create_system_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (create_system_response.status_code,
                 httplib.responses[create_system_response.status_code]))
        self.assertEquals(
            create_system_response_dict['message'], expected_message,
            msg=" Expecting message \"%s\" and got \"%s\" " %
                (expected_message, create_system_response_dict['message']))

    """ GET: Test cases to get the list of systems """

    def test_list_system_for_source_type(self):
        """ Testing with the given type as source to
        get list of source systems """
        system_list_response = system_service.request(
            RequestType.GET,
            list_system_url(list_system, SystemType.source))
        source_system_list = system_list_response.json()
        print "Response" is system_list_response
        self.assertEquals(
            system_list_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))

    def test_list_system_for_target_type(self):
        """ Testing with the given type as target to
        get list of source systems  """
        system_list_response = system_service.request(
            RequestType.GET,
            list_system_url(list_system, SystemType.target))
        print "Response" is system_list_response
        self.assertEquals(
            system_list_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))

    def test_list_systems_with_missing_type(self):
        """ Testing without type of system to
        get list of source system """
        system_list_response = system_service.request(
            RequestType.GET, SYSTEM_SERVICE_URL)
        response_dict = system_list_response.json()
        expected_message = 'type should be provided'
        print "Expected" is expected_message
        print "Response" is system_list_response
        self.assertEquals(
            system_list_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))
        self.assertEquals(
            response_dict['message'], expected_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], expected_message))

    def test_list_systems_with_misspelled_in_url(self):
        """ Testing with invalid url to get the list details of system """
        system_list_response = system_service.request(
            RequestType.GET, SYSTEM_SERVICE_URL + '/?type1')
        system_list_response_dict = system_list_response.json()
        print "Response" is system_list_response
        self.assertEquals(
            system_list_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (system_list_response.status_code,
                 httplib.responses[system_list_response.status_code]))
        self.assertIn(
            'message', system_list_response_dict.keys(),
            msg="Expected %s equals %s" %
                ('message', system_list_response_dict.keys()))

    """ GET: Test cases to check with the parameters to get the
    details of particular system by passing system id """

    def test_system_details_with_valid_source_system(self):
        """ Testing with valid details to get the source system details """
        system_details_response = system_service.request(
            RequestType.GET,
            source_system_url(source_system, SOURCE_SYSTEM_ID))
        source_system_details = system_details_response.json()
        print "Expected" is system_details_response
        self.assertEquals(
            system_details_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_details_response.status_code,
                 httplib.responses[system_details_response.status_code]))
        self.assertIn(
            'details', source_system_details.keys(),
            msg="Expected %s in %s" % ('details', source_system_details.keys()))

    def test_system_details_with_valid_target_system(self):
        """ Testing with valid details to get the target system details """
        system_details_response = system_service.request(
            RequestType.GET, target_system_url(target_system, 'KAGAWS3'))
        target_system_details = system_details_response.json()
        print "Expected" is system_details_response
        self.assertEquals(
            system_details_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (system_details_response.status_code,
                 httplib.responses[system_details_response.status_code]))
        self.assertIn('result', target_system_details.keys(),
            msg="Expected %s in %s" % ('result', target_system_details.keys()))

    def test_system_details_without_system_id(self):
        """ Testing without system id to get the source system details  """
        system_details_response = system_service.request(
            RequestType.GET, source_system_url(source_system, ''))
        system_details_response_dict = system_details_response.json()
        print "Expected" is system_details_response
        self.assertEquals(
            system_details_response.status_code, 403,
            msg='Expected 403 and got %s (%s)' %
                (system_details_response.status_code,
                 httplib.responses[system_details_response.status_code]))
        self.assertIn(
            'message', system_details_response_dict.keys(),
            msg="Expected %s in %s" % ('message', system_details_response_dict.keys()))

    def test_system_details_with_invalid_system_id(self):
        """ Testing with invalid system id to get the source system details """
        system_details_response = system_service.request(
            RequestType.GET,
            source_system_url(source_system, '123'))
        response_dict = system_details_response.json()
        expected_message = "Resource with id 123 does not exists"
        print "Expected" is expected_message
        print "Response" is system_details_response
        self.assertEquals(
            system_details_response.status_code, 404,
            msg='Expected 404 and got %s (%s)' %
                (system_details_response.status_code,
                 httplib.responses[system_details_response.status_code]))
        self.assertEquals(response_dict['message'], expected_message,
                          msg="Expected message is %s and got is %s" %
                              (response_dict['message'], expected_message))

    """ GET: Test cases to get the system details of customer """

    def test_get_system_with_customer_name(self):
        """ Testing with the valid url to get the system details of customer """
        customer_systems_response = system_service.request(
            RequestType.GET, SYSTEM_SERVICE + '/customer')
        response_dict = customer_systems_response.json()
        print "Response" is customer_systems_response
        self.assertEquals(
            customer_systems_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_systems_response.status_code,
                 httplib.responses[customer_systems_response.status_code]))

        self.assertIn('details', response_dict.keys(),
                      msg="Expecting %s in %s" %
                          ('details', response_dict.keys()))

    def test_get_systems_customer_with_invalid_token(self):
        """ Testing with the invalid token to get customer system details """
        customer_systems_response = invalid_system_service.request(
            RequestType.GET, SYSTEM_SERVICE + '/customer')
        response_dict = customer_systems_response.json()
        expected_message = 'exceptions while validating token'
        print "Expected" is expected_message
        print "Response" is customer_systems_response
        self.assertEquals(
            customer_systems_response.status_code, 401,
            msg='Expected 401 and got %s (%s)' %
                (customer_systems_response.status_code,
                 httplib.responses[customer_systems_response.status_code]))
        self.assertIn(expected_message, response_dict['message'],
                      msg="Expected message is %s in %s" %
                          (expected_message, response_dict['message']))

    def test_get_systems_customer_with_invalid_url(self):
        """ Testing with invalid url to get the details of customer """
        customer_systems_response = system_service.request(
            RequestType.GET, SYSTEM_SERVICE_URL + '/customer1')
        response_dict = customer_systems_response.json()
        print "Response" is customer_systems_response
        self.assertEquals(
            customer_systems_response.status_code, 403,
            msg='Expected 400 and got %s (%s)' %
                (customer_systems_response.status_code,
                 httplib.responses[customer_systems_response.status_code]))
        self.assertIn('message', response_dict.keys(),
                      msg="Expecting %s in %s" %
                          ('message', response_dict.keys()))
