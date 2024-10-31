# pypeerman
Python library for the Peering Manager API

## Installation

for now just `pip install .`

## Usage

Use `.get(id)` to get a single object from an endpoint

use `.all()` to get all objects from an endpoint

Returns a json object containing the data

All endpoints represented in the API are available

Only http gets are currently suported.

 ### Examples

```
import pypeerman
pm = pypeerman.PMEnv("http://peering-manager.mydomain.com", "my-api-token")

pm.peering.direct_peering_sessions.get(585)
pm.peering.internet_exchange_peering_sessions.get(430)
pm.peering.internet_exchange_peering_sessions.all()
pm.users.get(1)
pm.bgp.relationships.get(1)
```

Subendpoints also work in the same way:
```
pm.peering.internet_exchanges.available_peers.get(30)
```