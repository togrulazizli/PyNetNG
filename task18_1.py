
import yaml
from netmiko import ConnectHandler
import netmiko
from pprint import pprint


def send_show_command(device,command):
    
    with netmiko.ConnectHandler(**device) as ssh:
        result = ssh.send_command(command)
    return result




if __name__ == "__main__":
    command = "show ip int br"
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        #pprint (devices)
        for device in devices:
            pprint(send_show_command(device,command))


