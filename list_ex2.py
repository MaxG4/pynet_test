#!/usr/bin/env python
from __future__ import print_function

ip_add = "192.168.13.1"

my_IP_list = ip_add.split(".")

my_IP_list[-1] = 0

print()
print("{:<10} {:<10} {:<10} {:<10}".format("Octect1", "Octect2", "Octect3", "Octect4"))
print("{:<10} {:<10} {:<10} {:<10}".format(*my_IP_list))
print()
