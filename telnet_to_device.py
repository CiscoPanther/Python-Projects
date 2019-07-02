import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

with open('my_switches.txt') as f:   # opening the IP address file
    for IP in f:
        IP = IP.strip()
        print("Configuring Switch " + (ip))

        HOST = IP
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
        tn.write(b"enable\n")
        tn.write(b"cisco\n")  # enable password
        tn.write(b"conf t\n")

        for n in range(2, 10):
            tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
            tn.write(b"name Python_vlan_" + str(n).encode('ascii') + b"\n")

        tn.write(b"end\n")
        tn.write(b"wr\n")
        tn.write(b"exit\n")
        print(tn.read_all().decode('ascii'))

# The below scripts backs uo the running config of devices and saves to a file.
import getpass
import telnetlib

user = input("Enter your telnet username: ")
password = getpass.getpass()

with open('my_switches.txt') as f:   # opening the IP address file
    for IP in f:
        IP = IP.strip()
        print("Getting running config from the switch " + (ip))

        HOST = IP
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"Username: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
        tn.write(b"enable\n")
        tn.write(b"cisco\n")  # enable password
        tn.write(b"terminal length 0\n")  # This line makes the switch to show the whole running config in one file without the user  pressing spacebar
        tn.write(b"show run\n")
        tn.write(b"exit\n")

        readoutput = tn.read_all()
        saveoutput = open('switch' + HOST, 'w')
        saveoutput.write(readoutput.decode('ascii'))
        saveoutput.write("\n")
        saveoutput.close()





