
'''
import ipaddress


def convert_ranges_to_ip_list(ip_addresses):
    ip_list = []
    for ip_address in ip_addresses:
        if "-" in ip_address:
            start_ip, stop_ip = ip_address.split("-")
            if "." not in stop_ip:
                stop_ip = ".".join(start_ip.split(".")[:-1] + [stop_ip])
            start_ip = ipaddress.ip_address(start_ip)
            stop_ip = ipaddress.ip_address(stop_ip)
            for ip in range(int(start_ip), int(stop_ip) + 1):
                ip_list.append(str(ipaddress.ip_address(ip)))
        else:
            ip_list.append(str(ip_address))
    return ip_list
    
'''




from pprint import pprint
addresses = ['8.8.8.8','11.1.1.1-5','10.1.1.1-10.1.1.10']
final = []



def convert_ranges_to_ip_list(list):
    for i in addresses:

        if '-' in i.split('.')[3] and len(i.split('.'))>4:
            first , second, third , last, u, c ,last2 = i.split('.')
            start = int(last.split('-')[0])
            end = int(last2)
            for x in range(start,end+1):
                ip = '.'.join([first,second,third,str(x)])
                final.append(ip)

        if '-' in i.split('.')[3] and len(i.split('.'))<=4:
            first , second, third , last = i.split('.')
            start = int(last.split('-')[0])
            end = int(last.split('-')[1])
            #print (type(end))
            for x in range(start,end+1):
                ip = '.'.join([first,second,third,str(x)])
                final.append(ip)
        if not '-' in i:
            final.append(i)
    return final

            



if __name__=="__main__":
    pprint (convert_ranges_to_ip_list(addresses))



