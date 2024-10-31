from pypeerman.endpoints import PeeringEndpoint


class Bgp:
    def __init__(self, pm_instance):
        self.pm_instance = pm_instance
        resource_name = self.__class__.__name__.lower()
        # Initialize each endpoint
        self.relationships = PeeringEndpoint(
            pm_instance, resource_name, "relationships"
        )
