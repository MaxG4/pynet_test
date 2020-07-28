import os
from getpass import getpass
from jnpr.junos import Device
from pprint import pprint

password = os.getenv("JNPR_PASSWORD")
if password is None:
    password = getpass("Enter vMX password: ")

my_dev = Device(host="vmx1.lasthop.io", user="pyclass", password=password)

my_dev.open()

print()
print("device facts")
pprint(my_dev.facts)
