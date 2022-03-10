from subprocess import check_output
from re import split
output = check_output(['arp']).decode().strip().split('\n')[1:]
mac_lookup = {}
for x in open('vendorMacs.txt').read().strip().split('\n'):
    address, company = x.split(' ', 1)
    mac_lookup[address] = company
for x in output:
    address, HW, MAC, flag, interface = split(r' +', x)
    print(address, mac_lookup[MAC[:8].upper()])
