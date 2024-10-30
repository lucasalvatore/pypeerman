# peering.py

from pypeerman.lib.api import make_request, fetch_all

class PeeringEndpoint:
    def __init__(self, pm_instance, endpoint_name):
        self.pm_instance = pm_instance
        self.endpoint_name = endpoint_name

    def get(self, id=None):
        if id:
            endpoint = f"/api/peering/{self.endpoint_name}/{id}/"
        else:
            raise ValueError("ID is required when using get()"
                             "Use all() to pull all data without passing an ID"
                             )
        return make_request(self.pm_instance.base_url, self.pm_instance.headers, endpoint)

    def all(self):
        endpoint = f"/api/peering/{self.endpoint_name}/"
        return fetch_all(self.pm_instance.base_url, self.pm_instance.headers, endpoint)

class Peering:
    def __init__(self, pm_instance):
        self.pm_instance = pm_instance
        # Initialize each endpoint
        self.autonomous_systems = PeeringEndpoint(pm_instance, "autonomous-systems")
        self.bgp_groups = PeeringEndpoint(pm_instance, "bgp-groups")
        self.communities = PeeringEndpoint(pm_instance, "communities")
        self.direct_peering_sessions = PeeringEndpoint(pm_instance, "direct-peering-sessions")
        self.internet_exchange_peering_sessions = PeeringEndpoint(pm_instance, "internet-exchange-peering-sessions")
        self.internet_exchanges = PeeringEndpoint(pm_instance, "internet-exchanges")
        self.routers = PeeringEndpoint(pm_instance, "routers")
        self.routing_policies = PeeringEndpoint(pm_instance, "routing-policies")
