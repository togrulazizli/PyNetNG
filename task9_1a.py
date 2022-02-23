
from typing import List, Any , Iterable

access_mode_template = [
"switchport mode access",
"switchport access vlan",
"switchport nonegotiate",
"spanning-tree portfast",
"spanning-tree bpduguard enable",
]

port_security_template = [
"switchport port-security maximum 2",
"switchport port-security violation restrict",
"switchport port-security"
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}
access_config_2 = {
"FastEthernet0/3": 100,
"FastEthernet0/7": 101,
"FastEthernet0/9": 107,
}


def generate_access_config(intf_vlan_mapping, access_template,*args):
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
                config.append(f"{i} {vlan}")
                
            else:
                config.append(i)
        #config.append("\n")  
        if args:

            config.extend(args)
        #    for i in args:
        #           config.append(i)
        #    config.append("\n")    
        config.append("\n")

    return config
result =  generate_access_config(access_config,access_mode_template,port_security_template)

#print (result)

a1 = result[-1]

#x = np.array(result)
#arr = x[np.mod(np.arange(x.size),6)!=0]


#print (len(result))

def flatten (lst: List[Any]) -> Iterable[Any]:
    for sublist in lst:
        if isinstance(sublist,list):
            for item in sublist:
                yield item
        else:
            yield sublist

#print (list(flatten(result)))
#print (result)




#print (result)
#print (a1)

#x = result + a1
#print (x)

output = '\n'.join(list(flatten(result)))
print (output)
#print(flat)

#output = '\n'.join(result)


#print (output)



