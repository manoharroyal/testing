""" Ticket service payloads """


class TicketServicePayload(object):
    """ Class for Ticket Service Payloads """

    def update_ticket_payload(self, ticket_status="Accepted",
                              update_description="Required one"):
        """ payload to update the ticket status """
        payload = {
            "ticket_status": ticket_status,
            "update_description": update_description
        }
        return payload

    def get_tickets_payload(self, job_id="c01f5074-3f8c-42b6-a2ff-4f67de41b357"):
        """ payload to get list of tickets """
        payload = {
            "job_id": job_id
        }
        return payload
