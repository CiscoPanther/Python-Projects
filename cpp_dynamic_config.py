#!/usr/bin/env python
from __future__ import absolute_import,  division, print_function
from ConnectHandler import netmiko
import json
from getpass import getpass
import sys
import signal
import os
form pprint import pprint as pp

signal.signal(signal.SIGPIPE, signal.SIG_DFL)     # IOError: Broken pipe |
signal.signal(signal.SIGINT, signal.SIG_DFL)      # KeyBoardInterrupt CTRL+C

def get_input(prompt = ''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

def get_credentials():.;
    username = get_input('Enter username: ')
    password = None
    while not password:
        password = getpass()
        password_verify = getpass('Retype your password: ')
        if password != password_verify:
            print('password do not match, try again..')
            password = None
    return username, password


# This function gives interfaces a description with the connected device hostname and port connected to..

def get_config_from_cdp_neighbors(input_string):
    lines = input_string.splitlines()[5:]   # Removes the output header leaving just the interfaces details
    hostname = None
    config = []
    for line in lines:
        words = line.split()
        if hostname is None:
            hostname = words.pop(0).split('.')[0]
        if len(words) > 0:
            local = ''.join(words[0:2])   #Joining the interface def eth0/0
            remote = ''.join(words[-2:])
            description = '_'.join((hostname, remote))
            config.append('interface ' + local)
            config.append('description ' + description)
            config.append('!')   # totally optional
            hostname = None
    return config

if len(sys.arg) < 2:
    print('Usage:', sys.argv[0].split('/')[-1], 'devices.json')
    exit()

change_number = get_input('Please enter an approved change number: ')

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)

username, password = get_credentials()

with open(sys.argv[1]) as dev_file:   # This opens the JSON file
    devices = json.load(dev_file)

results = {'Successful': [], 'Failed': []}

for device in devices:               # This loads the username and password into every device opened.
    #device['username'] = username
    #device['password'] = password
    try:
        print('~'*79)
        print("Connecting to device " + device["ip"] + " now...")
        connection = netmiko.ConnectHandler(**device)
        connection.send_command('Send log "Starting change {}"'.format(change_number))
        output = connection.send_command('show cdp neighbors')
        config = get_config_from_cdp_neighbors(output)
        print('\n'.join(config))
        connection.send_config_set(config)
        connection.send_command('copy run start')
        connection.send_command('Send log "Completing change {}"'.format(change_number))
        connection.disconnect()
        results['Successful'].append(device["ip"])
    except netmiko_exceptions as e:
        print("Authentication into " + device["ip"] + " failed.\nThe error is " + e)
        results['Failed to'].append(': '.join((device["ip"], str(e))))

print(json.dumps(results, indent=2))   # Write the successful and failed log to a json file
with open('resullts-' + change_number + '.json', 'w') as results_file:
    json.dump(results, results_file, indent=2)




# This function gives interfaces a description with the connected device hostname and port connected to..

def get_config_from_cdp_neighbors(input_string):
    lines = input_string.splitlines()[5:]   # Removes the output header leaving just the interfaces details
    hostname = None
    config = []
    for line in lines:
        words = line.split()
        if hostname is None:
            hostname = words.pop(0).split('.')[0]
        if len(words) > 0:
            local = ''.join(words[0:2])   #Joining the interface def eth0/0
            remote = ''.join(words[-2:])
            description = '_'.join((hostname, remote))
            config.append('interface ' + local)
            config.append('description ' + description)
            config.append('!')   # totally optional
            hostname = None
    return config


# The below function sends a command to a device to remove all interface description

s1 = {
        "username": 'ernest',
        "password": "cisco",
        "device_type": "cisco_ios",
        "ip": "10.0.0.11"
}
connection = netmiko.ConnectHandler(**s1)
interfaces = connection.send_command('show run | i ^interface').splitlines()

# This function gives interfaces a description with the connected device hostname and port connected to..
def get_config_from_cdp_neighbors(input_string):
    lines = input_string.splitlines()[5:]   # Removes the output header leaving just the interfaces details
    hostname = None
    config = []
    for line in lines:
        words = line.split()
        if hostname is None:
            hostname = words.pop(0).split('.')[0]
        if len(words) > 0:
            local = ''.join(words[0:2])   #Joining the interface def eth0/0
            remote = ''.join(words[-2:])
            description = '_'.join((hostname, remote))
            config.append('interface ' + local)
            config.append('description ' + description)
            config.append('!')   # totally optional
            hostname = None
    return config

# The below function sends a command to a device to remove all interface description
def reset_interface_descriptions(connection):
    config = []
    for interface in interfaces:
        config.append(interface)
        config.append(' no description')
        config.append('!')
    print('\n'.join(config))
    connection.send_config_set(config)
