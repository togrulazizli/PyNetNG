import re
from pprint import pprint


def convert_ios_nat_to_asa(input,output):
    regex =( r"\S+ (?P<type>\w+) (?P<host>(?:\d+\.)+\d+) (?P<source_port>\d+) .+ (?P<destination_port>\d+)")
    cfg_lines = []
    with open(input) as f:      
        for i in f:
            m = re.search(regex,i)
            if m:
                cfg_lines.append(f"object network LOCAL_{m.group('host')}")
                cfg_lines.append(f" host {m.group('host')}")
                cfg_lines.append(f" nat (inside,outside) static inteface service {m.group('type')} {m.group('source_port')} {m.group('destination_port')}")
 
 
    cfg_string = '\n'.join(cfg_lines)
    x = open(output,'a')
    x.write(cfg_string) 
 



if __name__=="__main__": 
    convert_ios_nat_to_asa('cisco_nat_config.txt','asa_nat.txt')