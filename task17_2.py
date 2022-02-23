import re
import os.path
from pprint import pprint
import csv
import glob
from numpy import mat




def parse_sh_version(sh_ver):
    regex = r"Cisco IOS.+? (\d+\.\S+).*uptime is (.+?)\n.*file is \"(.+?)\"\n"    
    match = re.search(regex,sh_ver,re.DOTALL)
    if match:
        return match.groups()


def write_inventory_to_csv(filenames,output):
    with open(output,'w') as k:
        writer = csv.writer(k)
        writer.writerow(["hostname", "ios", "image", "uptime"])
        for file in filenames:
            extension = os.path.splitext(file)[0]
            device_name = extension.split('_')[2]
            with open (file) as f:
                final = [device_name] + list(parse_sh_version(f.read()))

                writer.writerow(final)



if __name__=="__main__":
    sh_version_files = glob.glob("sh_vers*")
    write_inventory_to_csv(sh_version_files,output="inventory.csv")

