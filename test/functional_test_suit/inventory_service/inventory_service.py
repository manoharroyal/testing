import unittest
from api_functional_testing.test.shared.rest_framework import RestAPIHeader, \
    RequestType
from api_functional_testing.test.functional_test_suit.common.config import \
    INVENTORY_SERVICE_URL, get_items_url, update_url
from api_functional_testing.test.functional_test_suit.common.payloads import\
            Inventoryservicepayload

inventory_service = RestAPIHeader()


class InventoryServiceTestcases(unittest.TestCase):
    """ Add item class """
    # POST: Add item into inventory

    def test_add_item_with_valid_details(self):
        """ Adding an item with all valid parameters into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload())
        input_dict = Inventoryservicepayload().inventory_additem_payload(self)
        response_dict = add_item_response.json()
        self.assertEquals(add_item_response.status_code, 200,
                          msg="Expected code is 200 and got is %s" %
                              add_item_response.status_code)
        self.assertIn(response_dict, input_dict,
                      msg="Expected %s in %s" % (response_dict, input_dict))

    def test_add_item_with_invalid_item_id(self):
        """ Testing with invalid item id to add an item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                item_id='1@d@323'))
        input_dict = Inventoryservicepayload().inventory_additem_payload(
            item_id='1@d@323')
        response_dict = add_item_response.json()
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s" %
                add_item_response.status_code)
        self.assertIn(response_dict, input_dict,
                      msg="Expected %s in %s" % (response_dict, input_dict))

    def test_add_item_with_invalid_hw_model(self):
        """ Testing with invalid hardware_model to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                hw_model='@dry@'))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_with_invalid_hw_number(self):
        """ Testing with invalid hardware_number to
        add an item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                hw_number='5tg#'))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_with_invalid_mac_addrrss(self):
        """ Testing with invalid mac_address to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                mac_address='tg$cb(wdui%'))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_with_invalid_storage_capacity(self):
        """ Testing with invalid storage_capacity to add
        an item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                storage_capacity=-300))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_with_invalid_itemstatus(self):
        """ Testing with invalid item_status to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                item_status='NEW@##*'))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_with_invalid_remarks(self):
        """ Testing with invalid data for remarks to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                remarks='AS #@'))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_with_invalid_order_id(self):
        """ Testing with invalid order_id to add an item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            order_id='1@ * '))
        self.assertEquals(add_item_response.status_code, 200,
                          msg="Expected code is 200 and got is %s" %
                              add_item_response.status_code)

    def test_add_item_with_invalid_storage_array_model(self):
        """ Testing with invalid storage_array_model to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_array_model='sv *cy%@'))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_with_invalid_storage_array_type(self):
        """ Testing with invalid storage_array_type to add
        an item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_array_type='asd# @'))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_item_id(self):
        """ Testing with response item_id to add an item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            item_id=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_hw_model(self):
        """ Testing with response hardware_model to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            hw_model=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_hw_number(self):
        """ Testing with empty hardware_number to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            hw_number=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_mac_address(self):
        """ Testing without content for mac_address to add an item
        into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            mac_address=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_storage_capacity(self):
        """ Testing without content for mac_address to
        add an item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_capacity=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_item_status(self):
        """ Testing without status of item to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            item_status=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_remarks(self):
        """ Testing with response content for remarks to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            remarks=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_storage_array_type(self):
        """ Testing with response storage_array_model to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_array_type=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_storage_array_model(self):
        """ Testing with  response storage_array_type to add an
        item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                                            storage_array_model=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    def test_add_item_without_order_id(self):
        """ Testing with response order_id to add an item into the inventory """

        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=Inventoryservicepayload().inventory_additem_payload(
                order_id=''))
        response_dict = add_item_response.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(add_item_response.status_code, 400,
                          msg="Expected code is 400 and got is %s" %
                              add_item_response.status_code)
        self.assertEquals(response_dict['message'], error_message,
                          msg=" expected message is %s and got is %s" %
                              (error_message, response_dict['message']))

    """ check the item in an inventory """
    """ Method:GET """

    def test_item_availability_with_valid_hw_model(self):
        """ Checking the item availability with valid hardware_model """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('hw_model', 'ASDF123'))
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s" %
                item_availability_response.status_code)
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expecting %s in %s" %
                ('items', item_availability_response.json().keys()))

    def test_item_availability_with_valid_item_id(self):
        """ Checking the item availability with valid item_id """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_id', 'NOOR'))
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s" %
                item_availability_response.status_code)
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expecting %s in %s" %
                ('items', item_availability_response.json().keys()))

    def test_item_availability_with_valid_storage_capacity(self):
        """ Checking the item availability with valid storage_capacity """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('storage_capacity', '299'))
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s" %
                item_availability_response.status_code)
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expecting %s in %s" %
                ('items', item_availability_response.json().keys()))

    def test_item_availability_with_valid_item_status(self):
        """ Checking the item availability with valid item_status """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_status', 'NEW'))
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s" %
                item_availability_response.status_code)
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expectiong %s in %s" %
                ('items', item_availability_response.json().keys()))

    def test_item_availability_with_invalid_hw_model(self):
        """ Checking the item availability with invalid hardware_model """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('hw_model', 'sf1@%563 7'))
        response_dict = item_availability_response.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s" %
                item_availability_response.status_code)
        self.assertEquals(
            response_dict['message'], error_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], error_message))

    def test_item_availability_with_invalid_item_id(self):
        """ Checking the item availability with invalid item_id"""

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_id', 'asfyd 227@'))
        response_dict = item_availability_response.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s" %
                item_availability_response.status_code)
        self.assertEquals(
            response_dict['message'], error_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], error_message))

    def test_item_availability_with_invalid_item_status(self):
        """ Checking the item availability with invalid item_status """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_status', 'asdf'))
        response_dict = item_availability_response.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s" %
                item_availability_response.status_code)
        self.assertEquals(
            response_dict['message'], error_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], error_message))

    def test_item_availability_without_hw_model(self):
        """ Checking the item availability without hardware_model """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('hw_model', ''))
        response_dict = item_availability_response.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s" %
                item_availability_response.status_code)
        self.assertEquals(
            response_dict['message'], error_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], error_message))

    def test_item_availability_without_item_id(self):
        """ Checking the item availability without item_id """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_id', ''))
        response_dict = item_availability_response.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s" %
                item_availability_response.status_code)
        self.assertEquals(
            response_dict['message'], error_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], error_message))

    def test_item_availability_without_storage_capacity(self):
        """ Checking the item availability without storage_capacity """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('storage_capacity', ''))
        response_dict = item_availability_response.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s" %
                item_availability_response.status_code)
        self.assertEquals(
            response_dict['message'], error_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], error_message))

    def test_item_availability_without_item_status(self):
        """ Checking the item availability without item_status """

        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_status', ''))
        response_dict = item_availability_response.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s" %
                item_availability_response.status_code)
        self.assertEquals(
            response_dict['message'], error_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], error_message))

    """ update the status of an item """

    """ Method:PUT"""

    def test_update_item_with_valid_item_id(self):
        """ Updating the item_status with valid item_id and sku """

        update_item_status_response = inventory_service.request(
            RequestType.PUT, update_url('NOOR'),
            payload=Inventoryservicepayload().inventory_update_payload())
        response_dict = update_item_status_response.json()
        expected_message = ["Item has been updated in Inventory"]
        self.assertEquals(
            update_item_status_response.status_code, 200,
            msg="Expected code is 200 and got is %s" %
                update_item_status_response.status_code)
        self.assertEquals(
            response_dict['message'], expected_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], expected_message))

    def test_update_item_without_sku(self):
        """ Updating the item_status with
        valid item_id and with response sku """

        update_item_status_response = inventory_service.request(
            RequestType.PUT, update_url('NOOR'),
            payload=Inventoryservicepayload().inventory_update_payload(
                item_status='newly', sku=''))
        response_dict = update_item_status_response.json()
        error_message = "Could not update database with expected values : " \
                        "No uid/sku found to update"
        self.assertEquals(
            update_item_status_response.status_code, 500,
            msg="Expected code is 500 and got is %s" %
                update_item_status_response.status_code)
        self.assertEquals(
            response_dict['message'], error_message,
            msg="Expected message is %s and got is %s" %
                (response_dict['message'], error_message))
