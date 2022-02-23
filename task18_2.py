
import yaml
from netmiko import ConnectHandler
import netmiko
from pprint import pprint


def send_show_command(device,command):
    
    with netmiko.ConnectHandler(**device) as ssh:
        
        result = ssh.send_config_set(command)
    return result




if __name__ == "__main__":
    command = ["logging buffered xml","no logging console"]
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        #pprint (devices)
        for device in devices:
            pprint(send_show_command(device,command))


