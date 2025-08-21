# Changing your MAC address in Linux
# creat functions to allow you to change mac bassed on the os you are using

import subprocess
import optparse
import re

def get_arguments():
    # create the object that can handal user arguments ⬇️
    parser = optparse.OptionParser() 
    # adding options to the object ⬇️⬇️⬇️
    parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    # contains the users inpurs in "options"
    (options, arguments) = get_arguments()
    # error handling
    if not options.interface:
        parser.error("Please enter a interface, for help use --help")
    elif not options.new_mac:
        parser.error("Please enter a new MAC address, for help use --help")
    
    return options

def change_mac(interface, new_mac):
    # for the user to see
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    # runs commands in the terminal
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
# change_mac(options.interface, options.new_mac)

# checking the output to see if the mac address changed
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)

mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
if mac_address_search_result:
    print(mac_address_search_result.group(0))
else:
    print("[ - ] could not read MAC address.")