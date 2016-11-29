"""This file defines the models."""

from django.db import models


class List(models.Model):
    """A list model definition."""
    name = models.CharField(max_length=50)

    def __str__(self):
        return "List {}".format(self.name)


class Card(models.Model):
    """A card model definition."""
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    story_points = models.IntegerField(null=True, blank=True)
    business_value = models.IntegerField(null=True, blank=True)
    list = models.ForeignKey(List, related_name="cards")

    def __str__(self):
        return "Card: {}".format(self.title)
