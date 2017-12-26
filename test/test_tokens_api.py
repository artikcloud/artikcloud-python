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
from artikcloud.apis.tokens_api import TokensApi


class TestTokensApi(unittest.TestCase):
    """ TokensApi unit test stubs """

    def setUp(self):
        self.api = artikcloud.apis.tokens_api.TokensApi()

    def tearDown(self):
        pass

    def test_check_token(self):
        """
        Test case for check_token

        Check Token
        """
        pass

    def test_refresh_token(self):
        """
        Test case for refresh_token

        Refresh Token
        """
        pass

    def test_token_info(self):
        """
        Test case for token_info

        Token Info
        """
        pass


if __name__ == '__main__':
    unittest.main()
