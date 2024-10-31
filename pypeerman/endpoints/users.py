from pypeerman.endpoints import PeeringEndpoint


class Users:
    def __init__(self, pm_instance):
        self.pm_instance = pm_instance
        resource_name = self.__class__.__name__.lower()
        # Initialize each endpoint
        self.groups = PeeringEndpoint(pm_instance, resource_name, "groups")
        self.userpref = PeeringEndpoint(pm_instance, resource_name, "userpref")
        self.users = PeeringEndpoint(pm_instance, resource_name, "users")
