

import ipaddress
from logging import exception


class IPAdress:

    def __init__(self,ip,mask):
        self.ip = ip
        self.mask = mask
        self.ip_str = self.ip +"/"+str(self.mask)
    def ipvalidate(self):
        
        try:
            address = ipaddress.IPv4Address (self.ip)
            network = ipaddress.IPv4Network(self.ip_str,strict=False)
        except ipaddress.AddressValueError:
            print ("Not correct IP address")
        except ipaddress.NetmaskValueError:
            print("Not correct mask")
        else:
            print ("IP address has correct format")
        
       


if __name__ == "__main__":
    ip1 = IPAdress("10.10.10.1",240)
    #print (ip1.ip_str)
    #print (ip1.mask)
    ip1.ipvalidate()