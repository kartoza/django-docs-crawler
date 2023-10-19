# coding=utf-8
__author__ = 'irwan@kartoza.com'
__date__ = '18/10/2023'

from django.test.testcases import TestCase

from docs_crawler.models.page import Page
from docs_crawler.models.preferences import Preferences


class PageTest(TestCase):
    """Test for Page model."""

    def setUp(self):
        """To setup test."""
        pref = Preferences.preferences()
        pref.documentation_base_url = 'http://main-docs'
        pref.save()

    def test_create(self):
        """Test create."""
        page = Page.objects.create(
            name='Page 1', relative_url='/test',
            url='/docs/test', title='Page 1'
        )
        self.assertEqual(page.link, 'http://main-docs/docs/test')

    def test_get_page(self):
        """Test get_page."""
        page_root = Page.objects.create(
            name='Page 1', url='/docs/test', title='Page 1'
        )
        page_1 = Page.objects.create(
            name='Page 2', url='/docs/test', title='Page 1',
            relative_url='/docs_1'
        )
        page_1_1 = Page.objects.create(
            name='Page 3', url='/docs/test', title='Page 1',
            relative_url='/docs_1/detail_1'
        )
        page_1_1_1 = Page.objects.create(
            name='Page 4', url='/docs/test', title='Page 1',
            relative_url='/docs_1/detail_1/sub_1'
        )
        page_1_1_2 = Page.objects.create(
            name='Page 5', url='/docs/test', title='Page 1',
            relative_url='/docs_1/detail_1/sub_2'
        )
        page_2_1 = Page.objects.create(
            name='Page 7', url='/docs/test', title='Page 1',
            relative_url='/docs_2/detail_1#test'
        )
        page_2 = Page.objects.create(
            name='Page 6', url='/docs/test', title='Page 1',
            relative_url='/docs_2'
        )
        self.assertEqual(Page.get_page('/other').id, page_root.id)
        self.assertEqual(Page.get_page('/docs_1/other').id, page_1.id)
        self.assertEqual(Page.get_page('/docs_2/other').id, page_2.id)
        self.assertEqual(
            Page.get_page('/docs_1/detail_1/other').id, page_1_1.id
        )
        self.assertEqual(
            Page.get_page('/docs_1/detail_1/sub_1').id, page_1_1_1.id
        )
        self.assertEqual(
            Page.get_page('/docs_2/detail_1#test').id, page_2_1.id
        )
        self.assertEqual(
            Page.get_page('/docs_1/detail_1/sub_2').id, page_1_1_2.id
        )
