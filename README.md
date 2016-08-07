# randommac

A MAC changer for Linux when Network Manager is monitoring connections.

## The macchanger and NetworkManager problem

As I searched the Internet for MAC spoofing solutions, it appeared that the main tool available for Linux (*macchanger*) breaks when *NetworkManager* is used for monitoring of the connections, which is the default on for example Ubuntu 16.04 LTS. I do not want to disable *NetworkManager* so I needed to find a way to do spoofing on Linux with it.

*NetworkManager* can be controlled from command line through its utility *nmcli*. *nmcli* supports MAC spoofing through the *cloned-mac-address* option. Therefore, I wrote a few Python wrappers to help me use nmcli for performing flexible MAC spoofing.

## The randommac code structure

- **/randommac/** contains the python code and an *OUI.list* file that is used for generating valid random MAC addresses with valid manufacturer ID. Interaction with the code should rely on functions from *randommac_interface.py* for use as a Python module, or *randommac_commandline.py* for use as a command line tool.
- **/examples/** contains examples of how to use as a Python module. You can start by testing the random MAC number generation (*python_compute_random_MAC.py*), then create new dummy spoofed connections (*python_new_spoofed_connection.py*), inspect it (*python_inspect_connection.py*) and spoof it again (*python_spoof_existing_connection.py*). You can also have a look at the interactive interface (*python_interactive_interface.py*). All those functionalities are also available directly from the command line tool when installed by pip (see **installation**), so on a daily usage you should not need to call the python modules.

## Installation

- either clone the repository and directly execute the python code
- or more simply for using the functionalities as Python module or command line: *$ pip install randommac*

## Quick start

For a quick step-by-step demonstration of the module, try the interactive interface.
- either launch by executing *examples/python_interactive_interface.py*
- or execute in terminal after pip install by: *$ randommac -i*

## Command line tool examples

- After having installed by pip, you will get access to the command line tools:

```
$ randommac -h
usage: randommac [-h] [-i] [-n] [-d DETAILS] [-r] [-s SPOOF] [-c CONNECTSPOOF]
                 [-p PASSWORD] [-a]

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
  -a, --all             spoof all known connections, each with its own random
                        MAC
```

- For getting info from nmcli:

`
~$ randommac -i
`

- For spoofing connection CONN, that already exists:

`
~$ randommac -s CONN
`

- For creating a new connection on an unknown network NETW, obtained from example from the nmcli info command, that will be spoofed since the beginning (note that you can add a WPA / WPA2 password by adding -p PASSWORD):

`
~$ randommac -c NETW
`

- For spoofing all know connections, all with get their own MAC:

`
~$ randommac -a
`

## Comments

- When changing MAC of existing network (either one or all), NetworkManager will briefly be shut off and therefore all connections under control of NetworkManager will be briefly suspended. This is to ensure that NetworkManger will have to restart any opened connection and therefore update the modified cloned MAC addressed.

- More functionalities are available through the Python module interface than the command line, but the command line should be enough for most daily use.

- To create a new connection, you do not want your MAC address to leak. Therefore first create a new spoofed connection profile, and only later activate it to connect to the network.

## Disclaimer

- This is a little side project I did to develop my Python skills. It is not intensively tested (at least not by me). If you want to seriously use this module, please test it (legally) against offensive security tools to check for leaking MAC and other bugs. If you perform some tests, it would be nice to post some reports in the **Report test** issue thread of this repository.

- As indicated in the license, this code comes without any warranty of any type and I cannot be held responsible for any damage arising from using this code. You should also make sure that you follow the legislation of your local country and do not use this code to break against the law.

## To do

This is a work in progress. Please report any bug / feature request.

- interactive interface: some missing functions
- command line interface: some missing functions
- add periodic automatic spoofing
- documentation
- website post
