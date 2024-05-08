from rest_framework import serializers

from food.models import MenuItem, UserRequestInfo


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('img', 'altimg', 'title', 'descr', 'price')


class UserRequestInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequestInfo
        fields = ('name', 'phone', 'id')
