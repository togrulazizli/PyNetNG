access_mode_template = [
"switchport mode access",
"switchport access vlan",
"switchport nonegotiate",
"spanning-tree portfast",
"spanning-tree bpduguard enable",
]
access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}
access_config_2 = {
"FastEthernet0/3": 100,
"FastEthernet0/7": 101,
"FastEthernet0/9": 107,
}


def generate_access_config(intf_vlan_mapping, access_template):
    """
        intf_vlan_mapping is a dictionary with interface-VLAN mapping:
        {'FastEthernet0/12': 10,
        'FastEthernet0/14': 11,
        'FastEthernet0/16': 17}
        access_template - list of commands for the port in access mode
        Returns a list of commands.
    """
    config = []
    number = len (access_template)
    for int , vlan  in intf_vlan_mapping.items():
        config.append("interface {}".format(int))
        for i in access_template:
            if i.endswith("vlan"):
                config.append(f"{i} {vlan}")
                
            else:
                config.append(i)
        config.append("\n")        

    return config
result =  generate_access_config(access_config,access_mode_template)
#print (result)


output = '\n'.join(result)
    #print (i)

print (output)



#print (generate_access_config(access_config,access_mode_template ))
