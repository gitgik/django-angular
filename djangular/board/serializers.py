"""Serializers to encode python objects as json."""
from rest_framework import serializers
from .models import Card, List


class ListSerializer(serializers.ModelSerializer):
    """Autogenerate json based on the list fields."""
    class Meta:
        model = List
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):
    """Autogenerate json based on the card fields"""
    class Meta:
        model = Card
        fields = '__all__'

