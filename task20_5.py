import os

import yaml
from jinja2 import Environment, FileSystemLoader

data = {
    'tun_num': 10,
    'wan_ip_1': '192.168.100.1',
    'wan_ip_2': '192.168.100.2',
    'tun_ip_1': '10.0.1.1 255.255.255.252',
    'tun_ip_2': '10.0.1.2 255.255.255.252'
}



result = []

def generate_ospf_config(*templates,data=data):


    for template in templates:
        temp_dir , temp_filename = os.path.split(template)

        env = Environment(loader=FileSystemLoader(temp_dir), lstrip_blocks=True, trim_blocks=True)
        temp = env.get_template(temp_filename)

        result.append(temp.render(data))
    #return result
    
    with open("cisco_vpn1.txt","w") as f:
        f.write(result[0])
        
    with open("cisco_vpn2.txt","w") as f:
        f.write(result[1])


if __name__ == "__main__":
    template_path_1 = "templates/vpn1.txt"
    template_path_2 = "templates/vpn2.txt"
    #data_path = "data_files/vlan.yml"
    #with open(data_path) as f:
    #    data = yaml.safe_load(f)

    generate_ospf_config(template_path_1,template_path_2)