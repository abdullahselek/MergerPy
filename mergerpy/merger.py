#!/usr/bin/env python

def load_file(filename):
    with open(filename, 'r') as payload_file:
        lines = []
        for line in payload_file:
            lines.append(line)
        return lines
