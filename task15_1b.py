import re
from pprint import pprint

def get_ip_from_cfg_interface(file):
    result = {}
    regex = (r"interface (?P<intf>\S+)(?:[\s+\S+]+?)"
    r"(?:address (?P<ip>\S+) (?P<mask>(?:\d+\.)+\d+))\n"
    r"(?: ip address (?P<ip2>\S+) (?P<mask2>(?:\d+\.)+\d+))*")
    with open(file) as f:
        match_iter = re.finditer(regex,f.read())
        for match in match_iter:
            #pprint(match.group())
            result[match.group('intf')] = re.findall("ip address (\S+) (\S+)",match.group())
    return result

if __name__=="__main__":
    pprint (get_ip_from_cfg_interface('config_r2.txt'))





