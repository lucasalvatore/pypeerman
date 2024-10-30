from pypeerman.endpoints.peering import Peering


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
        self.peering = Peering(self)

