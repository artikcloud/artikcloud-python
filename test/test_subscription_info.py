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
from artikcloud.models.subscription_info import SubscriptionInfo


class TestSubscriptionInfo(unittest.TestCase):
    """ SubscriptionInfo unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubscriptionInfo(self):
        """
        Test SubscriptionInfo
        """
        model = artikcloud.models.subscription_info.SubscriptionInfo()


if __name__ == '__main__':
    unittest.main()
