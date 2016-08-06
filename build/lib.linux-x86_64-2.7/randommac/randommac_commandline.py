#some command line interface for randommac

import argparse
from randommac_interface import *

def main():
    """the function to be called from terminal"""

    parser = argparse.ArgumentParser()

    # optional argument for launching interactive interface ------------------------
    parser.add_argument("-i","--interactive", help="launch the interactive randommac",
                        action="store_true")

    # optional argument for outputting nmcli information ---------------------------
    parser.add_argument("-n","--nmcliinfo", help="output information from nmcli",
                        action="store_true")

    # optional argument for showing information about one saved network ------------
    parser.add_argument("-d","--details", type=str, help="show details of one saved network, DETAILS is network NAME for which to show details, from nmcli")

    # optional argument to ask for a random MAC address ----------------------------
    parser.add_argument("-r","--randomaddress", help="output a random MAC address",
                        action="store_true")

    # optional argument to spoof a network -----------------------------------------
    parser.add_argument("-s","--spoof", type=str, help="spoof a saved network, SPOOF is network NAME to spoof from nmcli")

    # optional argument to connect and spoof to a new network ----------------------
    parser.add_argument("-c","--connectspoof", type=str, help="connect and spoof to a wifi network, CONNECTSPOOF is wifi network NAME to connect and spoof from nmcli")
    # additional optional argument for giving also a password
    parser.add_argument("-p","--password", type=str, help="password to connect and spoof to a wifi network, PASSWORD is the password to use on the network described by --connectspoof")


    args = parser.parse_args()

    if args.interactive:
       print "Launch interactive interface"
       interactive_interface()

    elif args.nmcliinfo:
        print "Output nmcli information"
        print "---------------------------------------------------------------------"
        print "Summary saved networks:"
        nmcli_show_connections()
        print "---------------------------------------------------------------------"
        print "All available Wifi networks:"
        nmcli_available_wifi()

    elif args.details:
        out = show_MAC_address_connection(args.details,DEBUG=True)

    elif args.randomaddress:
        address = generate_random_MAC(DEBUG=False)
        print address

    elif args.spoof:
        out = change_MAC_network([args.spoof])

    elif args.connectspoof:
        if args.password:
            # connect with a password
            add_new_wifi_spoofed_connection(args.connectspoof,connection_password=args.password)
        else:
            # connect without password
            add_new_wifi_spoofed_connection(args.connectspoof)

    else:
        print "Randommac, python wrappers on nmcli for easy MAC spoofing. Try -h for help."
