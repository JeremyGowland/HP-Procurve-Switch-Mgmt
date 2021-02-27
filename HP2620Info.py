# Created 27/02/2021
# Python Script Using Netmiko to run commands on HP Procurve Switches
# See doco on the website http://ktbyers.github.io/netmiko/
# Tested on HP2620 PoE 24 Port Switch
# 
# Imports Netmiko Python Module
import netmiko

# Connects to the HP Procurve Switches IP Address, Device Type sets the manufacturer you are connecting to.
# Or type dir (netmiko)
# This connection is to a new switch with no config hence no username or password
connection = netmiko.ConnectHandler(ip="192.168.1.160", device_type="hp_procurve")

# This line executes the commands as if at the CLI, the formatting of the output is formated using the print command to make it readbale
print (connection.send_command("sh system"))

# It is good practice in Python/Netmiko to disconnect from the device.
connection.disconnect()
