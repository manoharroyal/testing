import logging
import unittest
import httplib
from test.functional_test_suite.common.config import AUTH_SERVICE_URL, \
    delete_auth_user_url, validate_auth_user_url, initialize_logger
from test.shared.rest_framework import RestAPI, RequestType, path
from test.functional_test_suite.auth_service.auth_service_payloads import AuthServicePayload

auth_service = RestAPI(utype='sysops')
auth_service_invalid = RestAPI(utype='invalid')
initialize_logger(path + '/../../logs/auth_service.log')


class AuthService(unittest.TestCase):
    """ Test cases for the auth service """

    """ POST: Create user for given role """

    def test_create_user_with_valid_details(self):

        create_auth_user_response = auth_service.request(
            RequestType.POST, AUTH_SERVICE_URL,
            payload=AuthServicePayload().create_user_payload())
        create_auth_user_response_dict = create_auth_user_response.json()
        logging.info('test_create_user_with_valid_details')
        logging.info('Url is %s', AUTH_SERVICE_URL)
        logging.info('Request is %s', AuthServicePayload().create_user_payload())
        logging.info("Response is %s" % create_auth_user_response.text)
        key = "roles"
        self.assertEquals(
            create_auth_user_response.status_code, 201,
            msg="Expected 201 and got is %s (%s)" %
                (create_auth_user_response.status_code,
                 httplib.responses[create_auth_user_response.status_code]))
        self.assertIn(
            key, create_auth_user_response_dict.keys(),
            msg="Expected %s in %s" %
                (key, create_auth_user_response_dict.keys))
        userid = create_auth_user_response_dict['userId']
        return userid

    def test_create_user_with_invalid_token(self):
        """ Create user for given role with invalid token """

        expected_message = "Unauthorized"

        create_auth_user_response = auth_service_invalid.request(
            RequestType.POST, AUTH_SERVICE_URL,
            payload=AuthServicePayload().create_user_payload())
        create_auth_user_response_dict = create_auth_user_response.json()
        logging.info('test_create_user_with_invalid_token')
        logging.info('Url is %s', AUTH_SERVICE_URL)
        logging.info('Request is %s',
                     AuthServicePayload().create_user_payload())
        logging.info("Response is %s" % create_auth_user_response.text)
        self.assertEquals(
            create_auth_user_response.status_code, 401,
            msg="Expected 401 and got is %s (%s)" %
                (create_auth_user_response.status_code,
                 httplib.responses[create_auth_user_response.status_code]))
        self.assertEquals(
            expected_message, create_auth_user_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, create_auth_user_response_dict['message']))

    def test_create_user_with_invalid_roles(self):

        expected_message = "role is not supported"

        create_auth_user_response = auth_service.request(
            RequestType.POST, AUTH_SERVICE_URL,
            payload=AuthServicePayload().create_user_payload(role="@#"))
        create_auth_user_response_dict = create_auth_user_response.json()
        logging.info('test_create_user_with_invalid_roles')
        logging.info('Url is %s', AUTH_SERVICE_URL)
        logging.info('Request is %s',
                     AuthServicePayload().create_user_payload(role="@#"))
        logging.info("Response is %s" % create_auth_user_response.text)
        self.assertEquals(
            create_auth_user_response.status_code, 400,
            msg="Expected 400 and got is %s (%s)" %
                (create_auth_user_response.status_code,
                 httplib.responses[create_auth_user_response.status_code]))
        self.assertEquals(
            expected_message, create_auth_user_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, create_auth_user_response_dict['message']))

    def test_create_user_without_roles(self):

        expected_message = "role is not present in request body"

        create_auth_user_response = auth_service.request(
            RequestType.POST, AUTH_SERVICE_URL,
            payload=AuthServicePayload().create_user_payload(role=""))
        create_auth_user_response_dict = create_auth_user_response.json()
        logging.info('test_create_user_without_roles')
        logging.info('Url is %s', AUTH_SERVICE_URL)
        logging.info('Request is %s',
                     AuthServicePayload().create_user_payload(role=""))
        logging.info("Response is %s" % create_auth_user_response.text)
        self.assertEquals(
            create_auth_user_response.status_code, 400,
            msg="Expected 400 and got is %s (%s)" %
                (create_auth_user_response.status_code,
                 httplib.responses[create_auth_user_response.status_code]))
        self.assertEquals(
            expected_message, create_auth_user_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, create_auth_user_response_dict['message']))

    """ POST: validate the auth user for given role """

    def test_validate_auth_user_with_valid_details(self):

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload())
        validate_auth_user_response_dict = validate_auth_user_response.json()
        logging.info('test_validate_auth_user_with_valid_details')
        logging.info('Url is %s', validate_auth_user_url)
        logging.info('Request is %s',
                     AuthServicePayload().validate_user_credentials_payload())
        logging.info("Response is %s" % validate_auth_user_response.text)
        key = 'userId'
        self.assertEquals(
            validate_auth_user_response.status_code, 200,
            msg=("Expected code is 200 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses[validate_auth_user_response.status_code])))
        self.assertIn(key, validate_auth_user_response_dict.keys(),
                      msg="Expected %s in and got is %s" % (
                          key, validate_auth_user_response_dict.keys()))

    def test_validate_auth_user_with_invalid_user_id(self):

        expected_message = "User not found"

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload
            (username="@3"))
        validate_auth_user_response_dict = validate_auth_user_response.json()
        logging.info('test_validate_auth_user_with_invalid_user_id')
        logging.info('Url is %s', validate_auth_user_url)
        logging.info('Request is %s',
                     AuthServicePayload().validate_user_credentials_payload
                     (username="@3"))
        logging.info("Response is %s" % validate_auth_user_response.text)
        self.assertEquals(
            validate_auth_user_response.status_code, 404,
            msg=("Expected code is 404 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses[validate_auth_user_response.status_code])))
        self.assertEquals(
            expected_message, validate_auth_user_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, validate_auth_user_response_dict['message']))

    def test_validate_auth_user_with_invalid_password(self):

        expected_message = "Invalid credentials"

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload
            (password="1@"))
        validate_auth_user_response_dict = validate_auth_user_response.json()
        logging.info('test_validate_auth_user_with_invalid_password')
        logging.info('Url is %s', validate_auth_user_url)
        logging.info('Request is %s',
                     AuthServicePayload().validate_user_credentials_payload
                     (password="1@"))
        logging.info("Response is %s" % validate_auth_user_response.text)
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses[validate_auth_user_response.status_code])))
        self.assertEquals(
            expected_message, validate_auth_user_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, validate_auth_user_response_dict['message']))

    def test_validate_auth_user_with_invalid_client_id(self):

        expected_message = "Client_id is not valid"

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload
            (client_id="1@"))
        validate_auth_user_response_dict = validate_auth_user_response.json()
        logging.info('test_validate_auth_user_with_invalid_client_id')
        logging.info('Url is %s', validate_auth_user_url)
        logging.info('Request is %s',
                     AuthServicePayload().validate_user_credentials_payload
                     (client_id="1@"))
        logging.info("Response is %s" % validate_auth_user_response.text)
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses[validate_auth_user_response.status_code])))
        self.assertEquals(
            expected_message, validate_auth_user_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, validate_auth_user_response_dict['message']))

    def test_validate_auth_user_without_user_id(self):

        expected_message = "Internal server error"

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload
            (username=""))
        validate_auth_user_response_dict = validate_auth_user_response.json()
        logging.info('test_validate_auth_user_without_user_id')
        logging.info('Url is %s', validate_auth_user_url)
        logging.info('Request is %s',
                     AuthServicePayload().validate_user_credentials_payload
                     (username=""))
        logging.info("Response is %s" % validate_auth_user_response.text)
        self.assertEquals(
            validate_auth_user_response.status_code, 500,
            msg=("Expected code is 500 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses[validate_auth_user_response.status_code])))
        self.assertEquals(
            expected_message, validate_auth_user_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, validate_auth_user_response_dict['message']))

    def test_validate_auth_user_without_password(self):

        expected_message = "Invalid credentials"

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload
            (password=""))
        validate_auth_user_response_dict = validate_auth_user_response.json()
        logging.info('test_validate_auth_user_without_password')
        logging.info('Url is %s', validate_auth_user_url)
        logging.info('Request is %s',
                     AuthServicePayload().validate_user_credentials_payload
                     (password=""))
        logging.info("Response is %s" % validate_auth_user_response.text)
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses[validate_auth_user_response.status_code])))
        self.assertEquals(
            expected_message, validate_auth_user_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, validate_auth_user_response_dict['message']))

    def test_validate_auth_user_without_client_id(self):

        expected_message = "Client_id is not valid"

        validate_auth_user_response = auth_service.request(
            RequestType.POST, validate_auth_user_url,
            payload=AuthServicePayload().validate_user_credentials_payload
            (client_id=""))
        validate_auth_user_response_dict = validate_auth_user_response.json()
        logging.info('test_validate_auth_user_without_client_id')
        logging.info('Url is %s', validate_auth_user_url)
        logging.info('Request is %s',
                     AuthServicePayload().validate_user_credentials_payload
                     (client_id=""))
        logging.info("Response is %s" % validate_auth_user_response.text)
        self.assertEquals(
            validate_auth_user_response.status_code, 400,
            msg=("Expected code is 400 and got is %s (%s)" %
                 (validate_auth_user_response.status_code,
                  httplib.responses[validate_auth_user_response.status_code])))
        self.assertEquals(
            expected_message, validate_auth_user_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, validate_auth_user_response_dict['message']))

    """ DELETE: Delete the user with user name """

    def test_zdelete_user_with_valid_user_id(self):
        """ testing with valid user id to delete the user """

        userid = self.test_create_user_with_valid_details()
        auth_service_response = auth_service.request(
            RequestType.DELETE, delete_auth_user_url(user_id=userid))
        logging.info('test_delete_user_with_valid_user_id')
        logging.info('Url is %s', delete_auth_user_url(user_id=userid))
        logging.info("Response is %s" % auth_service_response.text)
        self.assertEquals(
            auth_service_response.status_code, 204,
            msg="Expected 204 and got is %s (%s)" %
                (auth_service_response.status_code,
                 httplib.responses[auth_service_response.status_code]))

    def test_delete_user_with_invalid_user_id(self):
        """ testing with valid user id to delete the user """

        expected_message = "User not found"

        auth_service_response = auth_service.request(
            RequestType.DELETE, delete_auth_user_url('you@#'))
        logging.info('test_delete_user_with_invalid_user_id')
        logging.info('Url is %s', delete_auth_user_url('you@#'))
        logging.info("Response is %s" % auth_service_response.text)
        auth_service_response_dict = auth_service_response.json()
        self.assertEquals(
            auth_service_response.status_code, 404,
            msg="Expected 404 and got is %s (%s)" %
                (auth_service_response.status_code,
                 httplib.responses[auth_service_response.status_code]))
        self.assertEquals(
            expected_message, auth_service_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, auth_service_response_dict['message']))

    def test_delete_user_with_invalid_token(self):
        """ testing with valid user id to delete the user """

        expected_message = "Unauthorized"

        auth_service_response = auth_service_invalid.request(
            RequestType.DELETE, delete_auth_user_url(user_id='you@#'))
        auth_service_response_dict = auth_service_response.json()
        logging.info('test_delete_user_with_invalid_token')
        logging.info('Url is %s', delete_auth_user_url(user_id='you@#'))
        logging.info("Response is %s" % auth_service_response.text)
        self.assertEquals(
            auth_service_response.status_code, 401,
            msg="Expected 401 and got is %s (%s)" %
                (auth_service_response.status_code,
                 httplib.responses[auth_service_response.status_code]))
        self.assertEquals(
            expected_message, auth_service_response_dict['message'],
            msg="Expected %s equals %s" %
                (expected_message, auth_service_response_dict['message']))
