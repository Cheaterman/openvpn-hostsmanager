#!/usr/bin/env python3
import os


current_hosts = []

with open('dnsmasq/hosts') as hosts:
    for line in hosts:
        if not line:
            continue

        current_hosts.append(line.strip().split(' '))

script_type = os.environ['script_type']
target_ip = os.environ['ifconfig_pool_remote_ip']
target_hostname = os.environ['common_name']

with open('dnsmasq/hosts', 'w') as hosts:
    for ip, hostname in current_hosts:
        if ip == target_ip or hostname == target_hostname:
            continue

        hosts.write('{} {}\n'.format(ip, hostname))

    if script_type == 'client-connect':
        hosts.write('{} {}\n'.format(target_ip, target_hostname))
