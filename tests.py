#!/usr/bin/env python

interface = input("Enter interface type and number: ")
vlan = input("Enter VLAN number: ")

access_template = [
    'switchport mode acceess',
    'switchport access vlan {}',
    'switchport nonegotiate',
    'spanning-tree port fast',
    'spanning-tree bpduguard enable'
]

<<<<<<< HEAD
print('\n' + '-' * 30)
print('interface {}'.format(interface))
print("\n".join(access_template).format(vlan))
=======
print("\n".join(access_template).format(10))
>>>>>>> a796525e7f36818463ff58687de36bf274c73629
