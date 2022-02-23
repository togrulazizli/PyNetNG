import yaml
from pprint import pprint


def transform_topology(input):
    with open(input) as f:
        template = yaml.safe_load(f)
    result = {}
    network_map = {}
    for k,v in template.items():
        for inner_k, inner_v in template[k].items():
            result[(k,inner_k)] = list(template[k][inner_k].items())[0]

        
    for key, value in result.items():
        
        if network_map.get(value) != key:
            network_map[key] = value
    return network_map
    
    



if __name__ == "__main__":
    pprint (transform_topology("topology.yaml"))


