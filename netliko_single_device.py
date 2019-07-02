#!/usr/bin/env python
from __future__ import absolute_import,  division, print_function
import netmiko
import json
from getpass import getpass

def get_input(prompt = ''):
#Checks which python version is running and uses the appropriate command
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

def get_credentials():
#Prompts for, and returns, a username and password...'''
    username = get_input('Enter username: ')
    password = None
    while not password:
        password = getpass()
        password_verify = getpass('Retype your password: ')
        if password != password_verify:
            print('password do not match, try again..')
            password = None
    return username, password
username, password = get_credentials()

ip = '10.0.0.11'
device_type = 'cisco_ios'
username = username
password = password

print('~'*79)
print("Connecting to " + ip + " now...")
connection = netmiko.ConnectHandler(ip=ip, device_type=device_type, username=username, password=password)
output = connection.send_command('show run config')
with open(output + ".json", "w") as file:
    json.dump(file)

connection.disconnect()
