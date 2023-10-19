# coding=utf-8
__author__ = 'irwan@kartoza.com'
__date__ = '18/10/2023'

from django.contrib.auth import get_user_model
from django.test.client import Client
from django.test.testcases import TestCase
from django.urls import reverse

from docs_crawler.models.page import Page, Block, PageBlock
from docs_crawler.models.preferences import Preferences

User = get_user_model()


class ApiTest(TestCase):
    """Test for api."""

    def setUp(self):
        """To setup test."""
        pref = Preferences.preferences()
        pref.documentation_base_url = 'http://main-docs'
        pref.save()

    def test_api(self):
        """Test api."""
        page = Page.objects.create(
            name='Page 1', url='/docs/test', title='Page 1'
        )
        block_1 = Block.objects.create(
            url='/docs/test/block_1'
        )
        block_2 = Block.objects.create(
            url='/docs/test/block_2',
            anchor='#Detaiil'
        )
        PageBlock.objects.create(
            page=page,
            block=block_1,
            order=1
        )
        PageBlock.objects.create(
            page=page,
            block=block_2,
            order=2
        )
        client = Client()
        response = client.get(reverse('docs-crawler-data'))
        self.assertEquals(response.status_code, 200)
        output = response.json()
        self.assertEqual(output['title'], 'Page 1')
        self.assertEqual(output['link'], 'http://main-docs/docs/test')
        self.assertEqual(
            output['blocks'][0]['link'], 'http://main-docs/docs/test/block_1'
        )
        self.assertEqual(output['blocks'][0]['anchor'], None)
        self.assertEqual(
            output['blocks'][1]['link'], 'http://main-docs/docs/test/block_2'
        )
        self.assertEqual(output['blocks'][1]['anchor'], '#Detaiil')
