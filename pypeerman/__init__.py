from pypeerman.endpoints.bgp import Bgp
from pypeerman.endpoints.core import Core
from pypeerman.endpoints.devices import Devices
from pypeerman.endpoints.extras import Extras
from pypeerman.endpoints.messaging import Messaging
from pypeerman.endpoints.net import Net
from pypeerman.endpoints.peering import Peering
from pypeerman.endpoints.peeringdb import Peeringdb
from pypeerman.endpoints.schema import Schema
from pypeerman.endpoints.status import Status
from pypeerman.endpoints.users import Users


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
        self.bgp = Bgp(self)
        self.core = Core(self)
        self.devices = Devices(self)
        self.extras = Extras(self)
        self.messaging = Messaging(self)
        self.net = Net(self)
        self.peering = Peering(self)
        self.peeringdb = Peeringdb(self)
        self.schema = Schema(self)
        self.status = Status(self)
        self.users = Users(self)
