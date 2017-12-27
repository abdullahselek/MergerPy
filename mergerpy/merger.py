#!/usr/bin/env python

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
