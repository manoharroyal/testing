""" Mocking function to get ticket details """

import json


def get_ticket_handler(event, context):
    """ mock get ticket details """
    if event.get('queryStringParameters', []):
        ticket_number = event['queryStringParameters']['number'];
    else:
        ticket_number = 'CHG0050999'

    body = {
        "result": [
            {
                "parent": "",
                "reason": "null",
                "watch_list": "",
                "upon_reject": "Cancel all future Tasks",
                "sys_updated_on": "2018-02-05 01:59:48",
                "type": "Comprehensive",
                "approval_history": "",
                "skills": "",
                "number": ticket_number,
                "test_plan": "",
                "cab_delegate": "",
                "requested_by_date": "",
                "state": "Closed Complete",
                "sys_created_by": "sa-data-seeding",
                "knowledge": "false",
                "order": "",
                "phase": "Requested",
                "u_subcategory": "null",
                "cmdb_ci": "",
                "impact": "2 - Medium",
                "active": "false",
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
                "short_description": "Approve Job",
                "correlation_display": "",
                "work_start": "",
                "additional_assignee_list": "",
                "outside_maintenance_schedule": "false",
                "service_offering": "",
                "sys_class_name": "Change Request",
                "closed_by": {
                    "display_value": "Sourabh Kulkarni (TDC)",
                    "link": "https://foggydev.service-now.com/api/now/table/sys_user/b25160e94f884f0044ff50ee0310c79f"
                },
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
                "sys_updated_by": "Sourabh.Kulkarni",
                "opened_by": {
                    "display_value": "Data Seeding",
                    "link": "https://foggydev.service-now.com/api/now/table/sys_user/1ed1832313304300c8c73262f244b0bb"
                },
                "user_input": "",
                "sys_created_on": "2018-01-25 16:29:07",
                "sys_domain": {
                    "display_value": "global",
                    "link": "https://foggydev.service-now.com/api/now/table/sys_user_group/global"
                },
                "u_welcome_letter_okay_to_send": "false",
                "closed_at": "2018-01-25 17:58:16",
                "review_comments": "",
                "business_service": "",
                "u_workflow_stage": "Requested",
                "time_worked": "0 Seconds",
                "expected_start": "",
                "opened_at": "2018-01-25 16:29:07",
                "work_end": "",
                "phase_state": "Open",
                "cab_date": "",
                "work_notes": "",
                "assignment_group": "",
                "description": "Approve Job",
                "calendar_duration": "",
                "u_cs_ticket": "",
                "close_notes": "",
                "sys_id": "0724ac0313bb8b004ce976d66144b0f6",
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
                "sys_mod_count": "21",
                "sys_tags": "",
                "conflict_last_run": "",
                "location": "",
                "risk": "Moderate",
                "category": "Other"
            }
        ]
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
