import yaml
import os
from jinja2 import Environment, FileSystemLoader
from pprint import pprint

def generate_router_config(template_location,data):
    directory, filename = os.path.split(template_location)
    env = Environment(loader=FileSystemLoader(directory),trim_blocks=True,lstrip_blocks=True )
    temp1 = env.get_template(filename)
    
    return temp1.render(data)





if __name__ == "__main__":
    template_location =  "templates/cisco_router_base.txt"
    data_location = "data_files/router_info.yml"
    with open(data_location) as f:
        data = yaml.safe_load(f)
    config = generate_router_config(template_location,data)
    with open("config_test.txt","w") as c:
        c.write(config)

    #print(config)