""" Functional test cases for customer profile service """

import logging
import unittest
import httplib
from test.shared.rest_framework import RequestType, RestAPI, path
from test.functional_test_suite.common.config import CUSTOMER_SERVICE_URL, \
    initialize_logger
from test.functional_test_suite.customer_profile_service.customer_profile_service_payloads import CustomerProfileServicePayload

customer_service = RestAPI(utype='customer')
customer_service_invalid_token = RestAPI(utype='invalid')


customer_profile_url = CUSTOMER_SERVICE_URL + str(customer_service.customerId)
customer_profile_invalid_customer_id = customer_profile_url + "1" + "/addresses/"
customer_profile_address_url = customer_profile_url + "/addresses/"
initialize_logger(path + "/../../logs/customer_profile_service.log")


class CustomerProfileTestCases(unittest.TestCase):
    """ Test cases for the creation of customer profile
    by passing the input parameters """

    """ GET: Test cases to get the list of addresses of customer """

    def test_list_address_with_customer_id(self):
        """ Test with the valid customer_id to get the list of addresses """

        # Get the list of addresses of customer with customer id
        customer_profile_response = customer_service.request(
            RequestType.GET, customer_profile_url)
        customer_profile_response.dict = customer_profile_response.json()
        logging.info('test_list_address_with_customer_id')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn(
            'shipping_addresses', customer_profile_response.dict.keys(),
            msg="Expected %s in %s" %
                ('shipping_addresses', customer_profile_response.dict.keys()))

    def test_list_address_with_customer_id_mismatch(self):
        """ Test with mis matched customer_id to get the list of addresses """

        expected_message = "Customer_id mismatch"

        # Get the list of addresses of customer with invalid customer id
        customer_profile_response = customer_service.request(
            RequestType.GET, CUSTOMER_SERVICE_URL + str(
                customer_service.customerId) + '12')
        customer_profile_response_dict = customer_profile_response.json()
        logging.info('test_list_address_with_customer_id_mismatch')
        logging.info('Url is %s', (CUSTOMER_SERVICE_URL + str(
                customer_service.customerId) + '12'))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_dict['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_dict['message'], expected_message))

    def test_list_address_customer_profile_with_invalid_token(self):
        """ Test without customer_id to get the list of addresses """

        # Get the list of addresses of customer with invalid token
        customer_profile_response = customer_service_invalid_token.request(
            RequestType.GET, CUSTOMER_SERVICE_URL)
        customer_profile_response_dict = customer_profile_response.json()
        logging.info('test_list_address_customer_profile_with_invalid_token')
        logging.info('Url is %s', CUSTOMER_SERVICE_URL)
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 403,
            msg='Expected 403 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn('message', customer_profile_response_dict.keys(),
                      msg="Expected message in %s and got %s" %
                          ('message', customer_profile_response_dict.keys()))

    """ PUT : Create/Update customer profile """

    def test_add_new_shipping_address_with_valid_details(self):
        """ Testing with valid details to add
        new shipping address to the customer profile """

        # create an address with address line 2
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload
            (addr1="New River Bridge", addr2="Near Post Office"))

        # Get the added address
        customer_profile_response_dict = customer_service.request(
            RequestType.GET,
            customer_profile_address_url + "9876").json()
        logging.info('test_add_new_shipping_address_with_valid_details')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s', (CustomerProfileServicePayload().customer_profile_payload
            (addr1="New River Bridge", addr2="Near Post Office")))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))

    def test_add_new_shipping_address_with_invalid_customer_id(self):
        """ Testing with mismatch customer_id to add
        new shipping address to the customer profile """

        expected_message = "Customer_id mismatch"

        # Create an address with invalid customer id
        customer_profile_response = customer_service.request(
            RequestType.PUT,
            CUSTOMER_SERVICE_URL + str('23e'),
            payload=CustomerProfileServicePayload().customer_profile_payload(
                addr1="400_NE, River_Bridge", addr2='Near Post Office'))
        customer_profile_response_dict = customer_profile_response.json()
        logging.info('test_add_new_shipping_address_with_invalid_customer_id')
        logging.info('Url is %s', CUSTOMER_SERVICE_URL + str('23e'))
        logging.info('Request is %s', CustomerProfileServicePayload().customer_profile_payload(
                addr1="400_NE, River_Bridge", addr2='Near Post Office'))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_dict['message'],
            msg="Expected message %s and got %s" %
                (expected_message, customer_profile_response_dict['message']))

    def test_add_new_shipping_address_with_invalid_token(self):
        """ Testing with mismatch customer_id to add
        new shipping address to the customer profile """

        expected_message = "Unauthorized"

        # Create an address with invalid customer id
        customer_profile_response = customer_service_invalid_token.request(
            RequestType.PUT,
            CUSTOMER_SERVICE_URL + str(customer_service.customerId),
            payload=CustomerProfileServicePayload().customer_profile_payload(
                addr1="400_NE, River_Bridge", addr2='Near Post Office'))
        logging.info('test_add_new_shipping_address_with_invalid_token')
        logging.info('Url is %s', CUSTOMER_SERVICE_URL + str('23e'))
        logging.info('Request is %s',
                     CustomerProfileServicePayload().customer_profile_payload(
                         addr1="400_NE, River_Bridge",
                         addr2='Near Post Office'))
        logging.info('Response is %s', customer_profile_response.text)
        customer_profile_response_dict = customer_profile_response.json()
        self.assertEquals(
            customer_profile_response.status_code, 401,
            msg='Expected 401 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_dict['message'],
            msg="Expected message %s and got %s" %
                (expected_message, customer_profile_response_dict['message']))

    def test_update_customer_profile_without_title(self):
        """ Testing without title to update customer profile """

        expected_message = 'Shipping address: ' + "title" + ' is not provided'

        # Update the address without title
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "title"))
        customer_profile_response_text = customer_profile_response.json()
        logging.info('test_update_customer_profile_without_title')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s', CustomerProfileServicePayload().delete_payload_parameter(
                "title"))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message,  customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    def test_update_customer_profile_without_address_line_1(self):
        """ Testing without address_line_1 to update customer profile """

        expected_message = 'Shipping address: ' + "address_line_1" + \
                           ' is not provided'

        # Update the address without address line1
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "address_line_1"))
        customer_profile_response_text = customer_profile_response.json()
        logging.info('test_update_customer_profile_without_address_line_1')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s',
                     CustomerProfileServicePayload().delete_payload_parameter(
                         "address_line_1"))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message,  customer_profile_response_text['message']))

    def test_add_new_shipping_address_without_address_line2(self):
        """ Testing without address line2 to add
        new shipping address to the customer profile """

        # Create an address without address line 2
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title="9876"))

        # Get the added address
        customer_profile_response_dict = customer_service.request(
            RequestType.GET,
            customer_profile_address_url + "9876").json()
        logging.info('test_add_new_shipping_address_without_address_line2')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s',
                     CustomerProfileServicePayload().customer_profile_payload(
                         title="9876"))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn(
            'title', customer_profile_response_dict.keys(),
            msg='Expected %s in %s' %
                ('shipping_addresses', customer_profile_response_dict.keys()))

    def test_update_customer_profile_without_contact_name(self):
        """ Testing without  contact name to update customer profile """

        expected_message = 'Shipping address: ' + "contact_name" + \
                           ' is not provided'

        # Update the address without contact name
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "contact_name"))
        customer_profile_response_text = customer_profile_response.json()
        logging.info('test_update_customer_profile_without_contact_name')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s',
                     CustomerProfileServicePayload().delete_payload_parameter(
                         "contact_name"))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    def test_update_customer_profile_without_contact_number(self):
        """ Testing without contact number to update customer profile """

        expected_message = 'Shipping address: ' + "contact_number" + \
                           ' is not provided'

        # Update the address without contact number
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "contact_number"))
        customer_profile_response_text = customer_profile_response.json()
        logging.info('test_update_customer_profile_without_contact_number')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s',
                     CustomerProfileServicePayload().delete_payload_parameter(
                         "contact_number"))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    def test_update_customer_profile_without_city(self):
        """ Testing without city to update customer profile """

        expected_message = 'Shipping address: ' + "city" + ' is not provided'

        # Update the address without city
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "city"))
        customer_profile_response_text = customer_profile_response.json()
        logging.info('test_update_customer_profile_without_city')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s',
                     CustomerProfileServicePayload().delete_payload_parameter(
                         "city"))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    def test_update_customer_profile_without_state(self):
        """ Testing without state to update customer profile """

        expected_message = 'Shipping address: ' + "state" + ' is not provided'

        # Update the address without state
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "state"))
        customer_profile_response_text = customer_profile_response.json()
        logging.info('test_update_customer_profile_without_state')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s',
                     CustomerProfileServicePayload().delete_payload_parameter(
                         "state"))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    def test_update_customer_profile_without_country(self):
        """ Testing without country to update customer profile """

        expected_message = 'Shipping address: ' + "country" + ' is not provided'

        # Update the address without country
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "country"))
        customer_profile_response_text = customer_profile_response.json()
        logging.info('test_update_customer_profile_without_country')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s',
                     CustomerProfileServicePayload().delete_payload_parameter(
                         "country"))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    def test_update_customer_profile_without_zipcode(self):
        """
        Testing without zipcode to update customer profile """

        expected_message = 'Shipping address: ' + "zipcode" + ' is not provided'

        # Update the address without zip code
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "zipcode"))
        customer_profile_response_text = customer_profile_response.json()
        logging.info('test_update_customer_profile_without_zipcode')
        logging.info('Url is %s', customer_profile_url)
        logging.info('Request is %s',
                     CustomerProfileServicePayload().delete_payload_parameter(
                         "zipcode"))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    """ GET: Test cases to get the particular address details
         of the customer by the address title """

    def test_get_address_details_for_given_customer(self):
        """ Testing with the valid address to get the
        details of the customer """

        # Get the address details with valid title
        customer_profile_response = customer_service.request(
            RequestType.GET, customer_profile_address_url + 'Test_Job')
        customer_profile_response_dict = customer_profile_response.json()
        logging.info('test_get_address_details_for_given_customer')
        logging.info('Url is %s', customer_profile_address_url + 'Test_Job')
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn('title', customer_profile_response_dict.keys(),
                      msg="Expected %s in %s" %
                          ('title', customer_profile_response_dict.keys()))

    def test_get_address_with_customer_id_mismatch(self):
        """ Testing with the mis match customer_id to get the
        details of the customer """

        expected_message = "Customer_id mismatch"

        # Get the address details with customer id mismatch
        customer_profile_addresses_url = \
            CUSTOMER_SERVICE_URL + str(customer_service.customerId) + \
            "23" + "/addresses/"
        customer_profile_response = customer_service.request(
            RequestType.GET, customer_profile_addresses_url + "Restore_Job")
        customer_profile_response_dict = customer_profile_response.json()
        logging.info('test_get_address_with_customer_id_mismatch')
        logging.info('Url is %s', customer_profile_addresses_url + "Restore_Job")
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, customer_profile_response_dict['message']))

    def test_get_address_with_invalid_title(self):
        """ Testing with invalid address title to get the
        details of the customer """

        expected_message = 'Address does not exist'

        # Get the address details with invalid title
        customer_profile_response = customer_service.request(
            RequestType.GET,
            customer_profile_address_url + str('xyz'))
        customer_profile_response_dict = customer_profile_response.json()
        logging.info('test_get_address_with_invalid_title')
        logging.info('Url is %s', customer_profile_address_url + str('xyz'))
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 404,
            msg='Expected 404 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, customer_profile_response_dict['message']))

    """ PUT: Test cases to update the shipping address by the address title """

    def test_update_shipping_address_with_valid_details(self):
        """ Testing with valid details to update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address with valid details
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + address_title,
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload())
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_with_valid_details')
        logging.info('Url is %s', customer_profile_address_url + address_title)
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload())
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    def test_update_shipping_address_with_invalid_title(self):
        """ Testing with invalid title to update
        shipping address to the customer profile """

        expected_message = "Address does not exist"

        # Update the shipping_address with invalid title
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "1111123",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload())
        customer_profile_shipping_address_response_dict = \
            customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_with_invalid_title')
        logging.info('Url is %s', customer_profile_address_url + "1111123")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload())
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 404,
            msg="Expected 404 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            expected_message,
            customer_profile_shipping_address_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message,
                 customer_profile_shipping_address_response_dict['message']))

    def test_update_shipping_address_with_invalid_customer_id(self):
        """ Testing with invalid title to update
        shipping address to the customer profile """

        expected_message = "Customer_id mismatch"

        # Update the shipping_address with invalid customer_id
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_invalid_customer_id + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload())
        customer_profile_shipping_address_response_dict = \
            customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_with_invalid_customer_id')
        logging.info('Url is %s', customer_profile_invalid_customer_id + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload())
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 400,
            msg="Expected 400 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            expected_message,
            customer_profile_shipping_address_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message,
                 customer_profile_shipping_address_response_dict['message']))

    def test_update_shipping_address_with_invalid_token(self):
        """ Testing with invalid title to update
        shipping address to the customer profile """

        expected_message = "Unauthorized"

        # Update the shipping_address with invalid customer_id
        customer_profile_shipping_address_response = \
            customer_service_invalid_token.request(
                RequestType.PUT, customer_profile_address_url + "9876",
                payload=CustomerProfileServicePayload().
                    update_shipping_address_payload())
        customer_profile_shipping_address_response_dict = \
            customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_with_invalid_token')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload().
                     update_shipping_address_payload())
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 401,
            msg="Expected 401 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            expected_message,
            customer_profile_shipping_address_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message,
                 customer_profile_shipping_address_response_dict['message']))

    def test_update_shipping_address_without_address_line_1(self):
        """ Testing without address_line_1 to update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address without address_line_1
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload(addr1=""))
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_without_address_line_1')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload(addr1=""))
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    def test_update_shipping_address_without_address_line_2(self):
        """ Testing without address_line_2 to update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address without address_line_2
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload(addr2=""))
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_without_address_line_2')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload(addr2=""))
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    def test_update_shipping_address_without_contact_name(self):
        """ Testing without contact name to update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address without contact name
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload(contact_name=""))
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_without_contact_name')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload(contact_name=""))
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    def test_update_shipping_address_without_contact_number(self):
        """ Testing without contact number to update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address without number
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload(contact_number=""))
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_without_contact_number')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload(contact_number=""))
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    def test_update_shipping_address_without_company_name(self):
        """ Testing without company name update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address without company name
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload(company_name="buiH12^&!%$"))
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_without_company_name')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload(
                         company_name="buiH12^&!%$"))
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    def test_update_shipping_address_without_city(self):
        """ Testing without city to update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address without city
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload(city=""))
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_without_city')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload(city=""))
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    def test_update_shipping_address_without_state(self):
        """ Testing without state to update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address without state
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload(state=""))
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_without_state')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload(state=""))
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    def test_update_shipping_address_without_country(self):
        """ Testing without country to update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address without country
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload(country=""))
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_without_country')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload(country=""))
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    def test_update_shipping_address_without_zipcode(self):
        """ Testing without zipcode to update
        shipping address to the customer profile """

        address_title = "9876"

        # Update the shipping_address without zipcode
        customer_profile_shipping_address_response = customer_service.request(
            RequestType.PUT, customer_profile_address_url + "9876",
            payload=CustomerProfileServicePayload
            ().update_shipping_address_payload(zipcode=""))
        response_dict = customer_profile_shipping_address_response.json()
        logging.info('test_update_shipping_address_without_zipcode')
        logging.info('Url is %s', customer_profile_address_url + "9876")
        logging.info('Request is %s',
                     CustomerProfileServicePayload
                     ().update_shipping_address_payload(zipcode=""))
        logging.info('Response is %s',
                     customer_profile_shipping_address_response.text)
        self.assertEquals(
            customer_profile_shipping_address_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_shipping_address_response.status_code,
                 httplib.responses[
                     customer_profile_shipping_address_response.status_code]))
        self.assertEquals(
            address_title, response_dict['title'],
            msg="Expected %s is equal to %s" %
                (address_title, response_dict['title']))

    """ DELETE: Test cases to delete the customer address with address title """

    def test_zdelete_address_with_valid_customer(self):
        """ Testing with the valid address title """

        # Delete address with valid title
        customer_profile_response = customer_service.request(
            RequestType.DELETE, customer_profile_address_url + "9876")
        customer_profile_response_dict = customer_profile_response.json()
        logging.info('test_delete_address_with_valid_customer')
        logging.info('Url is %s', customer_profile_address_url + "1111")
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))

    def test_delete_address_with_wrong_title(self):
        """ Testing with the invalid address title """

        expected_message = "Address does not exist"

        # Delete address with valid wrong title
        customer_profile_response = customer_service.request(
            RequestType.DELETE, customer_profile_address_url + "XYZ")
        customer_profile_response_dict = customer_profile_response.json()
        logging.info('test_delete_address_with_wrong_title')
        logging.info('Url is %s', customer_profile_address_url + "XYZ")
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 404,
            msg='Expected 404 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, customer_profile_response_dict['message']))

    def test_delete_address_with_customer_id_mismatch(self):
        """ Testing with the invalid address title """

        expected_message = "Customer_id mismatch"

        # Delete address with customer id mismatch
        customer_profile_response = customer_service.request(
            RequestType.DELETE,
            customer_profile_url + "24" + "/addresses/Test_Job")
        customer_profile_response_dict = customer_profile_response.json()
        logging.info('test_delete_address_with_customer_id_mismatch')
        logging.info('Url is %s',
                     customer_profile_url + "24" + "/addresses/Test_Job")
        logging.info('Response is %s', customer_profile_response.text)
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                    httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, customer_profile_response_dict['message']))
