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
from artikcloud.models.tasks_status_counts import TasksStatusCounts


class TestTasksStatusCounts(unittest.TestCase):
    """ TasksStatusCounts unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTasksStatusCounts(self):
        """
        Test TasksStatusCounts
        """
        model = artikcloud.models.tasks_status_counts.TasksStatusCounts()


if __name__ == '__main__':
    unittest.main()
