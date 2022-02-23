import csv
from pprint import pprint


def write_last_log_to_csv(input):
    with open(input) as f:
        reader = csv.reader(f)