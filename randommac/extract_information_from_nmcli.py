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
        print command_output

    return(command_output)

def nmcli_saved_connections(DEBUG=False):
    """returns the name of the saved connections as a Python list"""

    command_output = subprocess_cmd(bash_list_saved_connections)
    result = parse_output_bash(command_output,DEBUG=DEBUG)

    return result

def nmcli_types(DEBUG=False):
    """return the connection types as a Python list, corresponding to each connection"""

    command_output = subprocess_cmd(bash_list_saved_connection_types)
    result = parse_output_bash(command_output,DEBUG=DEBUG)

    return result
