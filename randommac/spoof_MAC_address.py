# do the command line interaction for setting a new MAC with the network manager through nmcli
from execute_bash_command import *
from extract_information_from_nmcli import *
from generate_random_MAC import *


class ExceptionNoWifi(Exception):
    pass

# structure of the command to enter / save a cloned mac address using nmcli ----
# example:   nmcli connection modify Get-1b7f62 802-11-wireless.cloned-mac-address 11:22:33:44:55:66
# structure: nmcli connection modify name       type           .cloned-mac-address cloned_addresss

################################################################################
# modify the MAC address of an already existing network
def spoof_MAC_address(network_name,network_type,MAC_address, PRINT=False,DEBUG=False):
    """spoof MAC address corresponding to network name on interface type"""

    if PRINT:
        print "*********************************************************************"
        print "spoofing on network name: " + network_name
        print "MAC addresses before: -----------------------------------------------"
        show_MAC_address_connection(network_name,True)
        print "---------------------------------------------------------------------"

    # command to issue
    command_spoof = "nmcli connection modify " + network_name + " " + network_type + ".cloned-mac-address " + MAC_address

    # execute
    command_output = subprocess_cmd(command_spoof,DEBUG)

    if PRINT:
        print "MAC addresses after: ------------------------------------------------"
        show_MAC_address_connection(network_name,True)
        print "---------------------------------------------------------------------"
        print "*********************************************************************"

    return command_output

################################################################################
