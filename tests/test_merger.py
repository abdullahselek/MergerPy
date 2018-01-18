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

    def test_process(self):
        self.assertEqual(merger.process('tests/resources/sample.txt'), 'ABE,ABi,AB34,AB26,ABs,AsE,Asi,As34,As26,Ass,AhE,Ahi,Ah34,Ah26,Ahs,AiE,Aii,Ai34,Ai26,Ais,ArE,Ari,Ar34,Ar26,Ars,1BE,1Bi,1B34,1B26,1Bs,1sE,1si,1s34,1s26,1ss,1hE,1hi,1h34,1h26,1hs,1iE,1ii,1i34,1i26,1is,1rE,1ri,1r34,1r26,1rs,eBE,eBi,eB34,eB26,eBs,esE,esi,es34,es26,ess,ehE,ehi,eh34,eh26,ehs,eiE,eii,ei34,ei26,eis,erE,eri,er34,er26,ers,2BE,2Bi,2B34,2B26,2Bs,2sE,2si,2s34,2s26,2ss,2hE,2hi,2h34,2h26,2hs,2iE,2ii,2i34,2i26,2is,2rE,2ri,2r34,2r26,2rs,aBE,aBi,aB34,aB26,aBs,asE,asi,as34,as26,ass,ahE,ahi,ah34,ah26,ahs,aiE,aii,ai34,ai26,ais,arE,ari,ar34,ar26,ars,3BE,3Bi,3B34,3B26,3Bs,3sE,3si,3s34,3s26,3ss,3hE,3hi,3h34,3h26,3hs,3iE,3ii,3i34,3i26,3is,3rE,3ri,3r34,3r26,3rs')

    def test_main(self):
        self.assertTrue(merger.main('tests/resources/sample.txt'))
