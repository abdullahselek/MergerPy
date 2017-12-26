#!/usr/bin/env python

def load_file(filename):
    """Loads given text file from directory into string lines"""
    with open(filename, 'r') as payload_file:
        lines = []
        for line in payload_file:
            lines.append(line)
        return lines
