""" Ticket service payloads """


class TicketServicePayload(object):
    """ Class for Ticket Service Payloads """

    def update_ticket_payload(self, detail="string", message="string"):
        """ payload to update the ticket status """
        payload = {
            "detail": detail,
            "message": message
        }
        return payload
