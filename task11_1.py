def parse_cdp_neighbors(out):
    final_dict = {}
    
    device_name = out.split(">")[0]
    out_lst = out.split("\n")[6:]
    for a, i  in enumerate (out_lst):
        out_lst[a] =[s for s in i.split(" ") if s != ""]
        out_lst[a] = out_lst[a][:3] + out_lst[a][8:]
        out_lst[a][1:3] = [''.join(out_lst[a][1:3])]
        out_lst[a][2:4] = [''.join(out_lst[a][2:4])]
    
    for i in out_lst:
        
        final_dict[(device_name,i[1])] = (i[0],i[2])
        
    return final_dict


if __name__=="__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        print (parse_cdp_neighbors(f.read()))



       





