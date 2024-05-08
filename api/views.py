from rest_framework.generics import ListAPIView

from food.models import MenuItem
from food.serializers import MenuItemSerializer


class MenuItemListAPIView(ListAPIView):
    queryset = MenuItem.objects
    serializer_class = MenuItemSerializer
