import unittest
from common.rest_framework import RestAPIHeader, RequestType
from common.config import INVENTORY_SERVICE_URL
from common.payloads import Inventoryservicepayload

inventory_rest_obj = RestAPIHeader()

""" Setting up the parameters with urls """


def get_items_url(param, val):
    """ Url for checking the item availability in the inventory"""

    return '%s?%s=%s' % (INVENTORY_SERVICE_URL, param, val)


def update_url(val):
    """ Url for updating the item status in the inventory by item id """

    return '%s/%s' % (INVENTORY_SERVICE_URL, val)


class InventoryServiceAddItemTestcases(unittest.TestCase):
    """ Add item class """
    """ Method:POST"""

    def test_with_valid_details(self):
        """ Adding an item with all valid parameters into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload())
        input_dict = Inventoryservicepayload().inventory_additem_payload(self)
        out_dict = out.json()
        self.assertEquals(out.status_code, 200)
        assert (out_dict.get(k, []) == input_dict[k] for k in input_dict)

    def test_with_invalid_item_id(self):
        """ Testing with invalid item id to add an item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             item_id='1@d@323'))
        input_dict = Inventoryservicepayload().inventory_additem_payload(
            item_id='1@%  $ &df')
        out_dict = out.json()
        self.assertEquals(out.status_code, 200)
        assert (out_dict.get(k, []) == input_dict[k] for k in input_dict)

    def test_with_invalid_hw_model(self):
        """ Testing with invalid hardware_model to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             hw_model='@dr ^ y@'))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_invalid_hw_number(self):
        """ Testing with invalid hardware_number to
        add an item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload
                                         (hw_number='5tg ^& $%'))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_invalid_mac_address(self):
        """ Testing with invalid mac_address to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             mac_address='tg$cb ( wdui%'))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_invalid_storage_capacity(self):
        """ Testing with invalid storage_capacity to add
        an item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             storage_capacity=-300))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_invalid_itemstatus(self):
        """ Testing with invalid item_status to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             item_status='NEW@##  * '))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_invalid_remarks(self):
        """ Testing with invalid data for remarks to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             remarks='AS #@'))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_invalid_order_id(self):
        """ Testing with invalid order_id to add an item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             order_id='1@ * '))
        input_dict = Inventoryservicepayload().inventory_additem_payload(
            order_id='1@ * ')
        out_dict = out.json()
        self.assertEquals(out.status_code, 200)
        assert (out_dict.get(k, []) == input_dict[k] for k in input_dict)

    def test_with_invalid_storage_array_model(self):
        """ Testing with invalid storage_array_model to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             storage_array_model='sv *cy%@'))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_invalid_storage_array_type(self):
        """ Testing with invalid storage_array_type to add
        an item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             storage_array_type='asd# @'))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_item_id(self):
        """ Testing with out item_id to add an item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             item_id=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_hw_model(self):
        """ Testing with out hardware_model to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             hw_model=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_hw_number(self):
        """ Testing with empty hardware_number to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             hw_number=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_mac_address(self):
        """ Testing without content for mac_address to add an item
        into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             mac_address=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_storage_capacity(self):
        """ Testing without content for mac_address to
        add an item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             storage_capacity=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_item_status(self):
        """ Testing without status of item to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             item_status=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_remarks(self):
        """ Testing with out content for remarks to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             remarks=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_storage_array_type(self):
        """ Testing with out storage_array_model to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             storage_array_type=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_storage_array_model(self):
        """ Testing with  out storage_array_type to add an
        item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             storage_array_model=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_orderid(self):
        """ Testing with out order_id to add an item into the inventory """

        out = inventory_rest_obj.request(RequestType.POST,
                                         INVENTORY_SERVICE_URL,
                                         payload=Inventoryservicepayload().
                                         inventory_additem_payload(
                                             order_id=''))
        out_dict = out.json()
        error_message = "Could not validate the input, " \
                        "please send the correct input parameters"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)


class CheckItemAvailabilityTestcases(unittest.TestCase):
    """ check the item in an inventory """
    """ Method:GET """

    def test_item_availability_with_valid_hw_model(self):
        """ Checking the item availability with valid hardware_model """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('hw_model', 'ASDF123'))
        print(get_items_url('hw_model', 'ASDF123'))
        assert out.status_code == 200 and 'items' in out.json().keys()

    def test_with_valid_item_id(self):
        """ Checking the item availability with valid item_id """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('item_id', 'NOOR'))
        self.assertEquals(out.status_code, 200)
        assert 'items' in out.json().keys()

    def test_with_valid_storage_capacity(self):
        """ Checking the item availability with valid storage_capacity """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('storage_capacity',
                                                       '299'))
        self.assertEquals(out.status_code, 200)
        assert 'items' in out.json().keys()

    def test_with_valid_item_status(self):
        """ Checking the item availability with valid item_status """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('item_status', 'NEW'))
        self.assertEquals(out.status_code, 200)
        assert 'items' in out.json().keys()

    def test_with_invalid_hw_model(self):
        """ Checking the item availability with invalid hardware_model """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('hw_model',
                                                       'sf1@%563 7'))
        out_dict = out.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_invalid_item_id(self):
        """ Checking the item availability with invalid item_id"""

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('item_id',
                                                       'asfyd 227@@!'))
        out_dict = out.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_with_invalid_item_status(self):
        """ Checking the item availability with invalid item_status """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('item_status', 'asdf'))
        out_dict = out.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_hw_model(self):
        """ Checking the item availability without hardware_model """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('hw_model', ''))
        out_dict = out.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_item_id(self):
        """ Checking the item availability without item_id """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('item_id', ''))
        out_dict = out.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_storage_capacity(self):
        """ Checking the item availability without storage_capacity """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('storage_capacity', ''))
        out_dict = out.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)

    def test_without_item_status(self):
        """ Checking the item availability without item_status """

        out = inventory_rest_obj.request(RequestType.GET,
                                         get_items_url('item_status', ''))
        out_dict = out.json()
        error_message = "Invalid attribute value!"
        self.assertEquals(out.status_code, 400)
        self.assertEquals(out_dict['message'], error_message)


class UpdateItemTestcases(unittest.TestCase):
    """ update the status of an item """

    """ Method:PUT"""

    def test_with_valid_item_id(self):
        """ Updating the item_status with valid item_id and sku """

        out = inventory_rest_obj.request(RequestType.PUT, update_url('NOOR'),
                                         payload=Inventoryservicepayload().
                                         inventory_update_payload())
        out_dict = out.json()
        message = ["Item has been updated in Inventory"]
        self.assertEquals(out.status_code, 200)
        self.assertEquals(out_dict['message'], message)

    def test_without_sku(self):
        """ Updating the item_status with valid item_id and with out sku """

        out = inventory_rest_obj.request(RequestType.PUT, update_url('NOOR'),
                                         payload=Inventoryservicepayload().
                                         inventory_update_payload(
                                             item_status='newly', sku=''))
        out_dict = out.json()
        error_message = "Could not update database with expected values : " \
                        "No uid/sku found to update"
        self.assertEquals(out.status_code, 500)
        self.assertEquals(out_dict['message'], error_message)


if __name__ == '__main__':
    unittest.main()
