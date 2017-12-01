""" Integration test cases for All Flows"""
import unittest

from test.shared.rest_framework import RequestType, RestAPI

""" urls over here """
CUSTOMER_SERVICE_URL = "https://8bfaht51mh.execute-api.us-west-2.amazonaws.com/dev/customer-profiles/"
SYSTEM_SERVICE_URL = "https://7hg5rkdftc.execute-api.us-west-2.amazonaws.com/dev/system"
JOB_SERVICE_URL = "https://fudkvrzvb7.execute-api.us-west-2.amazonaws.com/dev/jobs"
BOX_SERVICE_URL = "https://tcj0l5l2na.execute-api.us-west-2.amazonaws.com/dev/box"
AGENT_SERVICE_URL = "https://f02gsiq51l.execute-api.us-west-2.amazonaws.com/dev/agents/{0}/register"
SEEDJOB_ACTION_URL = "https://fudkvrzvb7.execute-api.us-west-2.amazonaws.com/dev/jobs/{0}/job?action={1}"

""" Token Creation """
customer = RestAPI(utype='customer')
sysops = RestAPI(utype='sysops')
agent = RestAPI(utype='agent')


""" url manipulation """
agent_id = 'dd12082c-972e-49d7-a8ec-13d30a2f59b2'
job_id = 'e3b3d908-c916-42ae-964f-ebba727a00ab'
customer_profile_url = CUSTOMER_SERVICE_URL + str(customer.customerId)
register_agent_url = AGENT_SERVICE_URL.format(agent_id)
seedjob_ack_url = SEEDJOB_ACTION_URL.format(job_id, "ack_box_received")
seedjob_test_conn_url = SEEDJOB_ACTION_URL.format(job_id, "test_conn_source")
seedjob_export_url = SEEDJOB_ACTION_URL.format(job_id, "start_export")
seedjob_import_url = SEEDJOB_ACTION_URL.format(job_id, "start_import")

""" payloads over here """
cust_payload = {
    "title": "cust_new_test",
    "address_line_1": "testaddr1",
    "address_line_2": "testaddr2",
    "contact_name": "testname",
    "contact_number": 12345,
    "company_name": "testcompnay",
    "city": "testcity",
            "state": "teststate",
            "country": "testcountry",
            "zipcode": 411057
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

tg_system_creation_payload = {
    "system_type": "target",
    "system_name": "TestSourceSystem",
    "details": SYSTEM_DETAILS
}

create_job_payload = {
    "job_name": "Test_Backup102",
    "job_type": "BOX",
    "target_system_id": "CTAZURE2",
    "address_title": "cust_new_test",
    "description": "Thisistestjob",
    "source_system_id": "01e493cc-4dfd-47bb-9881-e24599432f16",
    "max_data_size": "50",
    "notification":
    {
        "email_id": "test@test.com",
        "job_complete": "True",
        "job_approved": "False",
        "box_shipped": "True",
        "ready_to_restore": "False",
        "data_erased": "True",
        "box_prepared": "True",
        "box_in_transit": "True",
        "box_at_switch": "True",
        "box_del_to_cust": "True",
        "data_restored": "True",
        "optional_email_id": "test@test.com"
    }
}

job_action_payload = {
    "db_user_name": "dbc",
    "db_user_password": "dbc"
}


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

        # 2. Customer Profile Creation
        customer.request(method=RequestType.PUT,
                         url=customer_profile_url,
                         payload=cust_payload,
                         )
        # 3. Add Source System
        customer.request(method=RequestType.POST,
                         url=SYSTEM_SERVICE_URL,
                         payload=system_creation_payload
                         )
        # 4. Create Target System
        customer.request(method=RequestType.POST,
                         url=SYSTEM_SERVICE_URL,
                         payload=tg_system_creation_payload)
        # 5. Create Job
        job = customer.request(method=RequestType.POST,
                               url=JOB_SERVICE_URL,
                               payload=create_job_payload)
        self.assertEquals(job.status_code, 201)

    def test_prepare_shipment_flow(self):
        """ Testing Shippment Flow
            1) Register Agent
        """

        # 1) Register Agent
        print "url is ", register_agent_url
        agent_resp = agent.request(method=RequestType.PUT,
                                   url=register_agent_url,
                                   payload=None)
        print "agent resp", agent_resp.text
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
        customer.request(RequestType.PUT,
                         url=seedjob_ack_url,
                         payload=job_action_payload)

        # 3. Test Source Connection
        customer.request(RequestType.PUT,
                         url=seedjob_test_conn_url,
                         payload=job_action_payload)

        # 4. Test Start Export
        export_job = customer.request(RequestType.PUT,
                                      url=seedjob_export_url,
                                      payload=job_action_payload)
        self.assertEqual(export_job.status_code, 202)

    def test_restore_at_switch_flow(self):
        """ The restore job flow 
            1. Box Connected (box)
            2. Box Ready for Import
            3. Get Task (box)
            4. Get Target Details (box)
            5. Target connection successfull (box)
            6. Ready for restore (box)
            7. Get task (box)
            8. Restore job update complete (box)
        """

        restore = customer.request(RequestType.PUT,
                                   url=seedjob_import_url,
                                   payload=job_action_payload)

        self.assertEquals(restore.status_code, 202)
