from pprint import pprint
def parse_cdp_neighbors(command_output):
    """
    Here we pass the output of the command as single string because it is in this form that
    received command output from equipment. Taking the output of the command as an argument,
    instead of a filename, we make the function more generic: it can work
    both with files and with output from equipment.
    Plus, we learn to work with such a output.
    """
    result = {}
    for line in command_output.split("\n"):
        line = line.strip()
        columns = line.split()
        
        #print (columns)
        if ">" in line:
            hostname = line.split(">")[0]
        # index 3 is holdtime
        elif len(columns) >= 5 and columns[3].isdigit():
            r_host, l_int, l_int_num, *other, r_int, r_int_num = columns
            result[(hostname, l_int + l_int_num)] = (r_host, r_int + r_int_num)
    return result


if __name__ == "__main__":
    with open("sh_cdp_n_sw1.txt") as f:
        pprint(parse_cdp_neighbors(f.read()))