import pypeerman
pm = pypeerman.PMEnv("", "token")

"""
Some basic tests.  Others will need to change the IDs used for match their own environment
"""

print("running pm.peering.internet_exchanges.all()")
r = pm.peering.internet_exchanges.all()
if r:
    print("test: 'pm.peering.internet_exchanges.all()' was successfull")
else:
    print("test failed")
print()

print("running pm.bgp.relationships.get(1)")
r = pm.bgp.relationships.get(1)
if r:
    print("test: 'pm.bgp.relationships.get(1)' was successfull")
else:
    print("test failed")
print()

print("running pm.core.jobs.get(19535)")
r = pm.core.jobs.get(19535)
if r:
    print("test: pm.core.jobs.get(19535) was successfull")
else:
    print("test failed")
print()

print("running pm.peering.internet_exchanges.get(30)")
r = pm.peering.internet_exchanges.get(30)
if r:
    print("test: pm.peering.internet_exchanges.get(30) was successfull")
else:
    print("test failed")
print()

print("running pm.peering.internet_exchanges.available_peers.get(37)")
r = pm.peering.internet_exchanges.available_peers.get(37)
if r:
    print("test pm.peering.internet_exchanges.available_peers.get(37) was successfull")
else:
    print("test failed")
print()

print("running pm.peering.internet_exchanges.prefixes.get(38)")
r = pm.peering.internet_exchanges.prefixes.get(38)
if r:
    print("test pm.peering.internet_exchanges.prefixes.get(38) was successfull")
else:
    print("test failed")
print()

print("running pm.devices.configurations.all()")
r = pm.devices.configurations.all()
if r:
    print("test pm.devices.configurations.all() was successfull")
else:
    print("test failed")
print()


print("running pm.devices.configurations.get(4)")
r = pm.devices.configurations.get(4)
if r:
    print("test pm.devices.get(4) was successfull")
else:
    print("test failed")
print()


print("running pm.peering.routers.all()")
r = pm.peering.routers.all()
if r:
    print("test  pm.peering.routers.all() was successfull")
else:
    print("test failed")
print()

print("running pm.peering.routers.configuration.get(175)")
r = pm.peering.routers.configuration.get(175)
if r:
    print("test  pm.peering.routers.configuration.get(175) was successfull")
else:
    print("test failed")
print()
