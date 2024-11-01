from pypeerman.endpoints import DynamicEndpoint

class PMEnv:
    def __init__(self, URL: str, KEY: str):
        if not (URL and KEY):
            raise ValueError("Could not find peering-manager URL or API Key")
        self.base_url = URL
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"token {KEY}",
            "Content-Type": "application/json",
        }
        self.bgp = DynamicEndpoint(self, "bgp")
        self.core = DynamicEndpoint(self, "core")
        self.devices = DynamicEndpoint(self, "devices")
        self.extras = DynamicEndpoint(self, "extras")
        self.messaging = DynamicEndpoint(self, "messaging")
        self.net = DynamicEndpoint(self, "net")
        self.peering = DynamicEndpoint(self, "peering")
        self.peeringdb = DynamicEndpoint(self, "peeringdb")
        self.schema = DynamicEndpoint(self, "schema")
        self.status = DynamicEndpoint(self, "status")
        self.users = DynamicEndpoint(self, "users")
