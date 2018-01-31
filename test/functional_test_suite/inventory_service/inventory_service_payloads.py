""" Payloads for inventory service """


class InventoryServicePayload(object):
    """ Inventory Service Payload """

    def inventory_additem_payload(self, item_id='NOOR', hw_model='ASDF123',
                                  hw_number='5QWER', mac_address='NOONE',
                                  storage_capacity=299, item_status='NEW',
                                  remarks='store',
                                  storage_array_model='ADSFEYFD',
                                  storage_array_type='sop', order_id='asdfgh'):
        """ Request body for adding an item into the inventory """

        payload = {
            "item_id": item_id,
            "hw_model": hw_model,
            "hw_number": hw_number,
            "mac_address": mac_address,
            "storage_capacity": storage_capacity,
            "item_status": item_status,
            "remarks": remarks,
            "storage_array_model": storage_array_model,
            "storage_array_type": storage_array_type,
            "order_id": order_id
        }
        return payload

    def inventory_update_payload(self, item_status='ASSIGNED', sku='ASDF123-299',
                                 item_id=None, hw_model=None, hw_number=None,
                                 mac_address=None, storage_capacity=60,
                                 remarks=None, storage_array_model=None,
                                 storage_array_type=None, order_id=None):
        """ Request body for updating an item_status with item id and sku """
        payload = {"item_status": item_status, "sku": sku, "item_id": item_id,
                   "hw_model": hw_model, "hw_number": hw_number,
                   "mac_address": mac_address,
                   "storage_capacity": storage_capacity, "remarks": remarks,
                   "storage_array_model": storage_array_model,
                   "storage_array_type": storage_array_type,
                   "order_id": order_id}
        return payload
