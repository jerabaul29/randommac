"""spoof an existing connection"""

# add the module from adjacent folder if not installed on the whole system
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/../randommac/")

# import the interface module
import randommac_interface as randommac

# show all known connections
out = randommac.nmcli_show_connections()

# spoof address on a connection
name_connection = ['AIRPORT'] # any connection NAME returned by nmcli_show_connections
                              # use a list as could change on several addresses at once
out = randommac.change_MAC_network(name_connection)
