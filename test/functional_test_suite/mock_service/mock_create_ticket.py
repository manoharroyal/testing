""" Mocking function for creation of ticket """

import json
import random


def create_ticket_handler(event, context):
    """ mock create ticket response """
    body = {
        "result": {
            "parent": "",
            "reason": "null",
            "watch_list": "",
            "upon_reject": "Cancel all future Tasks",
            "sys_updated_on": "2018-03-27 12:48:24",
            "type": "Comprehensive",
            "approval_history": "",
            "skills": "",
            "number": "CHG" + str(random.randint(1000000, 9999999)),
            "test_plan": "",
            "cab_delegate": "",
            "requested_by_date": "",
            "state": "Open",
            "sys_created_by": "sa-data-seeding-dev",
            "knowledge": "false",
            "order": "",
            "phase": "Requested",
            "u_subcategory": "null",
            "cmdb_ci": "",
            "impact": "2 - Medium",
            "active": "true",
            "work_notes_list": "",
            "priority": "2 - High",
            "cab_recommendation": "",
            "production_system": "false",
            "review_date": "",
            "u_notify": "true",
            "business_duration": "",
            "group_list": "",
            "requested_by": {
                "display_value": "Data Seeding",
                "link": "https://foggydev.service-now.com/api/now/table/sys_user/1ed1832313304300c8c73262f244b0bb"
            },
            "change_plan": "",
            "approval_set": "",
            "implementation_plan": "",
            "end_date": "",
            "short_description": "DSS test ticket March 25",
            "correlation_display": "",
            "work_start": "",
            "additional_assignee_list": "",
            "outside_maintenance_schedule": "false",
            "service_offering": "",
            "sys_class_name": "Change Request",
            "closed_by": "",
            "follow_up": "",
            "u_workflow": "",
            "reassignment_count": "0",
            "review_status": "(3)",
            "u_common_category": "Other",
            "assigned_to": "",
            "start_date": "",
            "sla_due": "UNKNOWN",
            "u_customer_impacted": "false",
            "comments_and_work_notes": "",
            "escalation": "Normal",
            "upon_approval": "Proceed to Next Task",
            "correlation_id": "",
            "made_sla": "true",
            "backout_plan": "",
            "conflict_status": "Not Run",
            "u_service_impacted": "false",
            "sys_updated_by": "sa-data-seeding-dev",
            "opened_by": {
                "display_value": "Data Seeding-dev",
                "link": "https://foggydev.service-now.com/api/now/table/sys_user/94d7260b4f40174044ff50ee0310c71b"
            },
            "user_input": "",
            "sys_created_on": "2018-03-27 12:48:24",
            "sys_domain": {
                "display_value": "global",
                "link": "https://foggydev.service-now.com/api/now/table/sys_user_group/global"
            },
            "u_welcome_letter_okay_to_send": "false",
            "closed_at": "",
            "review_comments": "",
            "business_service": "",
            "u_workflow_stage": "Requested",
            "time_worked": "",
            "expected_start": "",
            "opened_at": "2018-03-27 12:48:24",
            "work_end": "",
            "phase_state": "Open",
            "cab_date": "",
            "work_notes": "",
            "assignment_group": {
                "display_value": "Teradata Cloud TIER I Support",
                "link": "https://foggydev.service-now.com/api/now/table/sys_user_group/2df4bf524db195000725667a7330dfe9"
            },
            "description": "DSS test ticket March 25",
            "calendar_duration": "",
            "u_cs_ticket": "",
            "close_notes": "",
            "sys_id": "39ec252e13cd17804ce976d66144b00f",
            "contact_type": "Phone",
            "cab_required": "false",
            "urgency": "3 - Low",
            "scope": "Medium",
            "company": {
                "display_value": "BevMo!",
                "link": "https://foggydev.service-now.com/api/now/table/core_company/66214cc36fa1a900b9e847dc5d3ee474"
            },
            "justification": "",
            "activity_due": "UNKNOWN",
            "comments": "",
            "u_access_role": "",
            "approval": "Not Yet Requested",
            "due_date": "",
            "sys_mod_count": "0",
            "sys_tags": "",
            "conflict_last_run": "",
            "location": "",
            "risk": "Moderate",
            "category": "Other"
        }
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
