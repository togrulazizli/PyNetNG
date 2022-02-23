
import re
import os.path
from pprint import pprint
import csv

def write_dhcp_snooping_to_csv(*argv,output):
    result_ls = []

    column = ['switch','mac','ip','vlan','interface']
    regex = r"(?P<mac>\S+:\w+) +(?P<ip>(?:\d+\.)+\d+) +\w+ +\S+ +(?P<vlan>\d+) +(?P<int>\S+)"
    for arg in argv:
        extension = os.path.splitext(arg)[0]
        device_name = extension.split('_')[0]
        with open(arg) as f:
            match = re.finditer(regex,f.read())
            for m in match:
                line = list(m.groups())
                line.insert(0,device_name)
                result_ls.append(line)
    

    result_ls.insert(0,column)
    
    with open (output,'w') as b:
        writer = csv.writer(b)
        for row in result_ls:
            writer.writerow(row)



    

if __name__ == "__main__":
    #pprint (write_dhcp_snooping_to_csv("sw1_dhcp_snooping.txt","sw2_dhcp_snooping.txt","sw3_dhcp_snooping.txt",output="final_output.csv"))
    write_dhcp_snooping_to_csv("sw1_dhcp_snooping.txt","sw2_dhcp_snooping.txt",output="final_output.csv")



#import csv
#import re
#import glob
#
#
#def write_dhcp_snooping_to_csv(filenames, output):
#    regex = r"(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)"
#    with open(output, "w") as dest:
#        writer = csv.writer(dest)
#        writer.writerow(["switch", "mac", "ip", "vlan", "interface"])
#        for filename in filenames:
#            switch = re.search("([^/]+)_dhcp_snooping.txt", filename).group(1)
#            with open(filename) as f:
#                for line in f:
#                    match = re.search(regex, line)
#                    if match:
#                        writer.writerow((switch,) + match.groups())
#
#
#if __name__ == "__main__":
#    sh_dhcp_snoop_files = glob.glob("*_dhcp_snooping.txt")
#    write_dhcp_snooping_to_csv(sh_dhcp_snoop_files, "example_csv.csv")