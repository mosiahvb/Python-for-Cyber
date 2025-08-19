# Changing your MAC address in Linux

import subprocess
import optparse

# create the object that can handal user arguments ⬇️
parser = optparse.OptionParser() 
# adding options to the object ⬇️⬇️⬇️
parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m","--mac", dest="new_mac", help="New MAC address")
# Reads what the user has entered to be handled ⬇️⬇️
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print(f"[+] Changing MAC address for {interface} to {new_mac}")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

