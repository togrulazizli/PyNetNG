import os

import yaml
from jinja2 import Environment, FileSystemLoader


def generate_ospf_config(template, data):
    temp_dir , temp_filename = os.path.split(template)

    env = Environment(loader=FileSystemLoader(temp_dir), lstrip_blocks=True, trim_blocks=True)
    temp = env.get_template(temp_filename)

    return temp.render(data)


if __name__ == "__main__":
    template_path = "templates/ospf.txt"
    data_path = "data_files/ospf.yml"
    with open(data_path) as f:
        data = yaml.safe_load(f)

    print (generate_ospf_config(template_path,data))