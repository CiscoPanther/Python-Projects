#!/usr/bin/env python
from __future__ import absolute_import, division, print_function
import sqlite3
import sys
import json
import netmiko
import mytools
from vlan_modules import *


# This module connects to the database and creates a table if doesn't already exist.
try:
    create_db_tables()
    # The login in screen to begin operating the tool
    my_login()
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()
