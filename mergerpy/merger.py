#!/usr/bin/env python

from itertools import product

def load_file(filename):
    """Loads given text file from directory into string lines"""
    with open(filename, 'r') as payload_file:
        lines = []
        for line in payload_file:
            lines.append(line)
        return lines

def parse_input(lines):
    """Parse given input array that contains string lines"""
    parsed_input = []
    for line in lines:
        parsed_data = line.split()
        parsed_input.append(parsed_data)
    return parsed_input

def merge_input(input_array):
    """Merges concatanates given input array into lines of strings"""
    product(*input_array)
    with open('merged.txt', 'w') as merged_file:
        for input_list in product(*input_array):
            merged_str = ''.join(str(e) for e in input_list)
            merged_file.write(merged_str + '\n')
    merged_file.close()
    print('Merged file created successfully!')
    return True
