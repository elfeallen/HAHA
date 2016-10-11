# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

import responses
import unittest

from line_bot import (
    LineBotApi
)


class TestLineBotApi(unittest.TestCase):
    def setUp(self):
        self.tested = LineBotApi('channel_secret')

    @responses.activate
    def test_get_profile(self):
        responses.add(
            responses.GET,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/profile/user_id',
            json={
                "displayName": "LINE taro",
                "userId": "Uxxxxxxxxxxxxxx...",
                "pictureUrl": "http://obs.line-apps.com/...",
                "statusMessage": "Hello, LINE!"
            },
            status=200
        )

        profile = self.tested.get_profile('user_id')

        request = responses.calls[0].request
        self.assertEqual(request.method, 'GET')
        self.assertEqual(
            request.url,
            LineBotApi.DEFAULT_API_ENDPOINT + '/v2/bot/profile/user_id'
        )
        self.assertEqual(profile.display_name, 'LINE taro')
        self.assertEqual(profile.user_id, 'Uxxxxxxxxxxxxxx...')
        self.assertEqual(profile.picture_url, 'http://obs.line-apps.com/...')
        self.assertEqual(profile.status_message, 'Hello, LINE!')