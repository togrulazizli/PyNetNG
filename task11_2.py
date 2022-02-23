
from venv import create
from task11_1_b import parse_cdp_neighbors
from pprint import pprint
infiles = ["sh_cdp_n_sw1.txt","sh_cdp_n_r1.txt","sh_cdp_n_r2.txt","sh_cdp_n_r3.txt"]
result_a = {}
def create_network_map():  
    for i in infiles:
        with open(i) as f:
            result_a.update(parse_cdp_neighbors(f.read()))
    return result_a

final = create_network_map()
dup_re = dict(final)
to_remove = {}
for a,x in final.items():
    for b in final.values():
        if a==b:
            del dup_re[a]
            to_remove[a]=x


            

#pprint(dup_re) 
#pprint("------------------------------------")
#
#pprint(u)

def unique_network_map(final):
    network_map = {}
    for key, value in final.items():
        
        if network_map.get(value) != key:
            network_map[key] = value
    return network_map

aa = unique_network_map(final)
pprint (aa)