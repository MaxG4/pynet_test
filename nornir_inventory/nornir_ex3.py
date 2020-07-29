from nornir import InitNornir

nr = InitNornir(config_file="./config.yaml")

sros3 = nr.inventory.hosts["sros3"]

print()
print(f"Name: {sros3.name}")
print(f"Host: {sros3.hostname}")
print(f"Port: {sros3.port}")
print(f"Groups: {sros3.groups}")
print(f"Platform: {sros3.platform}")
print(f"Platform: {sros3.username}")
print(f"Platform: {sros3.password}")
print()
