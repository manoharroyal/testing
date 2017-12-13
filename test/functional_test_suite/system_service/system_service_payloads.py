""" System service payloads """


class SystemServicePayload(object):
    """ Payloads for system service """

    SYSTEM_DETAILS = {
        "details": {
            "system_name": "TDCLOUD15TD11",
            "bynet": {
                "PMA": "72",
                "bynet0": {
                    "ip": "10.20.2.8",
                    "net_mask": "255.255.0.0"
                },
                "bynet1": {
                    "ip": "10.16.2.8",
                    "net_mask": "255.255.0.0"
                }
            },
            "node_ip": {
                "interface": "eth0",
                "ip": "10.21.130.8",
                "mask": "255.255.0.0"
            },
            "dc_ip": {
                "interface": "eth3",
                "ip": "10.25.152.62",
                "mask": "255.255.254.0"
            },
            "version": {
                "BLM driver": "03.07.03.02",
                "BLM protocol": "15.07.27.15",
                "database_version": "15.10.02.04",
                "BLM commands": "03.07.03.02"
            },
            "host_name": "TDCLOUD15TD10-2-8",
            "nodes": [
                {
                    "short_hostname": [
                        "TDCLOUD15TD10-2-8"
                    ],
                    "ip": "10.22.130.8",
                    "name": "TDCLOUD15TD10",
                    "full_qualified_hostname": "SMP002-8"
                }
            ]
        }
    }

    def system_creation_payload(self, system_type='source',
                                system_name="TDCLOUD15TD12",
                                details=SYSTEM_DETAILS["details"]):
        """ Request body for creation of seed job"""

        payload = {
            "system_type": system_type,
            "system_name": system_name,
            "details": details
        }
        return payload

    def system_deletion_payload(self, del_param=None):
        """ payload to delete the system """

        payload = self.system_creation_payload()
        if del_param is None:
            print ("parameter should be passed")
        else:
            payload.pop(del_param)
        return payload