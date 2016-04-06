# coding: utf-8

"""
Run the Message API tests.
$ pip install nose (optional)
$ cd artikcloud-python
$ nosetests -v
"""

import os
import time
import unittest

import artikcloud
from artikcloud.rest import ApiException

class MessagesApiTests(unittest.TestCase):

    def setUp(self):
        self.api_client = artikcloud.ApiClient()
        self.api_client.set_default_header(header_name="Authorization", header_value="Bearer 1eef3e3251e147d1ac707a57f6779c49")
        self.messages_api = artikcloud.MessagesApi(self.api_client)
        self.setUpModels()

    def tearDown(self):
        # sleep 1 sec between two every 2 tests
        time.sleep(1)

    def setUpModels(self):
        self.message = artikcloud.MessageAction()
        self.message.type = "message"
        self.message.sdid = "993925c3cd994bf7a51c620884be65e9"
        self.message.ts = int(round(time.time() * 1000))
        self.message.data = {'volume': 5}

        # nothing to do
        time.sleep(1)

    def test_send_message(self):
        response = self.messages_api.send_message_action(self.message)
        self.assertIsNotNone(response)
        messageid = response.data.mid
        self.assertIsNotNone(messageid)

        # get normalized message from mid
        time.sleep(2)
        envelope = self.messages_api.get_normalized_messages(mid=messageid)
        self.assertIsNotNone(envelope)
        self.assertEqual(envelope.size, 1)

        normalized = envelope.data[0]
        self.assertIsNotNone(normalized)
        self.assertEqual(normalized.mid, messageid)

        volume = normalized.data['volume']
        self.assertIsNotNone(volume)
        self.assertEqual(volume, 5.0)

if __name__ == '__main__':
    unittest.main()
