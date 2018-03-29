""" Agent service payloads """

agent_public_key = "-----BEGIN PUBLIC KEY-----MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA1zeqkPrMeiC5HpbWyr4U\nrk1nn4RRd6MMbtIWBAs9J59fnn+v8JxdvERX275PJGnkSYk1he6x/NKxxu2zf5El\nzDIl0xzsCo7fp6HGZj9dXlfk9v1J7tkQgHxOikbk/EIaUUimkjpNq20yUVrfskc+\n1UYJOAOonO4sfcc6MiDLBqNtQKDKmlHd+/23Z2IFOs22NVxd9cGLaNhVEvRglEPc\nq+cY9PX4RUZNLHjyMwZWUxN5BJc78qsPGJ8E0jMRAAM73V3UpDTMFHiSpeT/Vb2M\nSyn0CIIj1PqCP3aTec1ohlnnIeYTe9m1eMsrhCjSHWDNuc7AOOnPWWNOspqXdKSx\nhAp+nhmTHTMI04HkmSNyfObJlTDWc6EJ60Dlvvj/kHHLuW55p5y8Cjhy7qTVJ4y+\nBQp80nbHZL7gi7YTxUgwJ9V5YYwOsR30y9cg2q/cH7J/Zp2cEp9ia0FynnfaxAIa\nat7D6tL2nFDYvoEng4n8GwgjMPOtTYqKvPnZ4g6FVLZTL/GBuCZmInIaUL+Cy8G/\nok86jQK3dFavkmXmr2Z1yGy6EypabSoD/Zcivb1d8hhCg1pAatJJCISPA2yHv7EI\nzjH5w6NV65r4Xr+cf8e5lA6yizvtPQA0xNDpnUWffv3q7Qhk7SN3dVJylSSowgwS\nyHuI8gaM1Ju97BO6udWzjZUCAwEAAQ==-----END PUBLIC KEY-----"


class AgentServicePayload(object):
    """ Agent Service Payload """

    def update_agent_task_status(self, status='DONE',
                                 message='task completed successfully'):
        """ update status of agent """
        payload = {
            "status": status,
            "message": message
        }
        return payload

    def register_agent(self, username='testagent', password='testpswd',
                       agent_public_key=agent_public_key):
        """ Payload to register an agent """
        payload = {
            "username": username,
            "password": password,
            "agent_public_key": agent_public_key
        }
        return payload