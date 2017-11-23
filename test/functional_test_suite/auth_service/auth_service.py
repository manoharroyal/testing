import logging
import unittest
import httplib
import requests
from test.functional_test_suite.common.config import AUTH_SERVICE_URL, \
    delete_auth_user_url, validate_auth_user_url
from test.shared.rest_framework import RestAPIHeader, RequestType
from test.functional_test_suite.common.payloads import AuthServicePayload
auth_service = RestAPIHeader()


class AuthService(unittest.TestCase):
    """ Test cases for the auth service """

    """ DELETE: Delete the user with user name """

    def test_delete_user_with_valid_user_id(self):
        """ testing with valid user id to delete the user """

        auth_service_response = auth_service.request(
            RequestType.DELETE, delete_auth_user_url('your'))
        logging.info("Response is %s" % auth_service_response.text)
        self.assertEquals(
            auth_service_response.status_code, 200,
            msg="Expected 200 and got is %s (%s)" %
                (auth_service_response.status_code,
                 httplib.responses(auth_service_response.status_code)))

    def test_delete_user_with_invalid_user_id(self):
        """ testing with valid user id to delete the user """

        auth_service_response = auth_service.request(
            RequestType.DELETE, delete_auth_user_url('you@#'))
        logging.info("Response is %s" % auth_service_response.text)
        self.assertEquals(
            auth_service_response.status_code, 400,
            msg="Expected 400 and got is %s (%s)" %
                (auth_service_response.status_code,
                 httplib.responses(auth_service_response.status_code)))

    """ POST: Create user for given role """

    def test_create_user_with_valid_details(self):

        create_auth_user_response = auth_service.request(
            RequestType.POST, AUTH_SERVICE_URL,
            payload=AuthServicePayload().create_user_payload())
        logging.info("Response is %s" % create_auth_user_response.text)
        self.assertEquals(create_auth_user_response.status_code, 200,
                          msg="Expected 200 and got is %s (%s)" %
                              (create_auth_user_response.status_code,
                               httplib.responses(create_auth_user_response.status_code)))

    def test_create_user_with_invalid_url(self):

        create_auth_user_response = auth_service.request(
            RequestType.POST, AUTH_SERVICE_URL + "12",
            payload=AuthServicePayload().create_user_payload())
        logging.info("Response is %s" % create_auth_user_response.text)
        self.assertEquals(create_auth_user_response.status_code, 403,
                          msg="Expected 403 and got is %s (%s)" %
                              (create_auth_user_response.status_code,
                               httplib.responses(create_auth_user_response.status_code)))

    def test_create_user_with_invalid_roles(self):

        create_auth_user_response = auth_service.request(
            RequestType.POST, AUTH_SERVICE_URL,
            payload=AuthServicePayload().create_user_payload(roles="@#"))
        logging.info("Response is %s" % create_auth_user_response.text)
        self.assertEquals(create_auth_user_response.status_code, 200,
                          msg="Expected 200 and got is %s (%s)" %
                              (create_auth_user_response.status_code,
                               httplib.responses(create_auth_user_response.status_code)))

    def test_create_user_without_roles(self):

        create_auth_user_response = auth_service.request(
            RequestType.POST, AUTH_SERVICE_URL,
            payload=AuthServicePayload().create_user_payload(roles=""))
        logging.info("Response is %s" % create_auth_user_response.text)
        self.assertEquals(create_auth_user_response.status_code, 200,
                          msg="Expected 200 and got is %s (%s)" %
                              (create_auth_user_response.status_code,
                               httplib.responses(create_auth_user_response.status_code)))

    """ POST: validate the auth user for given role """

    def test_validate_auth_user_with_valid_details(self):

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload())
        self.assertEquals(
            validate_auth_user_response.status_code, 200,
            msg=("Expected code is 200 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses(validate_auth_user_response.status_code))))

    def test_validate_auth_user_with_invalid_url(self):

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url + "12",
            payload=AuthServicePayload().validate_user_credentials_payload())
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses(validate_auth_user_response.status_code))))

    def test_validate_auth_user_with_invalid_user_id(self):

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload(userId="@#"))
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses(validate_auth_user_response.status_code))))

    def test_validate_auth_user_with_invalid_password(self):

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload(password="1@"))
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses(validate_auth_user_response.status_code))))

    def test_validate_auth_user_with_invalid_client_id(self):

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload(client_id="1@"))
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses(validate_auth_user_response.status_code))))

    def test_validate_auth_user_without_user_id(self):

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload(userId=""))
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses(validate_auth_user_response.status_code))))

    def test_validate_auth_user_without_password(self):

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload(password=""))
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses(validate_auth_user_response.status_code))))

    def test_validate_auth_user_without_client_id(self):

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload(client_id=""))
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses(validate_auth_user_response.status_code))))
