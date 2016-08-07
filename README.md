# randommac

A MAC changer for Linux when Network Manager is monitoring connections.

## macchanger and the NetworkManager problem

As I searched the Internet for MAC spoofing solutions, it appeared that the main tool available for Linux (*macchanger*) breaks when *NetworkManager* is used for monitoring of the connections, which is the default on for example Ubuntu 16.04 LTS. I do not want to disable *NetworkManager* so I needed to find a way to do spoofing on Linux with it.

*NetworkManager* can be controlled from command line through its utility *nmcli*. *nmcli* supports MAC spoofing through the *cloned-mac-address* option. Therefore, I wrote a few Python wrappers to help me use nmcli for performing flexible MAC spoofing.

## randommac code structure

- **/randommac/** contains the python code and an *OUI.list* file that is used for generating valid random MAC addresses with valid manufacturer ID. Interaction with the code should rely on functions from *randommac_interface.py* for use as a Python module, or *randommac_commandline.py* for use as a command line tool.
- **/examples/** contains examples of how to use as a Python module. You can start by testing the random MAC number generation (*python_compute_random_MAC.py*), then create new dummy spoofed connections (*python_new_spoofed_connection.py*), inspect it (*python_inspect_connection.py*) and spoof it again (*python_spoof_existing_connection.py*). You can also have a look at the interactive interface (*python_interactive_interface.py*). All those functionalities are also available directly from the command line tool when installed by pip (see **installation**), so on a daily usage you should not need to call the python modules.

## installation

- either clone the repository and directly execute the python code
- or more simply for using the functionalities as Python module or command line: *$ pip install randommac*

## quick start

For a quick step-by-step demonstration of the module, try the interactive interface.
- either launch by executing *examples/python_interactive_interface.py*
- or execute in terminal after pip install by: *$ randommac -i*

## command line tool examples

- After having installed by pip, you will get access to the command line tools:

`
~$ randommac -h
usage: randommac [-h] [-i] [-n] [-d DETAILS] [-r] [-s SPOOF] [-c CONNECTSPOOF]
                 [-p PASSWORD]

optional arguments:
  -h, --help            show this help message and exit
  -i, --interactive     launch the interactive randommac
  -n, --nmcliinfo       output information from nmcli
  -d DETAILS, --details DETAILS
                        show details of one saved network, DETAILS is network
                        NAME for which to show details, from nmcli
  -r, --randomaddress   output a random MAC address
  -s SPOOF, --spoof SPOOF
                        spoof a saved network, SPOOF is network NAME to spoof
                        from nmcli
  -c CONNECTSPOOF, --connectspoof CONNECTSPOOF
                        connect and spoof to a wifi network, CONNECTSPOOF is
                        wifi network NAME to connect and spoof from nmcli
  -p PASSWORD, --password PASSWORD
                        password to connect and spoof to a wifi network,
                        PASSWORD is the password to use on the network
                        described by --connectspoof
`

- For getting info from nmcli:

`
~$ randommac -i
`

- For spoofing connection CONN, that already exists:

`
~$ randommac -s CONN
`

- For creating a new connection on an unknown network NETW, obtained from example from the nmcli info command, that will be spoofed since the beginning:

`
~$ randommac -c NETW
`

## To do

This is a work in progress. Please report any bug / feature request.

- interactive interface: some missing functions
- command line interface: some missing functions
- add periodic automatic spoofing
- documentation
- website post
