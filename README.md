# pypeerman
Python library for the Peering Manager API

## Usage

Use `.get(id)` to get a single object from an endpoint
use `.all()` to get all objects from an endpoint

Returns a json object containing the data

 ### Example

```
import pypeerman
PM = pypeerman.PMEnv("http://peering-manager.mydomain.com", "my-api-token")

direct_session = PM.peering.direct_peering_sessions.get(585)
ix_session = PM.peering.internet_exchange_peering_sessions.get(430)
all_sessions = PM.peering.internet_exchange_peering_sessions.all()
```