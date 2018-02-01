""" Payloads for box service """


class BoxServicePayloads(object):
    """ payloads for box service are goes here """

    def action_box_payload(self,
                           box_id='ASDFGH', agent_id='345728',
                           job_id='9273ba2c-d4ac-41a0-b609-1ce5526051ad',
                           order_id=None,
                           customer_id='66214cc36fa1a900b9e847dc5d3ee474',
                           credentials=None):
        """ payload for box update"""
        payload = {
            "box_id": box_id,
            "agent_id": agent_id,
            "job_id": job_id,
            "order_id": order_id,
            "customer_id": customer_id,
            "credentials": credentials
        }
        return payload

    def update_box_payload(self, agent_id='ASDFGH',
                           job_id='9273ba2c-d4ac-41a0-b609-1ce5526051ad',
                           customer_id='66214cc36fa1a900b9e847dc5d3ee474'):
        """ Pay load to create box """

        payload = {
            "agent_id": agent_id,
            "job_id": job_id,
            "customer_id": customer_id
        }
        return payload
