""" Agent service payloads """


class AgentServicePayload(object):
    """ Agent Service Payload """

    def update_agent_task_status(self, status='DONE',
                                 message='task completed successfully'):
        """ update status of agent """
        payload = {
            "status": status,
            "message": message
        }
        return payload

    def register_agent(self, username='testagent', password='testpswd',
                       agent_public_key='test_agent_public_key'):
        """ Payload to register an agent """
        payload = {
            "username": username,
            "password": password,
            "agent_public_key": agent_public_key
        }
        return payload