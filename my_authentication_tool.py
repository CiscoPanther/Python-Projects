#!/usr/bin/env python
from __future__ import absolute_import, division, print_function
from getpass import getpass

# Prompts users for input, included for python 2 support
def get_input(prompt=''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line

def get_credential():
    # Prompts for, and returns, a username & password
    username = get_input("Please enter your username: ")
    password = None
    while not password:
        #getpass makes the password entry invinsible
        password = getpass()
        password_verify = getpass('Retype you password: ')
        if password != password_verify:
            print('Password did not match, try again!')
            password = None
    return username, password
