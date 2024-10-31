from pypeerman.lib.api import make_request, fetch_all


class BaseEndpoint:
    def __init__(
        self, pm_instance, resource_name, endpoint_name, sub_endpoint_name=None
    ):
        self.pm_instance = pm_instance
        self.resource_name = resource_name
        self.endpoint_name = endpoint_name
        self.sub_endpoint_name = sub_endpoint_name

    def get(self, id=None):
        if id and self.sub_endpoint_name:
            # e.g /internet-exchanges/{id}/available-peers
            endpoint = f"/api/{self.resource_name}/{self.endpoint_name}/{id}/{self.sub_endpoint_name}/"
        elif id:
            # e.g /internet-exchanges/{id}
            endpoint = f"/api/{self.resource_name}/{self.endpoint_name}/{id}/"
        else:
            raise ValueError("ID is required when using get().")

        return make_request(
            self.pm_instance.base_url, self.pm_instance.headers, endpoint
        )

    def all(self, id=None):
        if id and self.sub_endpoint_name:
            endpoint = f"/api/{self.resource_name}/{self.endpoint_name}/{id}/{self.sub_endpoint_name}/"
        else:
            endpoint = f"/api/{self.resource_name}/{self.endpoint_name}/"

        return fetch_all(self.pm_instance.base_url, self.pm_instance.headers, endpoint)


class PeeringEndpoint(BaseEndpoint):
    def __init__(self, pm_instance, resource_name, endpoint_name):
        super().__init__(pm_instance, resource_name, endpoint_name)
        # Initialize sub-endpoints as attributes
        self.available_peers = PeeringSubEndpoint(
            pm_instance, resource_name, endpoint_name, "available-peers"
        )
        self.prefixes = PeeringSubEndpoint(
            pm_instance, resource_name, endpoint_name, "prefixes"
        )
        self.configuration = PeeringSubEndpoint(
            pm_instance, resource_name, endpoint_name, "configuration"
        )
        self.test_napalm_connection = PeeringSubEndpoint(
            pm_instance, resource_name, endpoint_name, "test-napalm-connection"
        )


class PeeringSubEndpoint(BaseEndpoint):
    def __init__(self, pm_instance, resource_name, parent_endpoint, sub_endpoint_name):
        super().__init__(pm_instance, resource_name, parent_endpoint, sub_endpoint_name)
