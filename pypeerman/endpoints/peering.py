from pypeerman.endpoints import PeeringEndpoint, PeeringSubEndpoint


class Peering:
    def __init__(self, pm_instance):
        self.pm_instance = pm_instance
        resource_name = self.__class__.__name__.lower()
        # Initialize each endpoint
        self.autonomous_systems = PeeringEndpoint(
            pm_instance, resource_name, "autonomous-systems"
        )
        self.bgp_groups = PeeringEndpoint(pm_instance, resource_name, "bgp-groups")
        self.communities = PeeringEndpoint(pm_instance, resource_name, "communities")
        self.direct_peering_sessions = PeeringEndpoint(
            pm_instance, resource_name, "direct-peering-sessions"
        )
        self.internet_exchange_peering_sessions = PeeringEndpoint(
            pm_instance, resource_name, "internet-exchange-peering-sessions"
        )
        self.internet_exchanges = PeeringEndpoint(
            pm_instance, resource_name, "internet-exchanges"
        )
        self.routers = PeeringEndpoint(pm_instance, resource_name, "routers")
        self.routing_policies = PeeringEndpoint(
            pm_instance, resource_name, "routing-policies"
        )
