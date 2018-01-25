""" Payloads for box service """


class BoxServicePayloads(object):
    """ payloads for box service are goes here """

    def update_box_payload(self, sample='one'):
        """ payload for box update"""
        payload = {
            "sample": sample
        }
        return payload
