""" Integration test cases for All Flows"""
import unittest
import logging
from test.shared.rest_framework import RequestType, RestAPI, path
from test.functional_test_suite.common.config import initialize_logger
from test.functional_test_suite.common.config import CUSTOMER_SERVICE_URL
from test.functional_test_suite.common.config import SYSTEM_SERVICE_URL
from test.functional_test_suite.common.config import SEED_JOB_URL
from test.functional_test_suite.common.config import register_agent_url
from test.functional_test_suite.common.config import user_action_url
from test.functional_test_suite.common.config import list_system
from test.functional_test_suite.common.config import list_system_url
from test.functional_test_suite.common.config import get_agent_id_url

initialize_logger(path + "/../../logs/integration_test.log")

""" Token Creation """
customer = RestAPI(utype='customer')
sysops = RestAPI(utype='sysops')
agent = RestAPI(utype='agent')

customer_profile_url = CUSTOMER_SERVICE_URL + str(customer.customerId)

""" payloads over here """


customer_payload = {
    "shipping_address": {
        "title": "cust_new_test",
        "address_line_1": "testaddr1",
        "address_line_2": "testaddr2",
        "contact_name": "testname",
        "contact_number": 12345,
        "city": "testcity",
        "state": "teststate",
        "country": "testcountry",
        "zipcode": 411057
    }
}

SYSTEM_DETAILS = {
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

system_creation_payload = {
    "system_type": "source",
    "system_name": "TestSourceSystem",
    "details": SYSTEM_DETAILS
}


def create_seed_job_payload(
        job_name='test 28', description='Thisistestjob', job_type='BOX',
        address_title="9876",
        source_system_id='930c3a1e-c354-4441-8983-e56ada60e94b',
        target_system_id='JOHNAWS2', max_data_size="60", passphrase='new1234',
        email_id='emanohar80@gmail.com',
        optional_email_id='eethakatla.manohar@opcito.com',
        box_connected_to_customer_permimses=True, job_approved=False,
        box_shipped=True, box_del_to_cust=True, box_at_switch=True,
        data_exported=True, data_restored=True, job_complete=True,
        data_erased=True, data_integrity_validated=True):
    """ Request body for creation of seed job"""

    payload = {"job_name": job_name,
               "description": description,
               "job_type": job_type,
               "notification": {
                   "email_id": email_id,
                   "optional_email_id": optional_email_id,
                   "box_connected_to_customer_permimses": box_connected_to_customer_permimses,
                   "job_approved": job_approved,
                   "box_shipped": box_shipped,
                   "box_del_to_cust": box_del_to_cust,
                   "box_at_switch": box_at_switch,
                   "data_exported": data_exported,
                   "data_restored": data_restored,
                   "job_complete": job_complete,
                   "data_erased": data_erased,
                   "data_integrity_validated": data_integrity_validated
               },
               "address_title": address_title,
               "source_system_id": source_system_id,
               "target_system_id": target_system_id,
               "max_data_size": max_data_size,
               "passphrase": passphrase
               }
    return payload


job_action_payload = {
    "db_user_name": "dbc",
    "db_user_password": "dbc"
}

job_id = 0
agent_id = 0


class IntegrationTest(unittest.TestCase):
    """ The integration test cases """

    def test_create_job_flow(self):
        """ Testing Create job Flow
            ( Trying to create a job with customer )
            1. Login as customer (token_generation)
            2. Customer profile creation
            3. Add source system
            4. Get target system
            5. Create job
        """

        global job_id

        # 2. Customer Profile Creation
        customer_profile_creation = customer.request(
            method=RequestType.PUT, url=customer_profile_url,
            payload=customer_payload)
        logging.info(customer_profile_creation.text)

        # 3. Add Source System
        source_system_creation = customer.request(
            method=RequestType.POST, url=SYSTEM_SERVICE_URL,
            payload=system_creation_payload)
        source_system_id = source_system_creation.json()['id']
        logging.info(source_system_creation.text)

        # 4. Create Target System
        target_system_creation = customer.request(
            method=RequestType.GET,
            url=list_system_url(list_system, system_type='target'))
        target_system_id = target_system_creation.json()['systems'][0]['siteId']
        logging.info(target_system_creation.text)

        # 5. Create Job
        job_creation = customer.request(
            method=RequestType.POST, url=SEED_JOB_URL,
            payload=create_seed_job_payload(
                address_title='cust_new_test',
                source_system_id=source_system_id,
                target_system_id=target_system_id))
        job_creation_dict = job_creation.json()
        job_id = job_creation_dict['job_id']
        logging.info(job_creation.text)
        self.assertEquals(job_creation.status_code, 201)

    def test_prepare_shipment_flow(self):
        """ Testing Shipment Flow
            1) Register Agent
        """
        # 1) Get agent_id which is associated with job
        global agent_id

        agent_id_resp = customer.request(
            RequestType.GET, get_agent_id_url(job_id=job_id))
        agent_id = agent_id_resp.json()['agent_id']
        print agent_id
        logging.info(agent_id_resp.text)

        # 1) Register Agent
        agent_resp = agent.request(
            RequestType.PUT, register_agent_url(agent_id=agent_id))
        logging.info(agent_resp.text)
        self.assertEqual(agent_resp.status_code, 202)

    def test_backupjob_flow(self):
        """ Testing Backup Job Creation in Customer DC
            1. Customer Box Ack
            2. Agent Connected (box)
            3. Test Source Connection
            4. Get Task (box)
            5. Get Source (box)
            6. Test Connection (box)
            7. DB Connection (box)
            8. Ready for Export (box)
            9. Get Object Tree
            10. Start Export
            11. Get Task (box)
            12. Update Done (box)
        """

        # 1. Customer Box Ack
        box_ack = customer.request(RequestType.PUT,
                         user_action_url(seed_job_id=job_id, action='ack_box_received'),
                         payload=job_action_payload)
        logging.info(box_ack.text)

        # 3. Test Source Connection
        box_test_conn_source = customer.request(RequestType.PUT,
                         user_action_url(seed_job_id=job_id, action='test_conn_source'),
                         payload=job_action_payload)
        logging.info(box_test_conn_source.text)

        # 4. Test Start Export
        export_job = customer.request(RequestType.PUT,
                                      user_action_url(seed_job_id=job_id, action='start_export'),
                                      payload=job_action_payload)
        logging.info(export_job.text)
        self.assertEqual(export_job.status_code, 202)

    def test_restore_at_switch_flow(self):
        """ The restore job flow
            1. Box Connected (box)
            2. Box Ready for Import
            3. Get Task (box)
            4. Get Target Details (box)
            5. Target connection successful (box)
            6. Ready for restore (box)
            7. Get task (box)
            8. Restore job update complete (box)
        """

        restore = customer.request(RequestType.PUT,
                                   user_action_url(seed_job_id=job_id, action='start_import'),
                                   payload=job_action_payload)
        logging.info(restore.text)
        self.assertEquals(restore.status_code, 202)
