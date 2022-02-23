import re
from pprint import pprint
import glob
from task17_3 import parse_sh_cdp_neighbors
import yaml


#def parse_sh_cdp_neighbors(input):
#    cdp_peers = {}
#    topology = {}
#    regex = r"(?P<remote_device>\S+) +(?P<local_port>\S+ \S+).+ (?P<remote_port>\S+ \d+\S+)"
#    local_device_reg = r"(\S+)>"
#    for file in input:
#        with open(file) as f:
#            match_1 = re.findall(local_device_reg,f.read())
#            cdp_peers[match_1[0]] = {}
#            match = re.finditer(regex,f.read())
#            for m in match:
#                
#                cdp_peers[match_1[0]][m.group('local_port')] = {m.group('remote_device'): m.group('remote_port')}
#        
#    return cdp_peers


def generate_sh_cdp_topology(input,output=None):
    result = {}
    for file in input:
        with open(file) as f:
            result.update(parse_sh_cdp_neighbors(f.read()))

    if output:
        with open(output,"w") as fout:
            yaml.dump(result,fout,default_flow_style=False)
    return result



if __name__=="__main__":
    files = glob.glob("sh_cdp*")
    pprint(generate_sh_cdp_topology(files))