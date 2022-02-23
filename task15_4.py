import re
from pprint import pprint


def get_ints_without_description(file):
    
    regex = r"!\ninterface (?P<int>\S+)\n [^d]"

    with open(file) as f:
        interfaces = [m.group('int') for m in re.finditer(regex,f.read())]

    return interfaces



#def get_ints_without_description(file):
#    
#    regex = r"!\ninterface (?P<int>\S+)\n [^d]"
#
#    with open(file) as f:
#        interfaces = re.findall(regex,f.read())
#    
#    return interfaces
#



if __name__ == "__main__":
    pprint (get_ints_without_description('config_r1.txt'))

