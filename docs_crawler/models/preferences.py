# coding=utf-8
__author__ = 'irwan@kartoza.com'
__date__ = '13/06/2023'

from django.db import models

from .singleton import SingletonModel


class Preferences(SingletonModel):
    """Preference settings specifically for Documentation."""

    documentation_base_url = models.CharField(
        max_length=512,
        default='https://documentation'
    )

    class Meta:  # noqa: D106
        verbose_name_plural = "preferences"

    @staticmethod
    def preferences() -> "Preferences":
        """Load Site Preference."""
        return Preferences.load()

    def __str__(self):
        return 'Preferences'
