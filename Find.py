import re
from pprint import pprint


result = {}
regex = (r"interface (?P<interface>\S+)"
         r"[\s\S]*?"
        r"ip\saddress\s(?P<IP>\d+\.\d+\.\d+\.\d+)\s(?P<Subnet>\S+)")
with open('config_r1.txt') as f:
    match_iter = re.finditer(regex,f.read())
    for match in match_iter:
        result[match.group('interface')] = match.group('IP','Subnet')

pprint (result)

#from pprint import pprint
#import re
#
#def get_ip_from_cfg(config):
#    with open(config) as f:
#        regex = re.compile(
#            r"interface (?P<intf>\S+)\n"
#            r"( .*\n)*"
#            r" ip address (?P<ip>\S+) (?P<mask>\S+)"
#        )
#        match = regex.finditer(f.read())
#
#    result = {m.group("intf"): m.group("ip", "mask") for m in match}
#    return result
#
#pprint (get_ip_from_cfg('config_r1.txt'))