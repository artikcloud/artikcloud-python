# coding: utf-8

"""
    ARTIK Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import artikcloud
from artikcloud.rest import ApiException
from artikcloud.models.task_by_did import TaskByDid


class TestTaskByDid(unittest.TestCase):
    """ TaskByDid unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTaskByDid(self):
        """
        Test TaskByDid
        """
        model = artikcloud.models.task_by_did.TaskByDid()


if __name__ == '__main__':
    unittest.main()
