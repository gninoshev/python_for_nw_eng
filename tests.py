access_template = [
    'switchport mode acceess',
    'switchport access vlan {}',
    'switchport nonegotiate',
    'spanning-tree port fast',
    'spanning-tree bpduguard enable'
]

print("\n".join(access_template).format(10))
test = 2