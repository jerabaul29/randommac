"""inspect all connections"""

# add the module from adjacent folder if not installed on the whole system
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/../randommac/")

# import the interface module
import randommac_interface as randommac

randommac.nmcli_show_connections()

# display details about MAC address on one specific connection
name_connection = 'AIRPORT' # any connection NAME returned by nmcli_show_connections
out = randommac.show_MAC_address_connection(name_connection,DEBUG=True)
