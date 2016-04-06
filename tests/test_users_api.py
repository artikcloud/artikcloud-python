# coding: utf-8

"""
Run the User API tests.
$ pip install nose (optional)
$ cd artikcloud-python
$ nosetests -v
"""

import os
import time
import unittest

import artikcloud
from artikcloud.rest import ApiException

class UsersApiTests(unittest.TestCase):

    def setUp(self):
        self.api_client = artikcloud.ApiClient()
        self.api_client.set_default_header(header_name="Authorization", header_value="Bearer 51e73cc3ad88418dbf921de4dceacf7e")
        self.users_api = artikcloud.UsersApi(self.api_client)
        self.setUpModels()
        self.user_id = self.users_api.get_self().data.id
        print(self.user_id)

    def tearDown(self):
        # sleep 1 sec between two every 2 tests
        time.sleep(1)

    def setUpModels(self):
        # nothing to do
        time.sleep(1)

    def test_get_self(self):
        response = self.users_api.get_self()
        self.assertIsNotNone(response)
        self.assertEqual(response.data.name, "maneesh")
        self.assertEqual(response.data.full_name, "Maneesh Sahu")
        self.assertEqual(response.data.email, "maneesh.sahu@ssi.samsung.com")

    def test_get_self_async(self):
        def callback_function(response):
            self.assertIsNotNone(response)
            self.assertEqual(response.data.name, "maneesh")
            self.assertEqual(response.data.full_name, "Maneesh Sahu")
            self.assertEqual(response.data.email, "maneesh.sahu@ssi.samsung.com")

        thread = self.users_api.get_self(callback=callback_function)
        thread.join(10)
        if thread.isAlive():
            self.fail("Request timeout")

    def test_get_user_devices(self):
        response = self.users_api.get_user_devices(user_id=self.user_id)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)


if __name__ == '__main__':
    unittest.main()
