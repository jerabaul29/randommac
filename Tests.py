from randommac.generate_random_MAC import *
from randommac.spoof_MAC_address import *
from randommac.extract_information_from_nmcli import *
from randommac.randommac_interface import *

# change_MAC_all_saved_networks(except_networks_list="Get-1b7f62")
# change_MAC_all_saved_networks_uniform_over_device()

nmcli_device_wifi()

add_new_wifi_spoofed_connection('Dobbeltagentan',connection_password="bla450FFg542FF")
