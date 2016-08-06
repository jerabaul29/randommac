
# provide a simple interface to randommac, both as python functions and command line interface
from generate_random_MAC import *
from spoof_MAC_address import *
from extract_information_from_nmcli import *

################################################################################
# NOTE:
# should do something to avoid displaying mac address when connecting to a network for the first time!!
################################################################################

# ------------------------------------------------------------------------------
# PYTHON INTERFACE -------------------------------------------------------------
# ------------------------------------------------------------------------------

class ExceptionNoWifi(Exception):
    pass

# display a brand new random spoofed MAC address


# set Network Manager parameters to ensure max safety --------------------------
# disable auto logging

# change MAC address randomly, on all saved networks ---------------------------
def change_MAC_all_saved_networks(except_networks_list=[],PRINT=True):
    """change for random MAC address for all saved networks except those in except
    Each network gets a different MAC address"""

    # display / generate informatio from nmcli
    nmcli_show_connections()
    network_names = nmcli_saved_connections()
    network_types = nmcli_types()

    # set / change the cloned MAC address on all the connections
    for connection_number, network_name in enumerate(network_names):
        if network_name in except_networks_list:
            pass
        else:
            network_type = network_types[connection_number]
            random_MAC = generate_random_MAC()
            spoof_MAC_address(network_name,network_type,random_MAC,PRINT=PRINT)

# change MAC address randomly, on all saved networks, same MAC on each ---------
# physical interface
def change_MAC_all_saved_networks_uniform_over_device(except_networks_list=[],PRINT=True):
    """change for random MAC for all saved networks except those in except
    All networks on the same device get the same MAC address"""

    # display / generate informatio from nmcli
    nmcli_show_connections()
    network_names = nmcli_saved_connections()
    network_types = nmcli_types()

    # list of devices already met
    list_devices_met = []
    # list of MAC addresses corresponding to each device
    list_devices_met_addresses = []

    # set / change the cloned MAC address on all the connections
    for connection_number, network_name in enumerate(network_names):
        network_type = network_types[connection_number]

        if network_name in except_networks_list:
            pass

        else:
            if not network_type in list_devices_met_addresses:
                # create a new address for this type of network
                random_MAC = generate_random_MAC()
                list_devices_met.append(network_type)
                list_devices_met_addresses.append(random_MAC)

            # put the right cloned MAC address
            current_MAC_index = list_devices_met.index(network_type)
            current_MAC = list_devices_met_addresses[current_MAC_index]
            spoof_MAC_address(network_name,network_type,current_MAC,PRINT=PRINT)

# change MAC address randomly, on a list of saved networks ---------------------
def change_MAC_network(network_name_list):
    """change the MAC address for the network name list
    each network name gets a different MAC address"""

    # display / generate informatio from nmcli
    nmcli_show_connections()
    network_names = nmcli_saved_connections()
    network_types = nmcli_types()

    # set / change the cloned MAC address on all the connections in network_name_list
    for connection_number, network_name in enumerate(network_names):
        if network_name in network_name_list:
            network_type = network_types[connection_number]
            random_MAC = generate_random_MAC()
            spoof_MAC_address(network_name,network_type,random_MAC,PRINT=PRINT)

# change MAC address randomly, on all saved network for one physical -----------
# interface

# periodically perform one of the random MAC changes functions -----------------

# perform at random time one of the random MAC changes functions ---------------

# ------------------------------------------------------------------------------
# COMMAND LINE WRAPPERS --------------------------------------------------------
# ------------------------------------------------------------------------------
