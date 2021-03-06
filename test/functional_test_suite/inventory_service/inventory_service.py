""" Functional test cases for inventory service """
import logging
import unittest
import httplib
from test.shared.rest_framework import RestAPI, RequestType, path
from test.functional_test_suite.common.config import INVENTORY_SERVICE_URL
from test.functional_test_suite.common.config import get_items_url
from test.functional_test_suite.common.config import update_item_url
from test.functional_test_suite.common.config import initialize_logger

from test.functional_test_suite.inventory_service.inventory_service_payloads import InventoryServicePayload

inventory_service = RestAPI(utype='sysops')
initialize_logger(path + '/../../logs/inventory_service.log')


class InventoryServiceTestCases(unittest.TestCase):
    """ Add item class """
    """ POST: Add item into inventory"""

    def test_add_item_with_valid_details(self):
        """ Adding an item with all valid parameters into the inventory """

        # Add an item with valid details
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=InventoryServicePayload().inventory_additem_payload())
        add_item_response_dict = add_item_response.json()
        logging.info('test_add_item_with_valid_details')
        logging.info('Url is %s', INVENTORY_SERVICE_URL)
        logging.info('Request is %s',
                     InventoryServicePayload().inventory_additem_payload())
        logging.info('Response is %s', add_item_response.text)
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertIn(
            'created_at', add_item_response_dict.keys(),
            msg="Expected %s in %s" %
                ('created_at', add_item_response_dict.keys()))
        logging.info('test case executed successfully')

    def test_add_item_with_invalid_storage_capacity(self):
        """ Testing with invalid storage_capacity to add
        an item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters : " \
                        "Invalid storage_capacity value."

        # Add an item with invalid storage capacity
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=InventoryServicePayload().inventory_additem_payload(
                storage_capacity=-300))
        add_item_response_dict = add_item_response.json()
        logging.info('test_add_item_with_invalid_storage_capacity')
        logging.info('Url is %s', INVENTORY_SERVICE_URL)
        logging.info('Request is %s',
                     InventoryServicePayload().inventory_additem_payload(
                         storage_capacity=-300))
        logging.info('Response is %s', add_item_response.text)
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))
        logging.info('test case executed successfully')

    def test_add_item_without_item_id(self):
        """ Testing with response item_id to add an item into the inventory """

        message = "Seed Box added successfully!"

        # Add an item without item id
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=InventoryServicePayload().inventory_additem_payload(
                                            item_id=''))
        add_item_response_dict = add_item_response.json()
        logging.info('test_add_item_without_item_id')
        logging.info('Url is %s', INVENTORY_SERVICE_URL)
        logging.info('Request is %s',
                     InventoryServicePayload().inventory_additem_payload(
                         item_id=''))
        logging.info('Response is %s', add_item_response.text)
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (message, add_item_response_dict['message']))
        logging.info('test case executed successfully')

    def test_add_item_without_storage_capacity(self):
        """ Testing without content for mac_address to
        add an item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters : " \
                        "Invalid storage_capacity value"

        # Add an item without storage capacity
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=InventoryServicePayload().inventory_additem_payload(
                                            storage_capacity=''))
        add_item_response_dict = add_item_response.json()
        logging.info('test_add_item_without_storage_capacity')
        logging.info('Url is %s', INVENTORY_SERVICE_URL)
        logging.info('Request is %s',
                     InventoryServicePayload().inventory_additem_payload(
                         storage_capacity=''))
        logging.info('Response is %s', add_item_response.text)
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))
        logging.info('test case executed successfully')

    def test_add_item_without_item_status(self):
        """ Testing without status of item to add an
        item into the inventory """

        error_message = "Could not validate the input, " \
                        "please send the correct input parameters : " \
                        "Item status is not valid"

        # Add an item with out item status
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=InventoryServicePayload().inventory_additem_payload(
                                            item_status=None))
        add_item_response_dict = add_item_response.json()
        logging.info('test_add_item_without_item_status')
        logging.info('Url is %s', INVENTORY_SERVICE_URL)
        logging.info('Request is %s',
                     InventoryServicePayload().inventory_additem_payload(
                         item_status=None))
        logging.info('Response is %s', add_item_response.text)
        self.assertEquals(
            add_item_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" %
                (add_item_response.status_code,
                 httplib.responses[add_item_response.status_code]))
        self.assertEquals(
            error_message, add_item_response_dict['message'],
            msg=" expected message is %s and got is %s" %
                (error_message, add_item_response_dict['message']))
        logging.info('test case executed successfully')

    def test_add_item_without_order_id(self):
        """ Testing with response order_id to add an item into the inventory """

        message = "Seed Box added successfully!"

        # Add an item without order id
        add_item_response = inventory_service.request(
            RequestType.POST, INVENTORY_SERVICE_URL,
            payload=InventoryServicePayload().inventory_additem_payload(
                order_id=''))
        add_item_response_dict = add_item_response.json()
        logging.info('test_add_item_without_order_id')
        logging.info('Url is %s', INVENTORY_SERVICE_URL)
        logging.info('Request is %s',
                     InventoryServicePayload().inventory_additem_payload(
                         order_id=''))
        logging.info('Response is %s', add_item_response.text)
        self.assertEquals(
            add_item_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (add_item_response.status_code,
                    httplib.responses[add_item_response.status_code]))
        self.assertEquals(message, add_item_response_dict['message'],
                          msg=" expected message is %s and got is %s" %
                              (message, add_item_response_dict['message']))
        logging.info('test case executed successfully')

    """ check the item in an inventory """
    """ Method:GET """

    def test_item_availability_with_valid_hw_model(self):
        """ Checking the item availability with valid hardware_model """

        # Check item availability in the inventory with hardware model
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url(param='hw_model', value='ASDF123'))
        logging.info('test_item_availability_with_valid_hw_model')
        logging.info('Url is %s', get_items_url(param='hw_model',
                                                value='ASDF123'))
        logging.info('Response is %s', item_availability_response.text)
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" %
                (item_availability_response.status_code,
                 httplib.responses[item_availability_response.status_code]))
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expected %s in %s" %
                ('items', item_availability_response.json().keys()))
        logging.info('test case executed successfully')

    def test_item_availability_with_valid_item_id(self):
        """ Checking the item availability with valid item_id """

        # Check item availability in the inventory with item id
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url(
                param='item_id', value='NOOR'))
        logging.info('test_item_availability_with_valid_item_id')
        logging.info('Url is %s', get_items_url(
            param='item_id', value='NOOR'))
        logging.info('Response is %s', item_availability_response.text)
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expected %s in %s" %
                ('items', item_availability_response.json().keys()))
        logging.info('test case executed successfully')

    def test_item_availability_with_valid_storage_capacity(self):
        """ Checking the item availability with valid storage_capacity """

        # Check item availability in the inventory with storage capacity
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url(
                param='storage_capacity', value='299'))
        logging.info('test_item_availability_with_valid_storage_capacity')
        logging.info('Url is %s', get_items_url(
            param='storage_capacity', value='299'))
        logging.info('Response is %s', item_availability_response.text)
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expected %s in %s" %
                ('items', item_availability_response.json().keys()))
        logging.info('test case executed successfully')

    def test_item_availability_with_valid_item_status(self):
        """ Checking the item availability with valid item_status """

        # Check item availability in the inventory with hardware model
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url(
                param='item_status', value='NEW'))
        logging.info('test_item_availability_with_valid_item_status')
        logging.info('Url is %s', get_items_url(
            param='item_status', value='NEW'))
        logging.info('Response is %s', item_availability_response.text)
        self.assertEquals(
            item_availability_response.status_code, 200,
            msg="Expected code is 200 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertIn(
            'items', item_availability_response.json().keys(),
            msg="Expected %s in %s" %
                ('items', item_availability_response.json().keys()))
        logging.info('test case executed successfully')

    def test_item_availability_with_invalid_hw_model(self):
        """ Checking the item availability with invalid hardware_model """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory with invalid hardware model
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url(param='hw_model', value='ss@'))
        item_availability_response_dict = item_availability_response.json()
        logging.info('test_item_availability_with_invalid_hw_model')
        logging.info('Url is %s', get_items_url(param='hw_model', value='ss@'))
        logging.info('Response is %s', item_availability_response.text)
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))
        logging.info('test case executed successfully')

    def test_item_availability_with_invalid_item_id(self):
        """ Checking the item availability with invalid item_id"""

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory with invalid item id
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url(param='item_id', value='as7@'))
        item_availability_response_dict = item_availability_response.json()
        logging.info('test_item_availability_with_invalid_item_id')
        logging.info('Url is %s', get_items_url(param='item_id', value='as7@'))
        logging.info('Response is %s', item_availability_response.text)
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))
        logging.info('test case executed successfully')

    def test_item_availability_with_invalid_item_status(self):
        """ Checking the item availability with invalid item_status """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory with invalid item status
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url(param='item_status', value='asdf'))
        item_availability_response_dict = item_availability_response.json()
        logging.info('test_item_availability_with_invalid_item_status')
        logging.info('Url is %s', get_items_url(
            param='item_status', value='asdf'))
        logging.info('Response is %s', item_availability_response.text)
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))
        logging.info('test case executed successfully')

    def test_item_availability_without_hw_model(self):
        """ Checking the item availability without hardware_model """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory without hardware model
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url(param='hw_model', value=''))
        item_availability_response_dict = item_availability_response.json()
        logging.info('test_item_availability_without_hw_model')
        logging.info('Url is %s', get_items_url(param='hw_model', value=''))
        logging.info('Response is %s', item_availability_response.text)
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))
        logging.info('test case executed successfully')

    def test_item_availability_without_item_id(self):
        """ Checking the item availability without item_id """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory without item id
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_id', ''))
        item_availability_response_dict = item_availability_response.json()
        logging.info('test_item_availability_without_item_id')
        logging.info('Url is %s', get_items_url('item_id', ''))
        logging.info('Response is %s', item_availability_response.text)
        self.assertEquals(
            item_availability_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                item_availability_response.status_code,
                httplib.responses[item_availability_response.status_code]))
        self.assertEquals(
            error_message, item_availability_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, item_availability_response_dict['message']))
        logging.info('test case executed successfully')

    def test_item_availability_without_storage_capacity(self):
        """ Checking the item availability without storage_capacity """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory without storage capacity
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('storage_capacity', ''))
        item_availability_response_dict = item_availability_response.json()
        logging.info('test_item_availability_without_storage_capacity')
        logging.info('Url is %s', get_items_url('storage_capacity', ''))
        logging.info('Response is %s', item_availability_response.text)
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
        logging.info('test case executed successfully')

    def test_item_availability_without_item_status(self):
        """ Checking the item availability without item_status """

        error_message = "Invalid attribute value!"

        # Check item availability in the inventory without item status
        item_availability_response = inventory_service.request(
            RequestType.GET, get_items_url('item_status', ''))
        item_availability_response_dict = item_availability_response.json()
        logging.info('test_item_availability_without_item_status')
        logging.info('Url is %s', get_items_url('item_status', ''))
        logging.info('Response is %s', item_availability_response.text)
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
        logging.info('test case executed successfully')

    """ update the status of an item """

    """ Method:PUT"""

    def test_update_item_with_valid_item_id(self):
        """ Updating the item_status with valid item_id and sku """

        expected_message = ["Item has been updated in Inventory"]

        # Update inventory with valid item id and sku
        update_item_status_response = inventory_service.request(
            RequestType.PUT, update_item_url(item_id='NOOR'),
            payload=InventoryServicePayload().inventory_update_payload())
        update_item_status_response_dict = update_item_status_response.json()
        logging.info('test_update_item_with_valid_item_id')
        logging.info('Url is %s', update_item_url(item_id='NOOR'))
        logging.info('Request is %s',
                     InventoryServicePayload().inventory_update_payload())
        logging.info('Response is %s', update_item_status_response.text)
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
        logging.info('test case executed successfully')

    def test_update_item_with_invalid_item_status(self):
        """ Updating the item_status with
        valid item_id and with response sku """

        error_message = "Invalid input values : Item status is not valid"

        # Update an inventory without sku
        update_item_status_response = inventory_service.request(
            RequestType.PUT, update_item_url(item_id='NOOR'),
            payload=InventoryServicePayload().inventory_update_payload(
                item_status='newly', sku=''))
        update_item_status_response_dict = update_item_status_response.json()
        logging.info('test_update_item_with_invalid_item_status')
        logging.info('Url is %s', update_item_url(item_id='NOOR'))
        logging.info('Request is %s',
                     InventoryServicePayload().inventory_update_payload(
                         item_status='newly', sku=''))
        logging.info('Response is %s', update_item_status_response.text)
        self.assertEquals(
            update_item_status_response.status_code, 400,
            msg="Expected code is 400 and got is %s (%s)" % (
                update_item_status_response.status_code,
                httplib.responses[update_item_status_response.status_code]))
        self.assertEquals(
            error_message,
            update_item_status_response_dict['message'],
            msg="Expected message is %s and got is %s" %
                (error_message, update_item_status_response_dict['message']))
        logging.info('test case executed successfully')
