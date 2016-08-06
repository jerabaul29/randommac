# extract information from nmcli through bash calls
from execute_bash_command import *

# list of commands -------------------------------------------------------------

# command line to print the name of the saved connections:
# print connections     | first work is name | not first line (label)
# nmcli connection show | awk '{print $1}'   | tail -n +2
bash_list_saved_connections = "nmcli connection show | awk '{print $1}'   | tail -n +2"

# command line to print the name of the connection types
# print connections     | third work is type | not first line (label)
# nmcli connection show | awk '{print $3}'   | tail -n +2
bash_list_saved_connection_types = "nmcli connection show | awk '{print $3}'   | tail -n +2"

# command line to print the list of physical devices
# print status devices  | first is device name | nor first line (label)
bash_list_physical_devices = "nmcli dev status | awk '{print $1}'   | tail -n +2"

# command line to print the list of connection types
# print status devices  | second is type | nor first line (label)
bash_list_physical_devices_type = "nmcli dev status | awk '{print $2}'   | tail -n +2"

# print the MAC address through nmcli
# nmcli connection show Get-1b7f62 | grep mac | head -n 2

def parse_output_bash(network_names,DEBUG=False):
    """turn the string of bash network outputs into a list of python name strings"""
    list_network_words = []
    current_word = []

    if DEBUG:
        print "Into parser: "
        print network_names

    for current_char in network_names:
        if current_char == '\n':
            list_network_words.append(''.join(current_word))
            current_word = []
        else:
            current_word.append(current_char)

    # do not forget the last one!
    list_network_words.append(''.join(current_word))

    if DEBUG:
        print "Out of parser: "
        print list_network_words

    return list_network_words

def index_all_occurences(list_values,occurence):
    """returns the list of indexes at which occurence appears in list_values
    work like .index() except that return a list of all occurences"""

    list_occurences_index = [i for i, j in enumerate(list_values) if j == occurence]
    return list_occurences_index

def nmcli_show_connections():
    """a wrapper around nmcli connection show"""

    command_output = subprocess_cmd("nmcli connection show")
    print command_output
    return command_output

def show_MAC_address_connection(connection, DEBUG=False):
    """return information about MAC and cloned MAC address"""

    command = "nmcli connection show " + connection + " | grep mac | head -n 2"
    command_output = subprocess_cmd(command)

    if DEBUG:
        print "MAC address information about connection: " + connection
        print command_output

    return(command_output)

def nmcli_saved_connections(DEBUG=False):
    """returns the name of the saved connections as a Python list"""

    command_output = subprocess_cmd(bash_list_saved_connections)
    result = parse_output_bash(command_output,DEBUG=DEBUG)

    return result

def nmcli_types(DEBUG=False):
    """return the connection types as a Python list, corresponding to each connection saved"""

    command_output = subprocess_cmd(bash_list_saved_connection_types)
    result = parse_output_bash(command_output,DEBUG=DEBUG)

    return result

def nmcli_device_wifi(DEBUG=False):
    """returns name of physical devices giving wifi access"""

    command_list_devices = subprocess_cmd(bash_list_physical_devices)
    list_devices = parse_output_bash(command_list_devices,DEBUG=DEBUG)

    command_list_devices_types = subprocess_cmd(bash_list_physical_devices_type)
    list_devices_type = parse_output_bash(command_list_devices_types,DEBUG=DEBUG)

    # find the one that have type wifi
    list_index_wifi = index_all_occurences(list_devices_type,"wifi")

    # return the corresponding devices
    return [list_devices[i] for i in list_index_wifi]

def nmcli_available_wifi(print_out=True):
    """print details about available Wifi networks"""

    output = subprocess_cmd("nmcli dev wifi list")

    if print_out:
        print output
