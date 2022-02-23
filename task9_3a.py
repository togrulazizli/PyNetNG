def get_int_vlan_map(filename): 
    f = open(filename,'r')
    lines = f.readlines()
    a = 0
    trunk = {}
    access = {}
    characters_to_remove = "'"
    for line in lines:
        a = a +1
        vlan = []
        if "FastE" in line:
            interface = line.split(" ")[1].strip('\n')
        if "access vlan" in line:

            vlan = line.split(" ")[4].strip("\n").split(',')
            access[interface] = [int(i) for i in vlan]
        if "allowed vlan" in line:

            vlan = line.split(" ")[5].strip('\n').split(',')

            trunk[interface] = [int(i) for i in vlan]
        if "mode access" in line and "duplex" in lines[a+1]:
            print(line)
            print (lines[a+1])
            access[interface] = 1

            
        #print (f'line {a}: {line}')

    return access,trunk

print(get_int_vlan_map("config_sw2.txt"))

 


