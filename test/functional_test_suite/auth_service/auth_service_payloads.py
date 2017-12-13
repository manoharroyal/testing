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
            self, username="e3abf07d-82f2-43fd-bc95-1b4e9e7dc6d5",
            password="Q1aeKDnSh5q6q4AF",
            client_id="h4psC1NTevUPYCJ6hTa76htrup4UNIyq"):
        """ Payload to validate user credentials """
        payload = {
            "username": username,
            "password": password,
            "client_id": client_id
        }
        return payload
