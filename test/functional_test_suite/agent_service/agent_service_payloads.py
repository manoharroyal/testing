""" Agent service payloads """


class AgentServicePayload(object):
    """ Agent Service Payload """

    def update_agent_task_status(self, status='string', message='string'):
        """ update status of agent """
        payload = {
            "status": status,
            "message": message
        }
        return payload
