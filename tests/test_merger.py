#!/usr/bin/env python

import unittest
from mergerpy import merger

class MergerTest(unittest.TestCase):

    def test_load_file(self):
        lines = merger.load_file('tests/resources/sample.txt')
        self.assertEqual(len(lines), 3)

    def test_parse_input(self):
        lines = merger.load_file('tests/resources/sample.txt')
        parsed_input = merger.parse_input(lines)
        self.assertEqual(len(parsed_input), 3)

    def test_merge_input(self):
        lines = merger.load_file('tests/resources/sample.txt')
        parsed_input = merger.parse_input(lines)
        merged_file_created = merger.merge_input(parsed_input)
        self.assertTrue(merged_file_created)        
