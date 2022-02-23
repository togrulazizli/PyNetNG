import re
from pprint import pprint
from tokenize import group


def generate_description_from_cdp(file):
    cdp_peers = {}
    regex = r"(?P<remote_device>\S+) +(?P<local_port>\w+ \d.\d) .+?\w+ .+?\d+ +(?P<remote_port>\S+ \S+)"
    with open(file) as f:
        match = re.finditer(regex,f.read())
        for m in match:
            cdp_peers[m.group('local_port')] = f"description Connected to {m.group('remote_device')} port {m.group('remote_port')}"
    return cdp_peers


if __name__ == '__main__':
    pprint(generate_description_from_cdp('sh_cdp_n_sw1.txt'))


