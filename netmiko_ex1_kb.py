import os
from getpass import getpass
from netmiko import ConnectHandler

sros_password = os.getenv("SROS_PASSWORD")
if sros_password is None:
    sros_password = getpass("Enter SROS password: ")

vmx_password = os.getenv("JNPR_PASSWORD")
if vmx_password is None:
    vmx_password = getpass("Enter vMX password: ")

sros1 = {
    "device_type": "nokia_sros",
    "host": "sros.lasthop.io",
    "username": "admin",
    "password": "admin",
    "port": 2211,
}
vmx1 = {
    "device_type": "juniper_junos",
    "host": "vmx1.lasthop.io",
    "username": "pyclass",
    "password": "88newclass",
}

for a_device in (sros1, vmx1):
    net_connect = ConnectHandler(**a_device)
    print("Current Prompt: " + net_connect.find_prompt())

    show_ver = net_connect.send_command("show version")
    print()
    print(show_ver)
    print()

if "nokia_sros" in a_device["device_type"]:
    cmd = "admin display-config"
elif "juniper_junos" in a_device["device_type"]:
    cmd = "show config"

show_run = net_connect.send_command("show_run")
print()
print(show_run)
print()
