[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# pypeerman
Python library for the Peering Manager API

## Installation

for now just `pip install .`

## Usage

Use `.get(id)` to get a single object from an endpoint

Use `.all()` to get all objects from an endpoint

Returns a json object containing the data

All endpoints represented in the API are available


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

To do a HTTP patch use `.update(id, payload)`

for example:
```
payload = {"tags": [{"name": "this-is-a-tag"}]}
r = pm.peering.internet_exchange_peering_sessions.update(10, payload)
```