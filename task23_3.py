

from pprint import pprint

topology_example = {('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

topology_example2 = {('R1', 'Eth0/4'): ('R7', 'Eth0/0'),
                    ('R1', 'Eth0/6'): ('R9', 'Eth0/0')}


class Topology:
    def __init__(self,topology):
        self.topology = self.topologyfinal(topology)
        
        


    def topologyfinal(self,topology):
        
        result= {}
        
        for key , value in topology.items():
            
            if not result.get(value) == key:
                result[key] = value
        
        

        return result


    def __add__(self,other):
       z = {**self.topology, **other.topology}
       return Topology(z)

       #return Topology(z.update(other))

    def __iter__(self):
        return iter(self.topology.items())
        


if __name__ == "__main__":
    t1 = Topology(topology_example)
    t2 = Topology(topology_example2)
    t3 = t1 + t2
    #pprint (t3.topology)
    for i in t3:
        print (i)
    ##print (t3.topology)
