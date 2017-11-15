import unittest
import httplib
from test.shared.rest_framework import RestAPIHeader, RequestType
from test.functional_test_suit.common.config import INVENTORY_SERVICE_URL, \
    get_items_url, update_url
from test.functional_test_suit.common.payloads import Inventoryservicepayload

inventory_service = RestAPIHeader(utype='sysops')


class InventoryServiceTestCases(unittest.TestCase):
    """ Add item class """
    """ POST: Add item into inventory"""

    def test_add_item_with_valid_details(self):
        """ Adding an item with all valid parameters into the inventory """

        expected_dict = Inventoryservicepayload().inventory_additem_payload()

        # Add an item with valid details
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload())
        add_item_response_dict = add_item_response.json()
        print "Response while adding: ", add_item_response.text
        print "Response while fetching: ", expected_dict.keys()
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertIn(
            expected_dict.keys(), add_item_response_dict.keys(),
            msg="Expected %s in %s" %
                (expected_dict.keys(), add_item_response_dict.keys()))

    def test_add_item_with_invalid_item_id(self):
        """ Testing with invalid item id to add an item into the inventory """

        expected_dict = Inventoryservicepayload().inventory_additem_payload(
            item_id='1@d@323')

        # Add an item with valid details
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                item_id='1@d@323'))
        add_item_response_dict = add_item_response.json()
        print "Response while adding: ", add_item_response.text
        print "Response while fetching: ", expected_dict.keys()
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (add_item_response.status_code, 
                 httplib.responses[add_item_response.status_code]))
        self.assertIn(
            expected_dict.keys(), add_item_response_dict.keys(),
            msg="Expected %s in %s" %
                (expected_dict.keys(), add_item_response_dict.keys()))

    def test_add_item_with_invalid_hw_model(self):
        """ Testing with invalid hardware_model to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with invalid hardware model
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                hw_model='@dry@'))
        add_item_response_dict = add_item_response.json()
        print "Response while adding: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
            (error_message, add_item_response_dict['message']))

    def test_add_item_with_invalid_hw_number(self):
        """ Testing with invalid hardware_number to
        add an item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with invalid hardware number
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                hw_number='5tg#'))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))

    def test_add_item_with_invalid_mac_address(self):
        """ Testing with invalid mac_address to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with invalid mac address
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                mac_address='tg$cb(wdui%'))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
            (error_message, add_item_response_dict['message']))

    def test_add_item_with_invalid_storage_capacity(self):
        """ Testing with invalid storage_capacity to add
        an item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with invalid storage capacity
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                storage_capacity=-300))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))

    def test_add_item_with_invalid_item_status(self):
        """ Testing with invalid item_status to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with invalid item status
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                item_status='NEW@##*'))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))

    def test_add_item_with_invalid_remarks(self):
        """ Testing with invalid data for remarks to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with invalid remarks
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                remarks='AS #@'))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))

    def test_add_item_with_invalid_order_id(self):
        """ Testing with invalid order_id to add an item into the inventory """

        expected_dict = Inventoryservicepayload().inventory_additem_payload(
            order_id='1@ *')

        # Add an item with valid details
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            order_id='1@ *'))
        add_item_response_dict = add_item_response.json()
        print "Response while adding: ", add_item_response.text
        print "Response while fetching: ", expected_dict.keys()
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertIn(
            expected_dict.keys(), add_item_response_dict.keys(),
            msg="Expected %s in %s" %
                (expected_dict.keys(), add_item_response_dict.keys()))

    def test_add_item_with_invalid_storage_array_model(self):
        """ Testing with invalid storage_array_model to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with invalid storage array model
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_array_model='sv *cy%@'))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))

    def test_add_item_with_invalid_storage_array_type(self):
        """ Testing with invalid storage_array_type to add
        an item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with invalid storage array type
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_array_type='asd# @'))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))

    def test_add_item_without_item_id(self):
        """ Testing with response item_id to add an item into the inventory """

        message = "Seed Box added successfully!"

        # Add an item without item id
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            item_id=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (message, add_item_response_dict['message']))

    def test_add_item_without_hw_model(self):
        """ Testing with response hardware_model to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item without hardware model
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            hw_model=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s (%s)" % (
                            add_item_response.status_code,
                            httplib.responses[add_item_response.status_code]))
        self.assertEquals(error_message, add_item_response_dict['message'],
                          msg=" expected message is %s and got is %s" %
                              (error_message, add_item_response_dict['message']))

    def test_add_item_without_hw_number(self):
        """ Testing with empty hardware_number to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item without hardware number
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            hw_number=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s (%s)" % (
                            add_item_response.status_code,
                            httplib.responses[add_item_response.status_code]))
        self.assertEquals(error_message, add_item_response_dict['message'],
                          msg=" expected message is %s and got is %s" %
                              (error_message, add_item_response_dict['message']))

    def test_add_item_without_mac_address(self):
        """ Testing without content for mac_address to add an item
        into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item without mac address
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            mac_address=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s (%s)" % (
                            add_item_response.status_code,
                            httplib.responses[add_item_response.status_code]))
        self.assertEquals(error_message, add_item_response_dict['message'],
                          msg=" expected message is %s and got is %s" %
                              (error_message, add_item_response_dict['message']))

    def test_add_item_without_storage_capacity(self):
        """ Testing without content for mac_address to
        add an item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item without storage capacity
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_capacity=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s (%s)" % (
                            add_item_response.status_code,
                            httplib.responses[add_item_response.status_code]))
        self.assertEquals(error_message, add_item_response_dict['message'],
                          msg=" expected message is %s and got is %s" %
                              (error_message, add_item_response_dict['message']))

    def test_add_item_without_item_status(self):
        """ Testing without status of item to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with out item status
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            item_status=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))

    def test_add_item_without_remarks(self):
        """ Testing with response content for remarks to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item without remarks
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            remarks=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s (%s)" % (
                            add_item_response.status_code,
                            httplib.responses[add_item_response.status_code]))
        self.assertEquals(error_message, add_item_response_dict['message'],
                          msg=" expected message is %s and got is %s" %
                              (error_message, add_item_response_dict['message']))

    def test_add_item_without_storage_array_type(self):
        """ Testing with response storage_array_model to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with out storage array type
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_array_type=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertEquals(error_message, add_item_response_dict['message'],
                          msg=" expected message is %s and got is %s" %
                              (error_message, add_item_response_dict['message']))

    def test_add_item_without_storage_array_model(self):
        """ Testing with  response storage_array_type to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"

        # Add an item with out storage array model
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_array_model=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertEquals(error_message, add_item_response_dict['message'],
                          msg=" expected message is %s and got is %s" %
                              (error_message, add_item_response_dict['message']))

    def test_add_item_without_order_id(self):
        """ Testing with response order_id to add an item into the inventory """

        message = "Seed Box added successfully!"

        # Add an item without order id
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                order_id=''))
        add_item_response_dict = add_item_response.json()
        print "Response is: ", add_item_response.text
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertEquals(message, add_item_response_dict['message'],
                          msg=" expected message is %s and got is %s" %
                              (message, add_item_response_dict['message']))

    """ check the item in an inventory """
    """ Method:GET """

    def test_item_availability_with_valid_hw_model(self):
        """ Checking the item availability with valid hardware_model """

        # Check item availability in the inventory with hardware model
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('hw_model', 'ASDF123'))
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (item_availability_response.status_code,
                 httplib.responses[item_availability_response.status_code]))
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expected %s in %s" %
                ('items', item_availability_response.json().keys()))

    def test_item_availability_with_valid_item_id(self):
        """ Checking the item availability with valid item_id """

        # Check item availability in the inventory with item id
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_id', 'NOOR'))
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expected %s in %s" %
                ('items', item_availability_response.json().keys()))

    def test_item_availability_with_valid_storage_capacity(self):
        """ Checking the item availability with valid storage_capacity """

        # Check item availability in the inventory with storage capacity
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('storage_capacity', '299'))
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expected %s in %s" %
                ('items', item_availability_response.json().keys()))

    def test_item_availability_with_valid_item_status(self):
        """ Checking the item availability with valid item_status """

        # Check item availability in the inventory with hardware model
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_status', 'NEW'))
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expected %s in %s" %
                ('items', item_availability_response.json().keys()))

    def test_item_availability_with_invalid_hw_model(self):
        """ Checking the item availability with invalid hardware_model """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory with invalid hardware model
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('hw_model', 'sf1@%563 7'))
        item_availability_response_dict = item_availability_response.json()
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))

    def test_item_availability_with_invalid_item_id(self):
        """ Checking the item availability with invalid item_id"""

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory with invalid item id
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_id', 'asfyd 227@'))
        item_availability_response_dict = item_availability_response.json()
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))

    def test_item_availability_with_invalid_item_status(self):
        """ Checking the item availability with invalid item_status """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory with invalid item status
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_status', 'asdf'))
        item_availability_response_dict = item_availability_response.json()
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))

    def test_item_availability_without_hw_model(self):
        """ Checking the item availability without hardware_model """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory without hardware model
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('hw_model', ''))
        item_availability_response_dict = item_availability_response.json()
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))

    def test_item_availability_without_item_id(self):
        """ Checking the item availability without item_id """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory without item id
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_id', ''))
        item_availability_response_dict = item_availability_response.json()
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))

    def test_item_availability_without_storage_capacity(self):
        """ Checking the item availability without storage_capacity """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory without storage capacity
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('storage_capacity', ''))
        item_availability_response_dict = item_availability_response.json()
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message,
            item_availability_response['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))
    def test_item_availability_without_item_status(self):
        """ Checking the item availability without item_status """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory without item status
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_status', ''))
        item_availability_response_dict = item_availability_response.json()
        error_message = "Invalid attribute value!"
        print "Response is: ", item_availability_response.text
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message,
            item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))

    """ update the status of an item """

    """ Method:PUT"""

    def test_update_item_with_valid_item_id(self):
        """ Updating the item_status with valid item_id and sku """

        expected_message = ["Item has been updated in Inventory"]

        # Update inventory with valid item id and sku
        update_item_status_response = inventory_service.request(
            RequestType.PUT, update_url('NOOR'),
            payload=Inventoryservicepayload().inventory_update_payload())
        update_item_status_response_dict = update_item_status_response.json()
        print "Response is: ", update_item_status_response.text
        self.assertEquals(
            update_item_status_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                update_item_status_response.status_code,
                httplib.responses[update_item_status_response.status_code]))
        self.assertEquals(
            expected_message,
            update_item_status_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (expected_message, update_item_status_response_dict['message']))

    def test_update_item_without_sku(self):
        """ Updating the item_status with
        valid item_id and with response sku """

        error_message = "Could not update database with expected values : " \
                        "No uid/sku found to update"

        # Update an inventory without sku
        update_item_status_response = inventory_service.request(
            RequestType.PUT, update_url('NOOR'),
            payload=Inventoryservicepayload().inventory_update_payload(
                item_status='newly', sku=''))
        update_item_status_response_dict = update_item_status_response.json()
        print "Response is: ", update_item_status_response.text
        self.assertEquals(
            update_item_status_response.status_code, 500,
            msg="Expected code is 500 and got is %s (%s)" % (
                update_item_status_response.status_code,
                httplib.responses[update_item_status_response.status_code]))
        self.assertEquals(
            error_message,
            update_item_status_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, update_item_status_response_dict['message']))
