#!/usr/bin/env python

import unittest
from mergerpy import merger

class MergerTest(unittest.TestCase):

    def test_full_version(self):
        full_version = merger.full_version()
        print(full_version)
        self.assertIsNotNone(full_version)

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

    def test_main(self):
        self.assertTrue(merger.main('tests/resources/sample.txt'))
