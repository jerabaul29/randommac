"""generate a valid MAC address"""

# add the module from adjacent folder if not installed on the whole system
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/../randommac/")

# import the interface module
import randommac_interface as randommac

address = randommac.generate_random_MAC(DEBUG=False)

print "Complete random MAC: " + address
