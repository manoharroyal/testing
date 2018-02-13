""" agent service payloads """


class AuthServicePayload(object):
    """ Class for Auth Service Payloads """

    def create_user_payload(self, role="SysOps-client"):
        """ Payload to create user """
        payload = {
            "role": role
        }
        return payload

    def validate_user_credentials_payload(
            self, username="d7ee7d21-0dd0-4ad1-b656-032c3746bf0b",
            password="U3guXkIbBB4#5s5H",
            client_id="h4psC1NTevUPYCJ6hTa76htrup4UNIyq"):
        """ Payload to validate user credentials """
        payload = {
            "username": username,
            "password": password,
            "client_id": client_id
        }
        return payload
