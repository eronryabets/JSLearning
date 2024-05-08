from rest_framework import serializers

from food.models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('img', 'altimg', 'title', 'descr', 'price')
