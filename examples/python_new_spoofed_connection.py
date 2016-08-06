"""create a new spoofed connection entry in NetworkManager"""

# add the module from adjacent folder if not installed on the whole system
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/../randommac/")

# import the interface module
import randommac_interface as randommac

randommac.add_new_wifi_spoofed_connection('AIRPORTOPEN') # add a wifi connection without WPA password
randommac.add_new_wifi_spoofed_connection('AIRPORT',connection_password="bla450FFg542FF") # add a wifi connection with WPA password
