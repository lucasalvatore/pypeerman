from pypeerman.endpoints import PeeringEndpoint


class Devices:
    def __init__(self, pm_instance):
        self.pm_instance = pm_instance
        resource_name = self.__class__.__name__.lower()
        # Initialize each endpoint
        self.configurations = PeeringEndpoint(
            pm_instance, resource_name, "configurations"
        )
        self.platforms = PeeringEndpoint(pm_instance, resource_name, "platforms")
