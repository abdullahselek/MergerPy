#!/usr/bin/env python

import unittest
from mergerpy import merger

class MergerTest(unittest.TestCase):

    def test_load_file(self):
        lines = merger.load_file('tests/resources/sample.txt')
        self.assertEqual(len(lines), 3)
