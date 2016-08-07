
# provide a simple interface to randommac, both as python functions and command line interface
from generate_random_MAC import *
from spoof_MAC_address import *
from extract_information_from_nmcli import *
from execute_bash_command import *
import time
import random

################################################################################
# NOTE:
################################################################################

# ------------------------------------------------------------------------------
# PYTHON INTERFACE -------------------------------------------------------------
# ------------------------------------------------------------------------------

# display a brand new random spoofed MAC address
def display_random_MAC():
    """display and return a random MAC address"""
    random_MAC = generate_random_MAC()
    print random_MAC
    return random_MAC

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

# change MAC address randomly, on all saved networks ---------------------------
def change_MAC_all_saved_networks(except_networks_list=[],PRINT=True):
    """change for random MAC address for all saved networks except those in except
    Each network gets a different MAC address"""

    # deactivate all connections
    subprocess_cmd("nmcli networking off")

    # display / generate informatio from nmcli
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

    # reactivate all connections
    subprocess_cmd("nmcli networking on")

# change MAC address randomly, on all saved networks, same MAC on each ---------
# physical interface
def change_MAC_all_saved_networks_uniform_over_device(except_networks_list=[],PRINT=True):
    """change for random MAC for all saved networks except those in except
    All networks on the same device get the same MAC address"""

    # deactivate all connections
    subprocess_cmd("nmcli networking off")

    # display / generate informatio from nmcli
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

    # deactivate all connections
    subprocess_cmd("nmcli networking on")

# change MAC address randomly, on a list of saved networks ---------------------
def change_MAC_network(network_name_list,PRINT=True):
    """change the MAC address for the network name list
    each network name gets a different MAC address"""

    # deactivate all connections
    subprocess_cmd("nmcli networking off")

    # display / generate informatio from nmcli
    network_names = nmcli_saved_connections()
    network_types = nmcli_types()

    # set / change the cloned MAC address on all the connections in network_name_list
    for connection_number, network_name in enumerate(network_names):
        if network_name in network_name_list:
            network_type = network_types[connection_number]
            random_MAC = generate_random_MAC()
            spoof_MAC_address(network_name,network_type,random_MAC,PRINT=PRINT)

    # deactivate all connections
    subprocess_cmd("nmcli networking on")

# change MAC address randomly, on all saved network for one physical -----------
# interface
def change_MAC_interface(interface_name_list,PRINT=True):
    """change the MAC address for the interface name list
    each network gets a different MAC addresss"""

    # deactivate all connections
    subprocess_cmd("nmcli networking off")

    # display / generate informatio from nmcli
    network_names = nmcli_saved_connections()
    network_types = nmcli_types()

    # set / change the cloned MAC address on all the connections in network_name_list
    for connection_number, network_type in enumerate(network_types):
        if network_type in interface_name_list:
            network_name = network_names[connection_number]
            random_MAC = generate_random_MAC()
            spoof_MAC_address(network_name,network_type,random_MAC,PRINT=PRINT)

    # deactivate all connections
    subprocess_cmd("nmcli networking off")

# periodically perform one of the random MAC changes functions -----------------
def periodically_perform_command(time_step,command):
    """periodically perform command, waiting (sleep) time_step between calls
    this is Ok as long as drift is ok in update"""

    eval(command)
    time.sleep(time_step)

# perform at random time one of the random MAC changes functions ---------------
def randomly_perform_command(min_time,max_time,command):
    """performs at random time, uniform in [min_time,max_time], the command"""

    eval(command)
    time.sleep(random.uniform(min_time,max_time))

# a step by step interface to help users
def interactive_interface():
    """a step by step interface to help the user"""

    string_welcome = """\
###########################################################
########## Welcome to step-by-step PyMacChanger ###########
###########################################################
    """
    print string_welcome

    print "---------------------------------------------------------------------"
    print "Summary saved networks:"
    nmcli_show_connections()

    print "---------------------------------------------------------------------"
    print "All available Wifi networks:"
    nmcli_available_wifi()

    print "---------------------------------------------------------------------"
    string_summary_functions = """\
    Summary of some of the available functionalities:
- [0] create spoofed connection on a new WiFi network
- [1] spoof existing connection
- [2] spoof all existing connections on an interface
- [3] start periodic spoofing
- [4] start random time spoofing
- [q] exit interactive interface
    """
    print string_summary_functions
    print "---------------------------------------------------------------------"

    continue_interactive = True

    while continue_interactive:

        function = raw_input("Choose functionality [0-4] or [q]: ")

        string_summary_spoofed_new_wifi = """\
    Create a spoofed connection on a new Wifi network
The aim is to never display your true MAC
See example: pyton_new_spoofed_connection.py
Main function to use: add_new_wifi_spoofed_connection()
Command line interface example:
    """

        string_summary_spoof_existing = """\
    Spoof an existing connection on any interface
The aim is to spoof (or modify spoofing) of an existing connection
See example: python_spoof_existing_connection.py
Main function to use: change_MAC_network()
Command line interface example:
        """

        if function == 'q':
            continue_interactive = False

        elif function == '0':
            print "---------------------------------------------------------------------"
            print string_summary_spoofed_new_wifi
            test = raw_input("Test function [y/n]: ")
            if test == 'y':
                network = raw_input("Enter new network name to spoof: ")
                password = raw_input("Enter WPA / WPA2 password (empty string for none): ")
                add_new_wifi_spoofed_connection(network,password)
            print "---------------------------------------------------------------------"

        elif function == '1':
            print "---------------------------------------------------------------------"
            print string_summary_spoof_existing
            test = raw_input("Test function [y/n]: ")
            if test == 'y':
                name_connection = raw_input("Enter name of existing connection to spoof: ")
                out = change_MAC_network([name_connection])
            print "---------------------------------------------------------------------"

        else:
            print "---------------------------------------------------------------------"
            print "Sorry, this is either invalid or not implemented yet."
            print "---------------------------------------------------------------------"
