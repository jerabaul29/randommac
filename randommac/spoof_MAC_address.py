# do the command line interaction with the network manager through nmcli
%reset -f
import subprocess

# NOTE: TO DO:
# take care of the sudo stuff

# command line to print the name of the saved connections:
# print connections     | first work is name | not first line (label)
# nmcli connection show | awk '{print $1}'   | tail -n +2
bash_list_saved_connections = "nmcli connection show | awk '{print $1}'   | tail -n +2"

# command line to print the name of the connection types
# print connections     | third work is type | not first line (label)
# nmcli connection show | awk '{print $3}'   | tail -n +2
bash_list_saved_connection_types = "nmcli connection show | awk '{print $3}'   | tail -n +2"

# structure of the command to enter / save a cloned mac address using nmcli
# example:   nmcli connection modify Get-1b7f62 802-11-wireless.cloned-mac-address 11:22:33:44:55:66
# structure: nmcli connection modify name       type           .cloned-mac-address cloned_addresss

def subprocess_cmd(command):
    """execute a bash command and return output"""
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    return(proc_stdout)

def parse_output_bash(network_names):
    """turn the string of bash network outputs into a list of python name strings"""
    list_network_names = []
    current_name = []

    for current_char in network_names:
        if current_char == '\n':
            list_network_names.append(''.join(current_name))
            current_name = []
        else:
            current_name.append(current_char)

    return list_network_names


bash_network_names = subprocess_cmd(bash_list_saved_connections)
list_network_names = parse_output_bash(bash_network_names)

print bash_network_names
print "------------------------"
print list_network_names[2]

bash_network_types = subprocess_cmd(bash_list_saved_connection_types)
list_network_types = parse_output_bash(bash_network_types)

print bash_network_types
print "------------------------"
print list_network_types[0]
