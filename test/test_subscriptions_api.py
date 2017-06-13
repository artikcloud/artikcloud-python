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
from artikcloud.apis.subscriptions_api import SubscriptionsApi


class TestSubscriptionsApi(unittest.TestCase):
    """ SubscriptionsApi unit test stubs """

    def setUp(self):
        self.api = artikcloud.apis.subscriptions_api.SubscriptionsApi()

    def tearDown(self):
        pass

    def test_create_subscription(self):
        """
        Test case for create_subscription

        Create Subscription
        """
        pass

    def test_delete_subscription(self):
        """
        Test case for delete_subscription

        Delete Subscription
        """
        pass

    def test_get_all_subscriptions(self):
        """
        Test case for get_all_subscriptions

        Get All Subscriptions
        """
        pass

    def test_get_messages(self):
        """
        Test case for get_messages

        Get Messages
        """
        pass

    def test_get_subscription(self):
        """
        Test case for get_subscription

        Get Subscription
        """
        pass

    def test_validate_subscription(self):
        """
        Test case for validate_subscription

        Validate Subscription
        """
        pass


if __name__ == '__main__':
    unittest.main()