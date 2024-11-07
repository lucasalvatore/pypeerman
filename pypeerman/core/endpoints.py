from pypeerman.lib.api import make_request, fetch_all, make_patch


class BaseEndpoint:
    def __init__(
        self, pm_instance, resource_name, parent_path="", sub_endpoint_name=None
    ):
        self.pm_instance = pm_instance
        self.resource_name = resource_name.replace("_", "-")
        self.parent_path = parent_path.strip("/")
        self.sub_endpoint_name = sub_endpoint_name

    def get(self, id=None):
        if self.sub_endpoint_name and id:
            # e.g /internet-exchanges/{id}/available-peers
            endpoint = f"/api/{self.parent_path}/{id}/{self.sub_endpoint_name}/"
        else:
            # e.g /internet-exchanges/{id}
            endpoint = f"/api/{self.parent_path}/{self.resource_name}/{id}/"

        return make_request(
            self.pm_instance.base_url, self.pm_instance.headers, endpoint
        )

    def all(self, parent_id=None):
        if self.sub_endpoint_name and parent_id:
            endpoint = f"/api/{self.parent_path}/{parent_id}/{self.sub_endpoint_name}/"
        else:
            endpoint = f"/api/{self.parent_path}/{self.resource_name}/"

        return fetch_all(self.pm_instance.base_url, self.pm_instance.headers, endpoint)

    def update(self, payload):
        results = []
        if not payload:
            raise ValueError("Payload must be inculded when using update")
        if not isinstance(payload, list):
            raise TypeError("Payload must be a list")

        for item in payload:
            endpoint = f"/api/{self.parent_path}/{self.resource_name}/{item.get('id')}/"
            data = {}
            k, v = list(item.items())[1]
            data[k] = v
            patch = make_patch(
                self.pm_instance.base_url, self.pm_instance.headers, endpoint, data
            )
            if patch.status_code == 200:
                results.append(
                    make_request(
                        self.pm_instance.base_url, self.pm_instance.headers, endpoint
                    )
                )
            else:
                raise ValueError(
                    f"Error while updating object id {item['id']}: {patch.text}"
                )
        return results


class DynamicEndpoint(BaseEndpoint):
    def __init__(self, pm_instance, resource_name, parent_path=""):
        super().__init__(pm_instance, resource_name, parent_path)

    def __getattr__(self, name):
        if self.parent_path:
            return SubEndpoint(
                self.pm_instance, name, f"{self.parent_path}/{self.resource_name}"
            )
        return DynamicEndpoint(self.pm_instance, name, self.resource_name)


class SubEndpoint(BaseEndpoint):
    def __init__(self, pm_instance, sub_endpoint_name, parent_path=""):
        super().__init__(pm_instance, sub_endpoint_name, parent_path)
        self.sub_endpoint_name = sub_endpoint_name.replace("_", "-")
