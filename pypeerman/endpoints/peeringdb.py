from pypeerman.endpoints import PeeringEndpoint


class Peeringdb:
    def __init__(self, pm_instance):
        self.pm_instance = pm_instance
        resource_name = self.__class__.__name__.lower()
        # Initialize each endpoint
        self.campuses = PeeringEndpoint(pm_instance, resource_name, "campuses")
        self.facilities = PeeringEndpoint(pm_instance, resource_name, "facilities")
        self.internet_exchange_facilities = PeeringEndpoint(
            pm_instance, resource_name, "internet-exchange-facilities"
        )
        self.internet_exchanges = PeeringEndpoint(
            pm_instance, resource_name, "internet-exchanges"
        )
        self.ixlan_prefixes = PeeringEndpoint(
            pm_instance, resource_name, "ixlan-prefixes"
        )
