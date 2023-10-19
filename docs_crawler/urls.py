# coding=utf-8
__author__ = 'irwan@kartoza.com'
__date__ = '22/08/2023'

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import re_path

from docs_crawler.api.documentation import DocumentationDetail
from docs_crawler.models.preferences import Preferences

admin.autodiscover()


def preferences(request):
    """Redirect preference to the change page."""
    Preferences.load()
    return redirect('/admin/docs_crawler/preferences/1/change/')


urlpatterns = [
    re_path(
        r'^admin/docs_crawler/preferences/$',
        preferences,
        name='docs-crawler-admin-preferences'
    ),
    re_path(
        r'^docs_crawler/data/?$',
        DocumentationDetail.as_view(),
        name='docs-crawler-data'
    ),
]
