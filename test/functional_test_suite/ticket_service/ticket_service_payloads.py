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
