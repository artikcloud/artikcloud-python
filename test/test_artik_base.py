# coding: utf-8

from __future__ import absolute_import

import os
import sys
import unittest

class TestArtikBase(unittest.TestCase):
    """ Artik tests base class """

    def __init__(self, *args, **kwargs):
        self.load_properties()
        super(TestArtikBase, self).__init__(*args, **kwargs)

    def load_properties(self):

        properties_filename = 'artik.properties'

        self.properties = {}

        with open(properties_filename) as f:

            lines = f.readlines()

            for line in lines:

                line = line.rstrip('\n').strip()

                if line.startswith('#') | ('=' not in line) | (line == ''):
                    continue

                key_value = line.split('=')
                key = key_value[0]
                value = key_value[1:][0].strip()
                self.properties[key] = value


if __name__ == '__main__':
    unittest.main()
