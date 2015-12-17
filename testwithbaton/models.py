from typing import List

from hgicommon.models import Model


class IrodsUser(Model):
    """
    Model of an iRODS user.
    """
    def __init__(self, username: str, password: str, zone: str, admin=False):
        self.username = username
        self.password = password
        self.zone = zone
        self.admin = admin


class IrodsServer(Model):
    """
    Model of an iRODS server.
    """
    def __init__(self, host: str, port: int, users: List[IrodsUser]):
        if not isinstance(port, int):
            raise ValueError("Port number must be an integer - `%s` given" % port.__class__)
        self.host = host
        self.port = port
        self.users = users


class ContainerisedIrodsServer(IrodsServer):
    """
    Model of an iRODS server that runs in a container.
    """
    def __init__(self, container: dict, host: str, port: int, users: List[IrodsUser]):
        super(ContainerisedIrodsServer, self).__init__(host, port, users)
        self.container = container
