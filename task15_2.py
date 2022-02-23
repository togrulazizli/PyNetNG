import re
from pprint import pprint


result = []

def parse_sh_ip_int_br(file):
    regex = (r"(?P<int>\S+d?) +(?P<ip>\S+) +\w+ \S+ *"
    r"(?P<status>up|down|administratively down) +(?P<protocol>up|down)")
    with open(file) as f:
        for line in f:
            m = re.search(regex,line)
            if m:
                result.append(m.groups())
    return result



if __name__=="__main__":
    pprint (parse_sh_ip_int_br("sh_ip_int_br.txt"))
