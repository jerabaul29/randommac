import randommac.randommac_interface as macchanger

macchanger.nmcli_available_wifi()
macchanger.add_new_wifi_spoofed_connection('Dobbeltagentan',connection_password="bla450FFg542FF")
macchanger.nmcli_show_connections()
macchanger.nmcli_saved_connections()
macchanger.show_MAC_address_connection('Get-1b7f62',DEBUG=True)
macchanger.change_MAC_network(['Get-1b7f62'])
macchanger.show_MAC_address_connection('Get-1b7f62',DEBUG=True)

macchanger.step_by_step_interface()

import sys
import os
os.getcwd()
os.path.dirname(__file__)
