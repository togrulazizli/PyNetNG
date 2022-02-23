
import subprocess
addresses = ['8.8.8.8','11.1.1.1']
available = []
unavailable = []

def ping_ip(ip_address):
    """
    Ping IP address and return tuple:
    On success:
        * True
        * command output (stdout)
    On failure:
        * False
        * error output (stderr)
    """
    reply = subprocess.run(['ping', '-c', '1', '-n', ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return 'Alive' #True, reply.stdout
    else:
        return 'Dead' #False, reply.stderr

def create_list_of_ips():
    for a in addresses:
        if ping_ip(a) == 'Alive':
            available.append(a)
        else:
            unavailable.append(a)  
    return available, unavailable

if __name__=="__main__":


    print (create_list_of_ips()[0],create_list_of_ips()[1]) 

