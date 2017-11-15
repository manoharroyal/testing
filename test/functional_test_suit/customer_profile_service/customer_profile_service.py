""" Functional test cases for customer profile service """

import unittest2
import httplib
from test.shared.rest_framework import RequestType, RestAPIHeader
from test.functional_test_suit.common.config import CUSTOMER_SERVICE_URL
from test.functional_test_suit.common.payloads import \
    CustomerProfileServicePayload

customer_service = RestAPIHeader(utype='customer')
customer_service_invalid_token = RestAPIHeader(utype='invalid')
customer_profile_url = CUSTOMER_SERVICE_URL + str(customer_service.customerId)
customer_profile_address_url = customer_profile_url + "/addresses/"


class CustomerProfileTestCases(unittest2.TestCase):
    """ Test cases for the creation of customer profile
    by passing the input parameters """
    """ PUT : Create/Update customer profile """

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
            customer_profile_address_url + "9786").json()
        print "Response while creating: ", customer_profile_response.text
        print "Response while fetching: ", customer_profile_response_dict.text
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn(
            'title', customer_profile_response_dict.keys(),
            msg='Expected %s in %s' %
                ('shipping_addresses', customer_profile_response_dict.keys()))

    def test_add_new_shipping_address_with_address_line2(self):
        """ Testing with optional address to add
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
        print "Response while creating: ", customer_profile_response.text
        print "Response while fetching: ", customer_profile_response_dict.text
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertIn(
            'title', customer_profile_response_dict.keys(),
            msg='Expected %s in %s' %
                ('shipping_addresses', customer_profile_response_dict.keys()))

    def test_add_new_shipping_address_with_invalid_customer_id(self):
        """ Testing with mismatch customer_id to add
        new shipping address to the customer profile """

        expected_message = "Customer_id mismatch"

        # Create an address with invalid customer id
        customer_profile_response = customer_service.request(
            RequestType.PUT,
            CUSTOMER_SERVICE_URL + str('23eds'),
            payload=CustomerProfileServicePayload().customer_profile_payload(
                addr1="400_NE, River_Bridge", addr2='Near Post Office'))
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            customer_profile_response_dict['message'], expected_message,
            msg="Expected message %s and got %s" %
                (expected_message, customer_profile_response_dict['message']))

    def test_update_customer_profile_with_address_line_1(self):
        """ Testing with address line_1 to update
        new shipping address to the customer profile """

        address_line_1 = 'Hollywood'
        # Update the address with address_line_1
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title='cust_new_test', addr1=address_line_1))
        customer_profile_response_data = customer_profile_response.json()

        # Getting the updated value
        updated_val = [data['address_line_1'] for data in
                       customer_profile_response_data["shipping_addresses"] for
                       key, value in data.items()
                       if value == 'cust_new_test'][0]
        print "Response while updating: ", customer_profile_response.text
        print "Response while fetching: ", updated_val
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            updated_val, address_line_1,
            msg="Expected %s and got %s" % (address_line_1, updated_val))

    def test_update_customer_profile_with_contact_number(self):
        """ Testing with contact number to update
        shipping address to the customer profile """

        contact_number = 9416345786
        # Update the address with contact number
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title='cust_new_test', cont_num=contact_number))
        customer_profile_response_data = customer_profile_response.json()

        # Getting the updated value
        updated_val = [data['contact_number'] for data in
                       customer_profile_response_data["shipping_addresses"] for
                       key, value in data.items()
                       if value == 'cust_new_test'][0]
        print "Response while updating: ", customer_profile_response.text
        print "Response while fetching: ", updated_val
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            contact_number, updated_val,
            msg="Expected is %s and got %s" % (contact_number, updated_val))

    def test_update_customer_profile_with_city(self):
        """ Testing with city to update shipping
        address to the customer profile """

        city = 'LA'
        # Update the address with city
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload
            (title='cust_new_test', city=city))
        customer_profile_response_data = customer_profile_response.json()

        # Getting the updated value
        updated_val = ''.join([data['city'] for data in
                    customer_profile_response_data["shipping_addresses"] for
                    key, value in data.items() if value == 'cust_new_test'][0])
        print "Response while updating: ", customer_profile_response.text
        print "Response while fetching: ", updated_val
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            city, updated_val,
            msg="Expected is %s and got %s" % (city, updated_val))

    def test_update_customer_profile_with_contact_name(self):
        """ Testing with contact name to update
        shipping address to the customer profile """

        contact_name = 'sagar'
        # Update the address with city
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload
            (title='cust_new_test', contact_name=contact_name))
        customer_profile_response_data = customer_profile_response.json()

        # Getting the updated value
        updated_val = ''.join(
            [data['contact_name'] for data in customer_profile_response_data[
                "shipping_addresses"] for
             key, value in data.items() if value == 'cust_new_test'][0])
        print "Response while updating: ", customer_profile_response.text
        print "Response while fetching: ", updated_val
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg="Expected 200 and got %s (%s)" %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            contact_name, updated_val,
            msg="Expected is %s and got %s" % (contact_name, updated_val))

    def test_update_customer_profile_with_state(self):
        """ Testing with state name to update
        shipping address to the customer profile """

        state = 'Texas'
        # Update the address with state
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title='cust_new_test', state=state))
        customer_profile_response_data = customer_profile_response.json()

        # Getting the updated value
        updated_val = ''.join(
            [data['state'] for data in
             customer_profile_response_data["shipping_addresses"] for
             key, value in data.items() if value == 'cust_new_test'][0])
        print "Response while updating: ", customer_profile_response.text
        print "Response while fetching: ", updated_val
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            updated_val, state,
            msg="Expected is %s and got %s" % (state, updated_val))

    def test_update_customer_profile_with_zipcode(self):
        """ Testing with zipcode to update
        shipping address to the customer profile """

        zipcode = 53535
        # Update the address with zip code
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().customer_profile_payload(
                title='cust_new_test', zipcode=zipcode))
        customer_profile_response_data = customer_profile_response.json()

        # Getting the updated value
        updated_val = [data['zipcode'] for data in
                       customer_profile_response_data["shipping_addresses"] for
                       key, value in data.items()
                       if value == 'cust_new_test'][0]
        print "Response is: ", customer_profile_response.text
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            zipcode, updated_val,
            msg="Expected updated_val is %s and got %s" %
                (zipcode, updated_val))

    def test_update_customer_profile_without_title(self):
        """ Testing without title to update
        shipping address to the customer profile """

        expected_message = 'Shipping address: ' + "title" + ' is not provided'

        # Update the address without title
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "title"))
        customer_profile_response_text = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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
        """ Testing without address_line_1 to update
        shipping address to the customer profile """

        expected_message = 'Shipping address: ' + "address_line_1" + ' is not provided'

        # Update the address without address line1
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "address_line_1"))
        customer_profile_response_text = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message,  customer_profile_response_text['message']))

    def test_update_customer_profile_without_contact_number(self):
        """ Testing without contact number to update
        shipping address to the customer profile """

        expected_message = 'Shipping address: ' + "contact_number" + ' is not provided'

        # Update the address without contact number
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "contact_number"))
        customer_profile_response_text = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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
        """ Testing without city to update
        shipping address to the customer profile """

        expected_message = 'Shipping address: ' + "city" + ' is not provided'

        # Update the address without city
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "city"))
        customer_profile_response_text = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    def test_update_customer_profile_without_contact_name(self):
        """ Testing without  contact name to update
        shipping address to the customer profile """

        expected_message = 'Shipping address: ' + "contact_name" + ' is not provided'

        # Update the address without contact name
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "contact_name"))
        customer_profile_response_text = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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
        """ Testing without state to update
        shipping address to the customer profile """

        expected_message = 'Shipping address: ' + "state" + ' is not provided'

        # Update the address without state
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "state"))
        customer_profile_response_text = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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
        """ Testing without country to update
        shipping address to the customer profile """

        expected_message = 'Shipping address: ' + "country" + ' is not provided'

        # Update the address without country
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "country"))
        customer_profile_response_text = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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
        Testing without zipcode to update shipping
        address to the customer profile """

        expected_message = 'Shipping address: ' + "zipcode" + ' is not provided'

        # Update the address without zip code
        customer_profile_response = customer_service.request(
            RequestType.PUT, customer_profile_url,
            payload=CustomerProfileServicePayload().delete_payload_parameter(
                "zipcode"))
        customer_profile_response_text = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_text['message'],
            msg="Expected message is %s and got %s" %
                (expected_message, customer_profile_response_text['message']))

    """ GET: To get the list of addresses """
    """ Test cases to get the list of addresses of customer """

    def test_list_address_with_customer_id(self):
        """ Test with the valid customer_id to get the list of addresses """

        # Get the list of addresses of customer with customer id
        customer_profile_response = customer_service.request(
            RequestType.GET, customer_profile_url)
        customer_profile_response.dict = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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
        print "Response is: ", customer_profile_response.text
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

        expected_message = 'Customer_id mismatch'

        # Get the list of addresses of customer with invalid url
        customer_profile_response = customer_service.request(
            RequestType.GET, CUSTOMER_SERVICE_URL + str('12'))
        customer_profile_response_text = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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

        # Get the list of addresses of customer without customer id
        customer_profile_response = customer_service.request(
            RequestType.GET, CUSTOMER_SERVICE_URL)
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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

        # Get the list of addresses of customer with invalid token
        customer_profile_response = customer_service_invalid_token.request(
            RequestType.GET, CUSTOMER_SERVICE_URL)
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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

        message = "address is deleted successfully"

        # Delete address with valid title
        customer_profile_response = customer_service.request(
            RequestType.DELETE, customer_profile_address_url + "1111")
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
        self.assertEquals(
            customer_profile_response.status_code, 200,
            msg='Expected 200 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            message, customer_profile_response_dict['message'],
            msg="Expected %s and got is %s" %
                (message, customer_profile_response_dict['message']))

    def test_delete_address_with_wrong_title(self):
        """ Testing with the invalid address title """

        expected_message = "Address does not exist"

        # Delete address with valid wrong title
        customer_profile_response = customer_service.request(
            RequestType.DELETE, customer_profile_address_url + "XYZ")
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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
        print "Response is: ", customer_profile_response.text
        self.assertEquals(
            customer_profile_response.status_code, 400,
            msg='Expected 400 and got %s (%s)' %
                (customer_profile_response.status_code,
                    httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, customer_profile_response_dict['message']))

    """ GET: Test cases to get the particular address details
    of the customer by the address title """

    def test_get_address_details_for_given_customer(self):
        """ Testing with the valid address to get the
        details of the customer """

        # Get the address details with valid title
        customer_profile_response = customer_service.request(
            RequestType.GET, customer_profile_address_url + 'cust_new_test')
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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
            CUSTOMER_SERVICE_URL + str(customer_service.customerId) + "23" + "/addresses/"
        customer_profile_response = customer_service.request(
            RequestType.GET, customer_profile_addresses_url + "Restore_Job")
        customer_profile_response_dict = customer_profile_response.json()
        print "Response is: ", customer_profile_response.text
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
        print "Response is: ", customer_profile_response.text
        self.assertEquals(
            customer_profile_response.status_code, 404,
            msg='Expected 404 and got %s (%s)' %
                (customer_profile_response.status_code,
                 httplib.responses[customer_profile_response.status_code]))
        self.assertEquals(
            expected_message, customer_profile_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, customer_profile_response_dict['message']))

    def test_get_address_with_customer_id_mismatch_with_valid_title(self):
        """ Testing with the mis match customer_id and the valid address
        title to get the details of the customer """

        expected_message = "Customer_id mismatch"

        # Get the address details with mismatched customer id and valid title
        customer_profile_address_url_change = CUSTOMER_SERVICE_URL + str(
            customer_service.customerId) + ' "/addresses/" '
        customer_profile_response = customer_service.request(
            RequestType.GET,
            customer_profile_address_url_change + "Restore_Job")
        customer_profile_response_dict = customer_profile_response.json()
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
