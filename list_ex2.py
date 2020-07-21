#!/usr/bin/env python
from __future__ import print_function

ip_add = "192.168.13.1"

my_ip_list = ip_add.split(".")

my_ip_list[-1] = 0

print()
print(*ip_add)
print("{:<10} {:<10} {:<10} {:<10}".format("Octect1", "Octect2", "Octect3", "Octect4"))
print("{:<10} {:<10} {:<10} {:<10}".format(*my_ip_list))
print()
