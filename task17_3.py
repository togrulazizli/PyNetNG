import re
from pprint import pprint



def parse_sh_cdp_neighbors(input):
    cdp_peers = {}
    regex = r"(?P<remote_device>\S+) +(?P<local_port>\S+ \S+).+ (?P<remote_port>\S+ \d+\S+)"
    local_device_reg = r"(\S+)>"
    match_1 = re.findall(local_device_reg,input)
    cdp_peers[match_1[0]] = {}
    match = re.finditer(regex,input)
    for m in match:
        cdp_peers[match_1[0]][m.group('local_port')] = {m.group('remote_device'): m.group('remote_port')}
    return cdp_peers


#def parse_sh_cdp_neighbors(command_output):
#    regex = re.compile(
#        r"(?P<r_dev>\w+)  +(?P<l_intf>\S+ \S+)"
#        r"  +\d+  +[\w ]+  +\S+ +(?P<r_intf>\S+ \S+)"
#    )
#    connect_dict = {}
#    l_dev = re.search(r"(\S+)[>#]", command_output).group(1)
#    connect_dict[l_dev] = {}
#    for match in regex.finditer(command_output):
#        r_dev, l_intf, r_intf = match.group("r_dev", "l_intf", "r_intf")
#        connect_dict[l_dev][l_intf] = {r_dev: r_intf}
#    return connect_dict

if __name__=="__main__":
    x = open("sh_cdp_n_r3.txt")
    pprint(parse_sh_cdp_neighbors(x.read()))