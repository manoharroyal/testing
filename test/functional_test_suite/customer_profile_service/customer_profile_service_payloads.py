""" Payloads for customer profile service """


class CustomerProfileServicePayload(object):
    """ Payloads for customer profile service """

    def customer_profile_payload(self, title="Test_Job",
                                 addr1="40 NE River Bridge", addr2=None,
                                 cont_num=344245224, zipcode=1234, country='US',
                                 state='IOWA', city='Cedar Rapids',
                                 contact_name='jeyanthi'):
        """ Return payload of customer profile """
        payload = {
            "shipping_address": {
                "title": title,
                "address_line_1": addr1,
                "address_line_2": addr2,
                "contact_number": cont_num,
                "contact_name": contact_name,
                "city": city,
                "state": state,
                "country": country,
                "zipcode": zipcode
            }
        }
        return payload

    def update_shipping_address_payload(
            self, title="9876", addr1="newbackup", addr2="Rest",
            contact_name="manohar", contact_number=9492, company_name="Company",
            city="opera", state="windows", country="lenovo", zipcode=411057):
        """ Payload to update the shipping address """
        payload = {
            "title": title,
            "address_line_1": addr1,
            "address_line_2": addr2,
            "contact_name": contact_name,
            "contact_number": contact_number,
            "company_name": company_name,
            "city": city,
            "state": state,
            "country": country,
            "zipcode": zipcode
        }
        return payload

    def delete_payload_parameter(self, del_param=None):
        """ Delete the payload parameter """
        customer_profile_payload = self.customer_profile_payload()
        if del_param is None:
            print ("parameter should be passed")
        else:
            customer_profile_payload["shipping_address"].pop(del_param)
        return customer_profile_payload
