""" Functional test cases for user profile service """

import unittest
from common.rest_framework import RestAPIHeader, RequestType
from common.config import CUSTOMER_SERVICE_URL
from common.payloads import CustomerProfileServicePayload

customer_rest_obj = RestAPIHeader()
customer_rest_obj_invalid_token = RestAPIHeader(utype='unuser')
customer_profile_url = CUSTOMER_SERVICE_URL + str(customer_rest_obj.cust_id)
customer_profile_address_url = customer_profile_url + "/addresses/"


class CustomerProfilePutTestCases(unittest.TestCase):
    """ Test cases for the PUT method """

    def test_add_new_shipping_address_without_optional_Param(self):
        """ Testing without optional address to add
        new shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        customer_profile_payload
                                        (title="Restore_Job"))
        input_dict = CustomerProfileServicePayload().customer_profile_payload(
            title="Restore_Job")
        if input_dict['shipping_address']['address_line_2'] is None:
            input_dict['shipping_address'].pop('address_line_2')
        input_dict = input_dict['shipping_address']
        out_dict = customer_rest_obj.request(RequestType.GET,
                                             customer_profile_address_url +
                                             "Restore_Job").json()
        self.assertEquals(out.status_code, 200)
        self.assertDictContainsSubset(input_dict, out_dict)

    def test_add_new_shipping_address_with_optional_Param(self):
        """ Testing with optional address to add
        new shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        customer_profile_payload
                                        (addr1="400_New_River_Bridge",
                                         addr2='Near Post Office'))
        input_dict = CustomerProfileServicePayload().customer_profile_payload(
            title="Restore_Job", addr1="400_NE, River_Bridge",
            addr2='Near Post Office')
        out_dict = customer_rest_obj.request(RequestType.GET,
                                             customer_profile_address_url +
                                             "Restore_Job").json()
        input_dict = input_dict['shipping_address']
        self.assertEquals(out.status_code, 200)
        self.assertDictContainsSubset(input_dict, out_dict)

    def test_customer_id_mismatch_error_message(self):
        """ Testing with mismatch customer_id to add
        new shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT,
                                        CUSTOMER_SERVICE_URL + str('23eds'),
                                        payload=CustomerProfileServicePayload().
                                        customer_profile_payload
                                        (addr1="400_NE, River_Bridge",
                                         addr2='Near Post Office'))
        out_dict = out.json()
        message = "Customer_id mismatch"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_update_customer_profile_address_line1_param(self):
        """ Testing with address line_1 to update
        new shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        customer_profile_payload
                                        (title='1111', addr1="Hollywood"))
        self.assertEquals(out.status_code, 200)

    def test_update_customer_profile_contact_number_param(self):
        """ Testing with contact number to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        customer_profile_payload
                                        (title='1111', cont_num=94163748392))
        out_data = out.json()
        upt_val = \
            [data['contact_number'] for data in out_data["shipping_addresses"]
             for key, value in data.items() if value == '1111'][0]
        self.assertEquals(out.status_code, 200)
        self.assertEquals(upt_val, 94163748392)

    def test_update_customer_profile_city_param(self):
        """ Testing with city to update shipping
        address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        customer_profile_payload(
                                            title='1111', city="LA"))
        out_data = out.json()
        upt_val = ''.join(
            [data['city'] for data in out_data["shipping_addresses"] for
             key, value in data.items() if value == '1111'][0])
        self.assertEquals(out.status_code, 200)
        self.assertEquals(upt_val, 'LA')

    def test_update_customer_profile_contact_name_param(self):
        """ Testing with contact name to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        customer_profile_payload(
                                            title='1111', contact_name="sagar"))
        out_data = out.json()
        upt_val = ''.join(
            [data['contact_name'] for data in out_data["shipping_addresses"] for
             key, value in data.items() if value == '1111'][0])
        self.assertEquals(out.status_code, 200)
        self.assertEquals(upt_val, 'sagar')
    #
    def test_update_customer_profile_state_param(self):
        """ Testing with state name to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        customer_profile_payload(
                                            title='1111', state="Texas"))
        out_data = out.json()
        upt_val = ''.join(
            [data['state'] for data in out_data["shipping_addresses"] for
             key, value in data.items() if value == '1111'][0])
        self.assertEquals(out.status_code, 200)
        self.assertEquals(upt_val, 'Texas')

    def test_update_customer_profile_zipcode_param(self):
        """ Testing with zipcode to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        customer_profile_payload(
                                            title='1111', zipcode=53235))
        out_data = out.json()
        upt_val = \
            [data['zipcode'] for data in out_data["shipping_addresses"] for
             key, value in data.items() if value == '1111'][0]
        self.assertEquals(out.status_code, 200)
        self.assertEquals(upt_val, 53235)

    def test_title_missing_parameter(self):
        """ Testing without title to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        delete_payload_parameter(
                                            "title"))
        out_text = out.json()
        string = 'Shipping address: ' + "title" + ' is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_text['message'], string)

    def test_address_line_1_missing_parameter(self):
        """ Testing without address_line_1 to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        delete_payload_parameter(
                                            "address_line_1"))
        out_text = out.json()
        string = 'Shipping address: ' + "address_line_1" + ' is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_text['message'], string)

    def test_contact_number_missing_parameter(self):
        """ Testing without contact number to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        delete_payload_parameter(
                                            "contact_number"))
        out_text = out.json()
        string = 'Shipping address: ' + "contact_number" + ' is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_text['message'], string)

    def test_city_missing_parameter(self):
        """ Testing without city to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        delete_payload_parameter(
                                            "city"))
        out_text = out.json()
        string = 'Shipping address: ' + "city" + ' is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_text['message'], string)

    def test_contact_name_missing_parameter(self):
        """ Testing without  contact name to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        delete_payload_parameter(
                                            "contact_name"))
        out_text = out.json()
        string = 'Shipping address: ' + "contact_name" + ' is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_text['message'], string)

    def test_state_missing_parameter(self):
        """ Testing without state to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        delete_payload_parameter(
                                            "state"))
        out_text = out.json()
        string = 'Shipping address: ' + "state" + ' is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_text['message'], string)

    def test_country_missing_parameter(self):
        """ Testing without country to update
        shipping address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        delete_payload_parameter(
                                            "country"))
        out_text = out.json()
        string = 'Shipping address: ' + "country" + ' is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_text['message'], string)

    def test_zipcode_missing_parameter(self):
        """
        Testing without zipcode to update shipping
        address to the customer profile """
        out = customer_rest_obj.request(RequestType.PUT, customer_profile_url,
                                        payload=CustomerProfileServicePayload().
                                        delete_payload_parameter(
                                            "zipcode"))
        out_text = out.json()
        string = 'Shipping address: ' + "zipcode" + ' is not provided'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_text['message'], string)


class CustomerProfileGetTestCases(unittest.TestCase):
    """ Test cases to get the list of addresses of customer """

    def test_get_customer_with_valid_id(self):
        """ Test with the valid customer_id to get the list of addresses """

        out = customer_rest_obj.request(RequestType.GET, customer_profile_url)
        out_dict = out.json()
        cust_dict_keys = ['company_name', 'customer_id', 'shipping_addresses']
        for key in cust_dict_keys:
            if key not in out_dict.keys():
                assert False
        out_dict = out_dict["shipping_addresses"]
        for item in out_dict:
            input_dict = customer_rest_obj.request(RequestType.GET,
                                                   customer_profile_address_url
                                                   + item['title']).json()
            assert (input_dict[k] == item[k] for k in
                    input_dict) and out.status_code == 200

    def test_customer_id_mismatch_error_message(self):
        """ Test with mis matched customer_id to get the list of addresses """

        out = customer_rest_obj.request(RequestType.GET,
                                        CUSTOMER_SERVICE_URL + str(
                                            customer_rest_obj.cust_id) + '12')
        out_dict = out.json()
        message = "Customer_id mismatch"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_get_customer_with_invalid_url(self):
        """ Test with the invalid customer_id to get the list of addresses """

        out = customer_rest_obj.request(RequestType.GET,
                                        CUSTOMER_SERVICE_URL + str('12'))
        out_dict = out.json()
        message = 'Customer_id mismatch'
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_get_customer_profile_without_id(self):
        """ Test without customer_id to get the list of addresses """

        out = customer_rest_obj.request(RequestType.GET, CUSTOMER_SERVICE_URL)
        out_dict = out.json()
        self.assertEquals(out.status_code, 403)
        self.assertIn('message', out_dict.keys())

    def test_get_customer_profile_with_invalid_token(self):
        """ Test without customer_id to get the list of addresses """

        out = customer_rest_obj_invalid_token.request(RequestType.GET,
                                                      CUSTOMER_SERVICE_URL)
        out_dict = out.json()
        self.assertEquals(out.status_code, 403)
        self.assertIn('message', out_dict.keys())


class CustomerProfileDeleteTestCases(unittest.TestCase):
    """ Test cases to delete the customer address with address title """

    def test_address_deletion_with_given_customer(self):
        """ Testing with the valid address title """
        out = customer_rest_obj.request(RequestType.DELETE,
                                        customer_profile_address_url
                                        + "Test_Job")
        out_dict = out.json()
        out_dict = out_dict["shipping_addresses"]
        for data in out_dict:
            assert "Test_Job" != data['title'] and out.status_code == 200

    def test_delete_address_with_wrong_title(self):
        """ Testing with the invalid address title """

        out = customer_rest_obj.request(RequestType.DELETE,
                                        customer_profile_address_url + "XYZ")
        out_dict = out.json()
        message = "Address does not exist"
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out_dict['message'], message)


class CustomerProfileGetAddressTestCases(unittest.TestCase):
    """ Test cases to get the particular address details
    of the customer by the address title """

    def test_get_address_title_for_given_customer(self):
        """ Testing with the valid address to get the
        details of the customer """
        out = customer_rest_obj.request(RequestType.GET,
                                        customer_profile_address_url + str(
                                            'Restore_Job'))
        output = out.json()
        user_input = CustomerProfileServicePayload().customer_profile_payload(
            title="Restore_Job")
        user_input = user_input["shipping_address"]
        if user_input["address_line_2"] is None:
            user_input.pop("address_line_2")
        assert all(user_input[k] == output[k] for k in user_input)
        self.assertEquals(out.status_code, 200)

    def test_customer_id_mismatch_error_message(self):
        """ Testing with the mis match customer_id to get the
        details of the customer """
        cust_profile_addrs_url = CUSTOMER_SERVICE_URL + str(
            customer_rest_obj.cust_id) + '"/addresses/"'
        out = customer_rest_obj.request(RequestType.GET,
                                        cust_profile_addrs_url + "Restore_Job")
        out_dict = out.json()
        message = "Customer_id mismatch"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)

    def test_get_address_given_customer_invalid_title(self):
        """ Testing with invalid address title to get the
        details of the customer """
        out = customer_rest_obj.request(RequestType.GET,
                                        customer_profile_address_url + str(
                                            'xyz'))
        out_dict = out.json()
        message = 'Address does not exist'
        self.assertEquals(out.status_code, 404)
        self.assertEquals(out_dict['message'], message)

    def test_customer_id_mismatch_with_valid_title(self):
        """ Testing with the mis match customer_id and the valid address
        title to get the details of the customer """
        customer_profile_address_url_change = CUSTOMER_SERVICE_URL + str(
            customer_rest_obj.cust_id) + ' "/addresses/" '
        out = customer_rest_obj.request(RequestType.GET,
                                        customer_profile_address_url_change
                                        + "Restore_Job")
        out_dict = out.json()
        message = "Customer_id mismatch"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], message)


if __name__ == '__main__':
    unittest.main()
