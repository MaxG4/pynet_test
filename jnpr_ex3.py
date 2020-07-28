import os
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import LockError
from jnpr.junos.utils.config import Config

# Use getpass
password = os.getenv("JNPR_PASSWORD")
if password is None:
    password = getpass("Enter vMX password: ")

# create device object and use open method to connect
a_device = Device(host="vmx2.lasthop.io", user="pyclass", password=password)
a_device.open()

# create config object
cfg = Config(a_device)

# lock configuration
# cfg.lock()

# lock status
print()
try:
    cfg.lock()
    print("Lock acquired!")
except LockError:
    print("Device is already locked.")

# unlock config
cfg.unlock()
