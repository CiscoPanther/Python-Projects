#!/usr/bin/env python
from __future__ import absolute_import, division, print_function
import sqlite3
import sys
import json
import netmiko
import mytools

# Connection to the database and creation of tables
def create_db_tables():
    conn = sqlite3.connect("production_vlan.db")
    c = conn.cursor()
    table_1 = "CREATE TABLE if not exists my_vlans (id INTEGER,name TEXT,description TEXT);"
    table_2 = "CREATE TABLE if not exists users (username TEXT,password TEXT);"
    c.execute(table_1)
    c.execute(table_2)
    conn.commit()

# SSH into the devices using the netmiko library.
def ssh_connection():
    netmiko_exceptions = (netmiko.ssh_exception.NetMikoTimeoutException,
                        netmiko.ssh_exception.NetMikoAuthenticationException)

    with open(devices.json) as dev_file:
        devices = json.load(dev_file)

    username, password = mytools.get_credential()
    query = "SELECT * FROM users WHERE username='username' AND password='password';"
    c.execute(query)
    result = c.fetchone()
    if (result):
        for device in devices:
            try:
                print('-'*79)
                print('Connecting to the device', device['ip'])
                connection = netmiko.ConnectHandler(**device)
                time.sleep(2)
            except netmiko_exceptions as e:
                print("Failed to connect to ", device['hostname'], e)
    else:
        print("User not found")


# This module gives the user like friendly interface to navigate through the tool.
def user_interface():
    print("***********************Welcome***********************************\n")
    print("[1]: Add new user\n\n")
    print("[2]: Create VLAN\n\n")
    print("[3]: Delete VLAN\n\n")
    print("[4]: Quit\n\n")

    selection = input("Please enter the number that matches the operation you want to perform today: ")
    if selection == "1":
        add_user()
    elif selection == "2":
        create_vlan()
    elif selection == "3":
        del_vlan()
    elif selection == "4":
        quit()
    else:
        print("Invalid Entry!! Please enter a valid selection ")
        sys.exit()

# This module adds a new user to the users table
def add_user():
    conn = sqlite3.connect("production_vlan.db")
    c = conn.cursor()
    new_user = input("Enter your username: ")
    new_password = input("Enter the new password:")
    query = "INSERT INTO users VALUES ('new_user', 'new_password');"
    c.execute(query)
    print("New user created!!")
    conn.commit()
    conn.close()
    response()

# User Authentication
def login():
    conn = sqlite3.connect("production_vlan.db")
    c = conn.cursor()
    username, password = mytools.get_credential()
    query = "SELECT * FROM users WHERE username='username' AND password='password';"
    c.execute(query)
    result = c.fetchall()
    if (result):
        print("Welcome Back")
        user_interface()
    else:
        print("Failed Login")

#backup_admin_authentication for testing
def my_login():
    username, password = mytools.get_credential()
    if username == "Ernest" and password == "cisco":
        user_interface()
    else:
        print("Login failed")

# This module creates the vlan on the router and updates the vlan table as well.
def create_vlan():
    global id, name, desc
    id = input("Please enter vlan ID: ")
    name = input("Please enter vlan name: ")
    desc = input("Please enter vlan description: ")
    update_vlan_table()
    response()

# VLAN table update
def update_vlan_table():
    conn = sqlite3.connect("production_vlan.db")
    c = conn.cursor()
    query = "INSERT INTO my_vlans VALUES ('id','name','description');"
    print("Creating VLAN")
    try:
        verify_vlan()
        c.execute(query, data)
        conn.commit()
        conn.close()
        ssh_conn()
        connection.send_command("enable")
        connection.send_command("conf t")
        connection.send_command("vlan ", id)
        connection.send_command("vlan ", name)
        connection.send_command("vlan ", desc)
    except:
        "Vlan already exists"

# This module deletes a VLAN from the device and the vlan table as well.
def del_vlan():
    conn = sqlite3.connect("production_vlan.db")
    c = conn.cursor()
    id = input("Please enter the ID of he VLAN you wish to delete: ")
    delete_query = "DELETE FROM vlans where id = 'id';"
    try:
        c.execute(delete_query)
        conn.commit()
        conn.close()
        ssh_conn()
        connection.send_command("enable")
        connection.send_command("conf t")
        connection.send_command("no vlan ", id)
        print("Vlan deleted")
        response()
    except:
        print("Vlan does not exist")

# Checks for VLAN duplication or overwriting
def verify_vlan():
    for vlan in vlans:
        for new_vlan in vlan:
            query = ("SELECT * FROM vlans;")
            c.execute(query)
            if new_vlan == vlan:
                print("Vlan already exists")
                break
            else:
                print("VLAN database is being updated")

# Gracefully exits from the program
def quit():
    sys.exit()

# Asks the user what else the user would like to explore before exiting the program.
def response():
    response = input("Do you want to perform another operation? [Yes or No] ")

    if response == "Yes" or "YES":
        user_interface()
    elif response == "No" or "NO":
        sys.exit()
