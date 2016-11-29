"""Serializers."""
from rest_framework import serializers
from .models import Card, List


class ListSerializer(serializers.ModelSerializer):
    """Serializer to change List fields to Json"""
    class Meta:
        model = List


class CardSerializer(serializers.ModelSerializer):
    """Serializer to change Card fields to Json"""
    class Meta:
        model = Card