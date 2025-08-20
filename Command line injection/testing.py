# Changing your MAC address in Linux
# creat functions to allow you to change mac bassed on the os you are using

import subprocess
import optparse

def get_arguments():
    # create the object that can handal user arguments ⬇️
    parser = optparse.OptionParser() 
    # adding options to the object ⬇️⬇️⬇️
    parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
    # Reads what the user has entered to be handled ⬇️⬇️
    return parser.parse_args()

def change_mac(interface, new_mac):
    # for the user to see
    print(f"[+] Changing MAC address for {interface} to {new_mac}")
    # runs commands in the terminal
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)
