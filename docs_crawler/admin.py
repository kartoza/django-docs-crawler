# coding=utf-8
__author__ = 'irwan@kartoza.com'
__date__ = '22/08/2023'

from django.contrib import admin

from docs_crawler.models import (
    Preferences, Block, Page, PageBlock, BlockChild
)


@admin.register(Preferences)
class PreferencesAdmin(admin.ModelAdmin):
    """Documentation preferences admin."""

    fieldsets = (
        (None, {
            'fields': ('documentation_base_url',)
        }),
    )


class PageBlockInline(admin.TabularInline):
    """PageBlock inline."""

    model = PageBlock
    extra = 1


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """Page admin."""

    list_display = ('name', 'relative_url')
    inlines = (PageBlockInline,)


class BlockChildInline(admin.TabularInline):
    """BlockChild inline."""

    fk_name = "parent"
    model = BlockChild
    extra = 1


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    """Block admin."""

    list_filter = ('url', 'anchor')
    inlines = (BlockChildInline,)
