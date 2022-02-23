
from tabulate import tabulate
from task12_1 import create_list_of_ips
Result = {}


def print_ip_table(list1,list2):
    Result['Reachable'] = list1
    Result['Unreachable'] = list2
    print (tabulate(Result, headers='keys'))


if __name__=="__main__":
    print_ip_table(create_list_of_ips()[0],create_list_of_ips()[1])