import yaml
from jinja2 import Environment, FileSystemLoader
import os


def generate_config(template,data):
    temp_dir , filename = os.path.split(template)

    env = Environment(loader=FileSystemLoader(temp_dir),trim_blocks=True, lstrip_blocks=True)
    temp1 = env.get_template(filename)

    return temp1.render(data)










if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open (data_file) as f:
        data = yaml.safe_load(f)
    print(generate_config(template_file,data))