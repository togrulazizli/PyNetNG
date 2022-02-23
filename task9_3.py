def get_int_vlan_map(filename): 
    f = open(filename,'r')
    lines = f.readlines()

    trunk = {}
    access = {}
    characters_to_remove = "'"
    for line in lines:

        vlan = []
        if "FastE" in line:
            interface = line.split(" ")[1].strip('\n')
        if "access vlan" in line:

            vlan = line.split(" ")[4].strip("\n").split(',')
            access[interface] = [int(i) for i in vlan]
        if "allowed vlan" in line:

            vlan = line.split(" ")[5].strip('\n').split(',')

            trunk[interface] = [int(i) for i in vlan]
        #if "allowed vlan" and "access vlan" not in line:

            #onfig[interface] = None
        #print (f'line {a}: {line}')

    return access,trunk

print(get_int_vlan_map("config_sw1.txt"))

 


