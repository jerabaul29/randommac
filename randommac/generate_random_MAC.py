# NOTE: some functions in random module are not suitable to cryptography
# to be cryptography safe, use random.SystemRandom that relies on /dev/urandom
import random
import os

def generate_random_MAC(DEBUG=False):
    """ generate a random MAC address representation as a string, with a valid vendor OUI
    A MAC number is 6 groups of hexadecimal digits ie 6 groups of octets ie 48 bits
    MAC numbers are usually displayed as oct1:oct2:oct3:oct4:oct4:oct6
    The first 3 octets are Organizationally Unique Identifier [OUI]
    To generate a plausible random MAC number, the OUI is extracted from an OUI list
    The OUI list used by default is the one of macchanger (see https://github.com/alobbs/macchanger/tree/master/data )
    """

    # random number generator safe for cryptography --------------------------------
    cryptogen = random.SystemRandom()

    # valid OUI --------------------------------------------------------------------
    # use OUI.list from macchanger

    # path to the data relative to the position of this file
    # file_valid_MAC = os.path.abspath(os.path.join(os.path.dirname(__file__), '/../data/OUI.list'))
    path_to_this_file = os.path.dirname(__file__)
    file_valid_MAC = path_to_this_file + '/OUI.list'

    if DEBUG:
        print file_valid_MAC

    # find number of lines
    number_of_lines = sum(1 for line in open(file_valid_MAC))
    if DEBUG:
        print number_of_lines

    # select one line randomly
    number_line_to_use = cryptogen.randrange(number_of_lines)
    if DEBUG:
        print number_line_to_use

    # extract the corresponding line
    with open(file_valid_MAC) as fp:
        for i, line in enumerate(fp):
            if i == (number_line_to_use-1):
                line_to_use = line
                break

    print "Using OUI: " + line_to_use[:-1]

    # extract the corresponding MAC address prefixe
    MAC_address_prefix = line_to_use[0:2]+":"+line_to_use[3:5]+":"+line_to_use[6:8]
    if DEBUG:
        print MAC_address_prefix

    # complete address -------------------------------------------------------------
    complete_random_realistic_MAC_address = MAC_address_prefix+":%02x:%02x:%02x" % (
            cryptogen.randrange(0, 255),
            cryptogen.randrange(0, 255),
            cryptogen.randrange(0, 255),
            )

    if DEBUG:
        print complete_random_realistic_MAC_address

    complete_random_realistic_MAC_address_uppercase = complete_random_realistic_MAC_address.upper()

    if DEBUG:
        print complete_random_realistic_MAC_address_uppercase

    return(complete_random_realistic_MAC_address_uppercase)
