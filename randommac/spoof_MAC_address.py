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
# add a new network with random cloned mac address since beginning -------------
def add_new_wifi_spoofed_connection(connection_name,connection_password=""):
    """ add a new wifi connection that is spoofed since the beginning"""

    list_wifi_ifnames = nmcli_device_wifi()
    if len(list_wifi_ifnames) == 0:
        print "Found no Wifi device, abort"
        raise ExceptionNoWifi()
    elif len(list_wifi_ifnames) > 1:
        print "Found more than one Wifi device: "
        print list_wifi_ifnames
        ifname_connection = raw_input("Enter name of device to use: ")
    else:
        ifname_connection = list_wifi_ifnames[0]

    # generate a random MAC address
    random_mac = generate_random_MAC()

    # add the connection
    command_add_connection = "nmcli con add con-name " + connection_name + " ifname " + ifname_connection + " type wifi ssid " + connection_name + " cloned-mac " + random_mac

    print "Command create new network: "
    print command_add_connection
    output = subprocess_cmd(command_add_connection)
    print output

    if connection_password:
        # add password
        print "Add password type WPA2"
        command = "nmcli con modify " + connection_name + " wifi-sec.key-mgmt wpa-psk"
        output = subprocess_cmd(command)
        print command
        command = "nmcli con modify " + connection_name + " wifi-sec.psk " + connection_password
        output = subprocess_cmd(command)
        print command
