trunk_mode_template = [
"switchport mode trunk",
"switchport trunk native vlan 999",
"switchport trunk allowed vlan",
]
trunk_config = {
"FastEthernet0/1": [10, 20, 30],
"FastEthernet0/2": [11, 30],
"FastEthernet0/4": [17],
}

trunk_config_2 = {
"FastEthernet0/11": [120, 131],
"FastEthernet0/15": [111, 130],
"FastEthernet0/14": [117],
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
    
    for int , vlan  in intf_vlan_mapping.items():
        config.append("interface {}".format(int))
        for i in access_template:
            if i.endswith("vlan"):
                config.append(f"{i} {' '.join(str(e) for e in vlan)}")
                
            else:
                config.append(i)
        config.append("\n")        

    return config
result =  generate_access_config(trunk_config,trunk_mode_template)
#print (result)


output = '\n'.join(result)
    #print (i)

print (output)



#print (generate_access_config(access_config,access_mode_template ))
