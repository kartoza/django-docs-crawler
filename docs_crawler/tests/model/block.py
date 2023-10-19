# coding=utf-8
__author__ = 'irwan@kartoza.com'
__date__ = '18/10/2023'

from django.test.testcases import TestCase

from docs_crawler.models.page import Block
from docs_crawler.models.preferences import Preferences


class BlockTest(TestCase):
    """Test for Block model."""

    def setUp(self):
        """To setup test."""
        pref = Preferences.preferences()
        pref.documentation_base_url = 'http://main-docs'
        pref.save()

    def test_create(self):
        """Test create."""
        page = Block.objects.create(url='/docs/test/block_1')
        self.assertEqual(page.link, 'http://main-docs/docs/test/block_1')
