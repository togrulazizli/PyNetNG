from ast import Raise


class IPAdress:
    def __init__(self,ip,mask):
        self.ip , self.mask = ip , mask
        self._validate_ip(ip)
        self._validate_mask(mask)


    def _validate_ip(self,ip):
        octets = ip.split(".")
        if len(octets) != 4:
            raise ValueError('Incorrect IP address')
        for octet in octets:
            if octet.isdigit() == False:
                raise ValueError('Incorrect IP address')
            elif int(octet) >= 255 or int(octet) <= 0:
                raise ValueError('Incorrect IP address')
        else:
            return True

    def _validate_mask (self, mask):
        if  0<= mask <=32:
            return True
        else:
            raise ValueError('Incorrect mask')
        

if __name__=="__main__":
    ip1 = IPAdress("10.10.1.1335",34)