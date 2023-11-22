# coding=utf-8
__author__ = 'irwan@kartoza.com'
__date__ = '22/08/2023'

from docs_crawler.models.block import Block, BlockChild
from docs_crawler.models.page import Page
from rest_framework import serializers


class BlockSerializer(serializers.ModelSerializer):
    """Block serializer."""

    blocks = serializers.SerializerMethodField()

    def get_blocks(self, obj: Block):
        """Return blocks."""
        blocks = []
        for block_child in BlockChild.objects.filter(
                parent=obj).order_by('order'):
            blocks.append(block_child.child)
        return BlockSerializer(blocks, many=True).data

    class Meta:  # noqa: D106
        model = Block
        fields = (
            'title', 'description', 'thumbnail', 'anchor', 'link', 'blocks'
        )


class PageSerializer(serializers.ModelSerializer):
    """Page serializer."""

    blocks = serializers.SerializerMethodField()
    autogenerate_block = serializers.SerializerMethodField()

    def get_blocks(self, obj: Page):
        """Return blocks."""
        blocks = []
        if not obj.autogenerate_block:
            for page_block in obj.pageblock_set.all().order_by('order'):
                blocks.append(page_block.block)
        return BlockSerializer(blocks, many=True).data

    def get_autogenerate_block(self, obj: Page):
        """Return blocks."""
        return obj.autogenerate_block

    class Meta:  # noqa: D106
        model = Page
        fields = (
            'title', 'intro', 'link', 'blocks', 'autogenerate_block'
        )
