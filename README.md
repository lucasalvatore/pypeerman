[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# pypeerman
Python library for the Peering Manager API <br> https://github.com/peering-manager/peering-manager

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

To update an object (HTTP patch) data must be a list containing a dict with the updated data.

The dict must contain the ID of the object(s) to change as the first key,value

for example:
```
payload = [
    {'id': 4491, 'tags': [{'name': 'this-is-a-tag'}]},
    {'id': 1881, 'tags': [{'name': 'this-is-a-tag'}]}
]
r = pm.peering.internet_exchange_peering_sessions.update(payload)
```

or another example:

```
payload = [
    {'id': 4491, 'status': 'disabled'},
    {'id': 1881, 'status': 'maintenance'}
]
r = pm.peering.internet_exchange_peering_sessions.update(payload)
```
If the patch is successfull the full object(s) will be returned in a list
