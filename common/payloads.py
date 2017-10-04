""" All the payloads managed here """


class AgentServicePayload(object):
    """ Agent Service Payload """

    def __init__(self):
        pass

    def update_agent_task_status(self, status='string', message='string'):
        """ update status of agent """
        payload = {"status": status, "message": message}
        return payload


class CustomerProfileServicePayload(object):
    """ Payloads for customer profile service """

    def __init__(self):
        pass

    def customer_profile_payload(self, title="Test_Job",
                                 addr1="40 NE River Bridge", addr2=None,
                                 cont_num=344245224, zipcode=1234, country='US',
                                 state='IOWA', city='Cedar Rapids',
                                 contact_name='jeyanthi'):
        """ Return payload of customer profile """
        payload = {
            "shipping_address": {
                "title": title,
                "address_line_1": addr1,
                "address_line_2": addr2,
                "contact_number": cont_num,
                "contact_name": contact_name,
                "city": city,
                "state": state,
                "country": country,
                "zipcode": zipcode
            }
        }
        return payload

    def delete_payload_parameter(self, del_param=None):
        """ Delete the payload parameter """
        customer_profile_payload = self.customer_profile_payload()
        if del_param is None:
            print ("parameter should be passed")
        else:
            customer_profile_payload["shipping_address"].pop(del_param)
        return customer_profile_payload


class Inventoryservicepayload(object):
    """ Inventory Service Payload """

    def __init__(self):
        pass

    def inventory_additem_payload(self, item_id='NOOR', hw_model='ASDF123',
                                  hw_number='5QWER', mac_address='NOONE',
                                  storage_capacity=299, item_status='NEW',
                                  remarks='store',
                                  storage_array_model='ADSFEYFD',
                                  storage_array_type='sop', order_id='asdfgh'):
        """ Request body for adding an item into the inventory """

        payload = {"item_id": item_id, "hw_model": hw_model,
                   "hw_number": hw_number, "mac_address": mac_address,
                   "storage_capacity": storage_capacity,
                   "item_status": item_status, "remarks": remarks,
                   "storage_array_model": storage_array_model,
                   "storage_array_type": storage_array_type,
                   "order_id": order_id}
        return payload

    def inventory_update_payload(self, item_status='ONEONLY', sku='ASDF123-299',
                                 item_id=None, hw_model=None, hw_number=None,
                                 mac_address=None, storage_capacity=None,
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


class SeedJobServicePayload(object):
    """ Payload for seed job service """

    def __init__(self):
        pass

    def create_seed_job_payload(
            self, seed_job_name='TestBackup20', job_type='BOX',
            target_system_id='0f9dcceb-926c-4b0e-be63-785d26edc8a1',
            address_title=1111, description='Thisistestjob',
            source_system_id='86dc65e4-42a0-4ee8-91e8-f201678f53aa',
            max_data_size=50, email_id='emanohar80@gmail.com',
            job_complete=True, job_approved=False, box_shipped=False,
            ready_to_restore=False, data_erased=False, box_prepared=False,
            box_in_transit=False, box_at_switch=False, box_del_to_cust=False,
            data_restored=False,
            optional_email_id='eethakatla.manohar@opcito.com'):
        """ Request body for creation of seed job"""

        payload = {"seed_job_name": seed_job_name, "job_type": job_type,
                   "target_system_id": target_system_id,
                   "notification": {"email_id": email_id,
                                    "job_complete": job_complete,
                                    "job_approved": job_approved,
                                    "box_shipped": box_shipped,
                                    "ready_to_restore": ready_to_restore,
                                    "data_erased": data_erased,
                                    "box_prepared": box_prepared,
                                    "optional_email_id": optional_email_id,
                                    "box_in_transit": box_in_transit,
                                    "box_at_switch": box_at_switch,
                                    "box_del_to_cust": box_del_to_cust,
                                    "data_restored": data_restored},
                   "address_title": address_title, "description": description,
                   "source_system_id": source_system_id,
                   "max_data_size": max_data_size}
        return payload

    def update_seed_job_payload(
            self,
            email_optional='eethakatla.manohar@opcito.com',
            email='emanohar80@gmail.com',
            source_system_id='86dc65e4-42a0-4ee8-91e8-f201678f53aa',
            target_system_id='0f9dcceb-926c-4b0e-be63-785d26edc8a1',
            seeding_type='new', job_complete=True, job_approved=False,
            box_shipped=False, ready_to_restore=False, data_erased=False,
            box_prepared=False, box_in_transit=False, box_at_switch=False,
            box_del_to_cust=False, data_restored=False,
            source_selections="test"):
        """ Request body to update the seedjob details """

        payload = {"notification": {"email_optional": email_optional,
                                    "job_complete": job_complete,
                                    "job_approved": job_approved,
                                    "box_shipped": box_shipped,
                                    "ready_to_restore": ready_to_restore,
                                    "data_erased": data_erased,
                                    "box_prepared": box_prepared,
                                    "box_in_transit": box_in_transit,
                                    "box_at_switch": box_at_switch,
                                    "box_del_to_cust": box_del_to_cust,
                                    "data_restored": data_restored,
                                    "email": email},
                   "source_system_id": source_system_id,
                   "target_system_id": target_system_id,
                   "seeding_type": seeding_type,
                   "source_selections": [source_selections]}
        return payload

    def system_credentials(self, db_user_name='dbc', db_user_password='dbc'):
        """ Credentials for the database """
        payload = {"db_user_name": db_user_name,
                   "db_user_password": db_user_password}
        return payload

    def expected_payload(self, created_at="2017-09-06 06:34:35.274153",
                         customer_id="66214cc36fa1a900b9e847dc5d3ee474",
                         job_id="5caf59ea-9ce7-4465-b38a-2fe7434b656f",
                         job_status="CREATED", job_type="BOX",
                         seed_job_name="TestBackup20",
                         timeline_status="CREATED"):
        """ Payload for jobs """
        payload = {"created_at": created_at, "customer_id": customer_id,
                   "job_id": job_id, "job_status": job_status,
                   "job_type": job_type, "seed_job_name": seed_job_name,
                   "timeline_status": timeline_status}
        return payload

    def approve_payload(self, comment="Approved"):
        """ Payload to approve the job """
        payload = {"comment": comment}
        return payload

    def update_job_logs(self, source_objects=({"AS": "OFF"})):
        """ Payload to update the job logs """
        payload = {"source_objects": source_objects}
        return payload


SYSTEM_DETAILS = {
    "details": {
        "system_name": "TDCLOUD15TD11",
        "bynet": {
            "PMA": "72",
            "bynet0": {
                "ip": "10.20.2.8",
                "net_mask": "255.255.0.0"
            },
            "bynet1": {
                "ip": "10.16.2.8",
                "net_mask": "255.255.0.0"
            }
        },
        "node_ip": {
            "interface": "eth0",
            "ip": "10.21.130.8",
            "mask": "255.255.0.0"
        },
        "dc_ip": {
            "interface": "eth3",
            "ip": "10.25.152.62",
            "mask": "255.255.254.0"
        },
        "version": {
            "BLM driver": "03.07.03.02",
            "BLM protocol": "15.07.27.15",
            "database_version": "15.10.02.04",
            "BLM commands": "03.07.03.02"
        },
        "host_name": "TDCLOUD15TD10-2-8",
        "nodes": [
            {
                "short_hostname": [
                    "TDCLOUD15TD10-2-8"
                ],
                "ip": "10.22.130.8",
                "name": "TDCLOUD15TD10",
                "full_qualified_hostname": "SMP002-8"
            }
        ]
    }
}


class SystemServicePayload(object):
    """ Payloads for system service """

    def __init__(self):
        pass

    def system_creation_payload(self, system_type='source',
                                system_name="TDCLOUD15TD12",
                                details=SYSTEM_DETAILS["details"]):
        """ Request body for creation of seed job"""

        payload = {"system_type": system_type, "system_name": system_name,
                   "details": details}
        return payload

    def system_deletion_payload(self, del_param=None):
        """ payload to delete the system """

        payload = self.system_creation_payload()
        if del_param is None:
            print ("parameter should be passed")
        else:
            payload.pop(del_param)
        return payload


class TicketServicePayload(object):
    """ Class for Ticket Service Payloads """

    def __init__(self):
        pass

    def update_ticket_payload(self, detail="string", message="string"):
        """ payload to update the ticket status """
        payload = {"detail": detail, "message": message}
        return payload
