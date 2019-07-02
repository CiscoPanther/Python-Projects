#!/usr/bin/env python
from __future__ import absolute_import,  division, print_function
from ConnectHandler import netmiko
import json
from getpass import getpass
import sys
import signal
import os

signal.signal(signal.SIGPIPE, signal.SIG_DFL)     # IOError: Broken pipe |
signal.signal(signal.SIGINT, signal.SIG_DFL)      # KeyBoardInterrupt CTRL+C

def get_input(prompt = ''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

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

username, password = get_credentials()

if len(sys.arg) < 3:
    print('Usage python_script_name.py commands.txt devices_auth_file.json')
    exit()

netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                      netmiko.ssh_exception.NetMikoAuthenticationException)


with open(sys.argv[1]) as cmd_file:  # This opens the command file
    commands = cmd_file.readlines()

with open(sys.argv[2]) as dev_file:   # This opens the JSON file
    devices = json.load(dev_file)

for device in devices:               # This loads the username and password into every device opened.
    device['username'] = username
    device['password'] = password
    try:
        print('~'*79)
        print("Connecting to device " + device["ip"] + " now...")
        connection = netmiko.ConnectHandler(**device)
        newdir = connection.base_prompt
        os.mkdir(newdir)
        for command in commands:
            filename = command.replace(' ', '-') + '.txt'
            filename = '/'.join((newdir, filename))
            with open(filename, 'w') as out_file:
                out_file.write(connection.send_command(command) + '\n')
        connection.disconnect()
    except netmiko_exceptions as e:
        print("Authentication into " + device["ip"] + " failed.\nThe error is " + e)

