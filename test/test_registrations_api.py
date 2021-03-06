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
from artikcloud.apis.registrations_api import RegistrationsApi


class TestRegistrationsApi(unittest.TestCase):
    """ RegistrationsApi unit test stubs """

    def setUp(self):
        self.api = artikcloud.apis.registrations_api.RegistrationsApi()

    def tearDown(self):
        pass

    def test_confirm_user(self):
        """
        Test case for confirm_user

        Confirm User
        """
        pass

    def test_get_request_status_for_user(self):
        """
        Test case for get_request_status_for_user

        Get Request Status For User
        """
        pass

    def test_unregister_device(self):
        """
        Test case for unregister_device

        Unregister Device
        """
        pass


if __name__ == '__main__':
    unittest.main()
