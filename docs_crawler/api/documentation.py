# coding=utf-8
__author__ = 'irwan@kartoza.com'
__date__ = '22/08/2023'

from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from docs_crawler.models.page import Page
from docs_crawler.serializer.page import PageSerializer


class DocumentationDetail(APIView):
    """Documentation detail."""

    def get(self, request, *args, **kwargs):
        """Get documentation detail."""
        relative_url = request.GET.get('relative_url', '')
        page = Page.get_page(relative_url)
        if not page:
            raise Http404
        return Response(PageSerializer(page).data)
