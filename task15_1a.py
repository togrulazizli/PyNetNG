
import re
from pprint import pprint

#def get_ip_from_cfg_interface(file):
#    result = {}
#    regex = (r"interface (?P<interface>\S+)"
#             r"[\s\S]*?"
#            r"ip\saddress\s(?P<IP>\d+\.\d+\.\d+\.\d+)\s(?P<Subnet>\S+)")
#    with open('config_r1.txt') as f:
#        match_iter = re.finditer(regex,f.read())
#        for match in match_iter:
#            result[match.group('interface')] = match.group('IP','Subnet')
#    return result
#
#if __name__=="__main__":
#    pprint (get_ip_from_cfg_interface('config_r1.txt'))


#interface Loopback0
# ip address 10.1.1.1 255.255.255.255

def get_ip_from_cfg_interface_2(file):
    result = {}
    with open(file) as f:
        regex = (r"interface (?P<int>\S+\d)"
        r"| ip address (?P<ip>\S+) (?P<mask>\S+)")
        for line in f:
            m = re.search(regex,line)
            if m:
                group = m.lastgroup
                value = m.group(group)
                if group == "int":
                    result[value] = {}
                    interface = value
                else:
                    result[interface] = m.group("ip","mask")

    result = dict([(k,v) for k,v in result.items() if len(v)>0])

    return result


if __name__=="__main__":
    pprint (get_ip_from_cfg_interface_2('config_r1.txt'))