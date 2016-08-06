# randommac

A MAC changer for Linux with Network Manager support

## macchanger and the NetworkManager problem

As I searched the Internet for MAC spoofing solutions, it appeared that the main tool available for Linux (*macchanger*) breaks when *NetworkManager* is used for monitoring of the connections, which is the default on for example Ubuntu 16.04 LTS. I do not want to disable *NetworkManager* so I needed to find a way to do spoofing on Linux with it.

*NetworkManager* can be controlled from command line through its utility *nmcli*. *nmcli* supports MAC spoofing through the *cloned-mac-address* option. Therefore, I wrote a few Python wrappers to help me use nmcli for performing flexible MAC spoofing

## randommac

- /data/ contains an OUI.list file that is used for generating valid random MAC addresses with valid manufacturer ID
- /randommac/ contains the code. Interaction with the code should rely on functions from randommac_interface.py for use as a Python module, or randommac for use as a command line tool
- /examples/ contains examples of how to use the Python module

## To do
- command line interface
- documentation
- examples
- release
- post answers to people having problem with NM and maccanger:
http://askubuntu.com/questions/603196/macchanger-wlan-not-working
https://github.com/alobbs/macchanger/issues/22
http://askubuntu.com/questions/173084/ubuntu-12-04-system-error-macchanger-issue
- website post?
- take care of re opening network manager if bug in one of the functions
