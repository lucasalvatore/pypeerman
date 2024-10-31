from pypeerman.endpoints import PeeringEndpoint


class Net:
    def __init__(self, pm_instance):
        self.pm_instance = pm_instance
        resource_name = self.__class__.__name__.lower()
        # Initialize each endpoint
        self.connections = PeeringEndpoint(pm_instance, resource_name, "connections")
