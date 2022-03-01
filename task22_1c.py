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



class Topology:
    def __init__(self,topology):
        self.topology = self._normalize(topology)


    def _normalize(self,input):
        
        result= {}
        
        for key , value in input.items():
            
            if not result.get(value) == key:
                result[key] = value
        
        return result

    def delete_link(self, input1, input2):
        #if self.topology.get(input1) == input2:
        if input1 in self.topology and input2 in self.topology.values():
            self.topology.pop(input1)
            return self.topology
           
        #elif self.topology.get(input2) == input1:
        elif input2 in self.topology and input1 in self.topology.values():
            self.topology.pop(input2)
            return self.topology
            
        else:
            pprint("There is no such link")
    
    def delete_node(self,node):
        
        result = {}
        
        for key, value in self.topology.items():
   
            if not key[0] == node and not value[0] == node:
                result[key] = value

             
        if len(result.values()) == len(self.topology.values()):
            return "There is no such device"
        else:
            return result




if __name__ == "__main__":

    top = Topology(topology_example)
    pprint(top.topology)
    pprint("-"*20)
    pprint(top.delete_node('SW1'))