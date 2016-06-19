from randommac.generate_random_MAC import *
from randommac.spoof_MAC_address import *
from randommac.extract_information_from_nmcli import *

# generate a random MAC address
random_MAC = generate_random_MAC()

# display / generate informatio from nmcli
nmcli_show_connections()
network_names = nmcli_saved_connections()
network_types = nmcli_types()

# set / change the cloned MAC address on one of the connections
connection_number = 0
spoof_MAC_address(network_names[connection_number],network_types[connection_number],random_MAC,PRINT=True)
