#!/usr/bin/env python
from __future__ import absolute_import,  division, print_function
from ConnectHandler import netmiko
import json
from getpass import getpass
import network_automation_tools

#Checks which python version is running and uses the appropriate command
def get_input(prompt = ''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

#Prompts for, and returns, a username and password...
def get_credentials():
    username = get_input('Enter username: ')
    password = None
    while not password:
        password = getpass()
        password_verify = getpass('Retype your password: ')
        if password != password_verify:
            print('password do not match, try again..')
            password = None
    return username, password
'''
Parses the username and password into the get_credentials function.
The network_automation_tools.get_credentials() is used if I have some functions
in another file, we can access the function with this code
'''
username, password = get_credentials()
with open('device_file.json') as dev_file:
    devices = json.load(dev_file)
#The below catches netmiko possible errors and stores them in a tuple
netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)
#Loops through the ip address in the opened file

for device in devices:
    device['username'] = username
    device['password'] = password
    try:
        print('~'*79)
        print("Connecting to "+ device["ip"] +" now...")
        connection = netmiko.ConnectHandler(**device)
        print(connection.send_command('The command goes in here....'))
        connection.disconnect()
    except netmiko_exceptions as e:
        print("Authentication into " + device["ip"] + " failed.\nThe error is "+ e)

