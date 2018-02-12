""" Ticket service payloads """


class TicketServicePayload(object):
    """ Class for Ticket Service Payloads """

    def update_ticket_payload(self, ticket_status="string",
                              update_description="string"):
        """ payload to update the ticket status """
        payload = {
            "ticket_status": ticket_status,
            "update_description": update_description
        }
        return payload

    def get_tickets_payload(self, job_id="abcsdhuiddwshuah"):
        """ payload to get list of tickets """
        payload = {
            "job_id": job_id
        }
        return payload
