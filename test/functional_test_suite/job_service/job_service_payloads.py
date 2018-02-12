""" Payloads for job service """


class SeedJobServicePayload(object):
    """ Payload for seed job service """

    def create_seed_job_payload(
            self, job_name='TestBackup102', job_type='BOX',
            target_system_id='',
            address_title="9876", description='Thisistestjob',
            source_system_id='0cb0fba4-1776-4434-9f44-170b8013a710',
            max_data_size="60", email_id='emanohar80@gmail.com',
            job_complete=True, job_approved=False, box_shipped=True,
            ready_to_restore=False, data_erased=True, box_prepared=True,
            box_in_transit=True, box_at_switch=True, box_del_to_cust=True,
            data_restored=True,
            optional_email_id='eethakatla.manohar@opcito.com'):
        """ Request body for creation of seed job"""

        payload = {"job_name": job_name,
                   "job_type": job_type,
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
                   "address_title": address_title,
                   "description": description,
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
        payload = {
            "db_user_name": db_user_name,
            "db_user_password": db_user_password
        }
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
