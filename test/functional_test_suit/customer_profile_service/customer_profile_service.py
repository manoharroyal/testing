""" Functional test cases for user profile service """

import unittest
import httplib
from test.shared.rest_framework import RequestType, RestAPIHeader
from test.functional_test_suit.common.config import CUSTOMER_SERVICE_URL
from test.functional_test_suit.common.payloads import \
    CustomerProfileServicePayload

customer_service = RestAPIHeader(utype='customer')
customer_service_invalid_token = RestAPIHeader(utype='invalid')
customer_profile_url = CUSTOMER_SERVICE_URL + str(customer_service.customerId)
customer_profile_address_url = customer_profile_url + "/addresses/"


class CustomerProfileTestCases(unittest.TestCase):
    """ Test cases for the creation of customer profile
    by passing the input parameters """
    """ PUT : Create/Update customer profile """

    def test_add_new_shipping_address_without_optional_Param(self):
        """ Testing without optional address to add
        new shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title="9876"))
        input_dict = CustomerProfileServicePayload().customer_profile_payload(
            title="9876")
        if input_dict['shipping_address']['address_line_2'] is None:
            input_dict['shipping_address'].pop('address_line_2')
        input_dict = input_dict['shipping_address']
        customer_profile_response_dict = customer_service.request(
            RequestType.GET,
            customer_profile_address_url + "9786").json()
        print "Expected is", input_dict
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn(
            'title', customer_profile_response_dict.keys(),
            msg='Expected %s in %s' %
                ('shipping_addresses', customer_profile_response_dict.keys()))

    def test_add_new_shipping_address_with_optional_Param(self):
        """ Testing with optional address to add
        new shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload
            (addr1="New River Bridge", addr2="Near Post Office"))
        input_dict = CustomerProfileServicePayload().customer_profile_payload(
            addr1="New River Bridge", addr2="Near Post Office")
        customer_profile_response_dict = customer_service.request(
            RequestType.GET,
            customer_profile_address_url + "9876").json()
        print "Expected is", input_dict
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn(
            'title', customer_profile_response_dict.keys(),
            msg='Expected %s in %s' %
                ('shipping_addresses', customer_profile_response_dict.keys()))


    def test_update_customer_profile_with_address_line_1(self):
        """ Testing with address line_1 to update
        new shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title='cust_new_test', addr1="Hollywood"))
        customer_profile_response_data = customer_profile_response.json()
        updated_val = [data['address_line_1'] for data in
                       customer_profile_response_data["shipping_addresses"] for
                       key, value in data.items()
                       if value == 'cust_new_test'][0]
        print "Expected is", updated_val
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(updated_val, "Hollywood",
                          msg="Expected %s and got %s" %
                              ("Hollywood", updated_val))


    def test_update_customer_profile_with_contact_number(self):
        """ Testing with contact number to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title='cust_new_test', cont_num=94163748392))
        customer_profile_response_data = customer_profile_response.json()
        updated_val = \
            [data['contact_number'] for data in
             customer_profile_response_data["shipping_addresses"]
             for key, value in data.items() if value == 'cust_new_test'][0]
        print "Expected is", updated_val
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(94163748392, updated_val,
                          msg="Expected is %s and got %s" %
                              (94163748392, updated_val))

    def test_update_customer_profile_with_city(self):
        """ Testing with city to update shipping
        address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload
            (title='cust_new_test', city="LA"))
        customer_profile_response_data = customer_profile_response.json()
        updated_val = ''.join(
            [data['city'] for data in
             customer_profile_response_data["shipping_addresses"] for
             key, value in data.items() if value == 'cust_new_test'][0])
        print "Expected is", updated_val
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals('LA', updated_val,
                          msg="Expected is %s and got %s" %
                              ("LA", updated_val))

    def test_update_customer_profile_with_contact_name(self):
        """ Testing with contact name to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title='cust_new_test', contact_name="sagar"))
        customer_profile_response_data = customer_profile_response.json()
        updated_val = ''.join(
            [data['contact_name'] for data in customer_profile_response_data[
                "shipping_addresses"] for
             key, value in data.items() if value == 'cust_new_test'][0])
        print "Expected is", updated_val
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals("sagar", updated_val,
                          msg="Expected is %s and got %s" %
                              ("sagar", updated_val))

    def test_update_customer_profile_with_state(self):
        """ Testing with state name to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title='cust_new_test', state="Texas"))
        customer_profile_response_data = customer_profile_response.json()
        updated_val = ''.join(
            [data['state'] for data in
             customer_profile_response_data["shipping_addresses"] for
             key, value in data.items() if value == 'cust_new_test'][0])
        print "Expected is", updated_val
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(updated_val, 'Texas',
                          msg="Expected is %s and got %s" %
                              (updated_val, "Texas"))

    def test_update_customer_profile_with_zipcode(self):
        """ Testing with zipcode to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title='cust_new_test', zipcode=53235))
        customer_profile_response_data = customer_profile_response.json()
        updated_val = \
            [data['zipcode'] for data in
             customer_profile_response_data["shipping_addresses"] for
             key, value in data.items() if value == 'cust_new_test'][0]
        print "Expected is", updated_val
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(updated_val, 53235,
                          msg="Expected updated_val is %s and got %s" %
                              (updated_val, 53235))

    def test_add_new_shipping_address_with_invalid_customer_id(self):
        """ Testing with mismatch customer_id to add
        new shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, CUSTOMER_SERVICE_URL + str('23eds'),
            payload=CustomerProfileServicePayload().customer_profile_payload(
                addr1="400_NE, River_Bridge", addr2='Near Post Office'))
        customer_profile_response_dict = customer_profile_response.json()
        expected_message = "Customer_id mismatch"
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                    httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_dict['message'], expected_message,
            msg="Expected message %s and got %s" %
                (expected_message, customer_profile_response_dict['message']))

    def test_update_customer_profile_without_title(self):
        """ Testing without title to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "title"))
        customer_profile_response_text = customer_profile_response.json()
        expected_message = 'Shipping address: ' + "title" + ' is not provided'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_text['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_text['message'], expected_message))

    def test_update_customer_profile_without_address_line_1(self):
        """ Testing without address_line_1 to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "address_line_1"))
        customer_profile_response_text = customer_profile_response.json()
        expected_message = 'Shipping address: ' + "address_line_1" + \
                           ' is not provided'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_text['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_text['message'], expected_message))

    def test_update_customer_profile_without_contact_number(self):
        """ Testing without contact number to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "contact_number"))
        customer_profile_response_text = customer_profile_response.json()
        expected_message = 'Shipping address: ' + "contact_number" + \
                           ' is not provided'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_text['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_text['message'], expected_message))

    def test_update_customer_profile_without_city(self):
        """ Testing without city to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "city"))
        customer_profile_response_text = customer_profile_response.json()
        expected_message = 'Shipping address: ' + "city" + ' is not provided'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_text['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_text['message'], expected_message))

    def test_update_customer_profile_without_contact_name(self):
        """ Testing without  contact name to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "contact_name"))
        customer_profile_response_text = customer_profile_response.json()
        expected_message = 'Shipping address: ' + "contact_name" + \
                           ' is not provided'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_text['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_text['message'], expected_message))

    def test_update_customer_profile_without_state(self):
        """ Testing without state to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "state"))
        customer_profile_response_text = customer_profile_response.json()
        expected_message = 'Shipping address: ' + "state" + ' is not provided'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_text['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    def test_update_customer_profile_without_country(self):
        """ Testing without country to update
        shipping address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "country"))
        customer_profile_response_text = customer_profile_response.json()
        expected_message = 'Shipping address: ' + "country" + ' is not provided'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_text['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_text['message'], expected_message))

    def test_update_customer_profile_without_zipcode(self):
        """
        Testing without zipcode to update shipping
        address to the customer profile """
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "zipcode"))
        customer_profile_response_text = customer_profile_response.json()
        expected_message = 'Shipping address: ' + "zipcode" + ' is not provided'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_text['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_text['message'], expected_message))

    """ GET: To get the list of addresses """
    """ Test cases to get the list of addresses of customer """

    def test_list_address_with_customer_id(self):
        """ Test with the valid customer_id to get the list of addresses """
        customer_profile_response = customer_service.request(
            RequestType.GET, customer_profile_url)
        customer_profile_response.dict = customer_profile_response.json()
        print "Response is", customer_profile_response
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

        customer_profile_response = customer_service.request(
            RequestType.GET, CUSTOMER_SERVICE_URL + str(
                customer_service.customerId) + '12')
        customer_profile_response_dict = customer_profile_response.json()
        expected_message = "Customer_id mismatch"
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_dict['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_dict['message'], expected_message))

    def test_list_address_customer_with_invalid_url(self):
        """ Test with the invalid customer_id to get the list of addresses """
        customer_profile_response = customer_service.request(
            RequestType.GET, CUSTOMER_SERVICE_URL + str('12'))
        customer_profile_response_text = customer_profile_response.json()
        expected_message = 'Customer_id mismatch'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_text['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_text['message'], expected_message))

    def test_list_address_customer_profile_without_id(self):
        """ Test without customer_id to get the list of addresses """
        customer_profile_response = customer_service.request(
            RequestType.GET, CUSTOMER_SERVICE_URL)
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 403,
            msg='Expected 403 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn('message', customer_profile_response_dict.keys(),
                      msg="Expected message in %s and got %s" %
                          ('message', customer_profile_response_dict.keys()))

    def test_list_address_customer_profile_with_invalid_token(self):
        """ Test without customer_id to get the list of addresses """

        customer_profile_response = customer_service_invalid_token.request(
            RequestType.GET, CUSTOMER_SERVICE_URL)
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 403,
            msg='Expected 403 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn('message', customer_profile_response_dict.keys(),
                      msg="Expected message in %s and got %s" %
                          ('message', customer_profile_response_dict.keys()))

    """ DELETE: Test cases to delete the customer address with address title """

    def test_delete_address_with_customer(self):
        """ Testing with the valid address title """
        customer_profile_response = customer_service.request(
            RequestType.DELETE, customer_profile_address_url + "1111")
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))

    def test_delete_address_with_wrong_title(self):
        """ Testing with the invalid address title """

        customer_profile_response = customer_service.request(
            RequestType.DELETE, customer_profile_address_url + "XYZ")
        customer_profile_response_dict = customer_profile_response.json()
        expected_message = "Address does not exist"
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 404,
            msg='Expected 404 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_dict['message'], expected_message,
            msg="Expected message is %s and got is %s" %
                (customer_profile_response_dict['message'], expected_message))

    def test_delete_address_with_customer_id_mismatch(self):
        """ Testing with the invalid address title """

        customer_profile_response = customer_service.request(
            RequestType.DELETE,
            customer_profile_url + "24" + "/addresses/Test_Job")
        customer_profile_response_dict = customer_profile_response.json()
        expected_message = "Customer_id mismatch"
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                    httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_dict['message'], expected_message,
            msg="Expected message is %s and got is %s" %
                (customer_profile_response_dict['message'], expected_message))

    """ GET: Test cases to get the particular address details
    of the customer by the address title """

    def test_get_address_title_for_given_customer(self):
        """ Testing with the valid address to get the
        details of the customer """
        customer_profile_response = customer_service.request(
            RequestType.GET, customer_profile_address_url + 'cust_new_test')
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is", customer_profile_response
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
        customer_profile_addresses_url = \
            CUSTOMER_SERVICE_URL + str(customer_service.customerId) + \
            "23" + "/addresses/"
        customer_profile_response = customer_service.request(
            RequestType.GET, customer_profile_addresses_url + "Restore_Job")
        customer_profile_response_dict = customer_profile_response.json()
        expected_message = "Customer_id mismatch"
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_dict['message'], expected_message,
            msg="Expected message is %s and got is %s" %
                (customer_profile_response_dict['message'], expected_message))

    def test_get_address_with_invalid_title(self):
        """ Testing with invalid address title to get the
        details of the customer """
        customer_profile_response = customer_service.request(
            RequestType.GET,
            customer_profile_address_url + str('xyz'))
        customer_profile_response_dict = customer_profile_response.json()
        expected_message = 'Address does not exist'
        print "Expected is", expected_message
        print "Response is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 404,
            msg='Expected 404 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_dict['message'], expected_message,
            msg="Expected message is %s and got is %s" %
                (customer_profile_response_dict['message'], expected_message))

    def test_get_address_with_customer_id_mismatch_with_valid_title(self):
        """ Testing with the mis match customer_id and the valid address
        title to get the details of the customer """
        customer_profile_address_url_change = CUSTOMER_SERVICE_URL + str(
            customer_service.customerId) + ' "/addresses/" '
        customer_profile_response = customer_service.request(
            RequestType.GET,
            customer_profile_address_url_change + "Restore_Job")
        customer_profile_response_dict = customer_profile_response.json()
        expected_message = "Customer_id mismatch"
        print "Expected is", expected_message
        print "Response  is", customer_profile_response
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_dict['message'], expected_message,
            msg="Expected message is %s and got %s" %
                (customer_profile_response_dict['message'], expected_message))
