from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import MenuItem
from food.serializers import MenuItemSerializer


class MenuAPIView(APIView):
    def get(self, request, format=None):
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response({"menu": serializer.data})
