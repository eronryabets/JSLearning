from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from food.models import MenuItem, UserRequestInfo
from food.serializers import MenuItemSerializer, UserRequestInfoSerializer


class MenuAPIView(APIView):
    def get(self, request, format=None):
        queryset = MenuItem.objects.all()
        serializer = MenuItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRequestInfoAPIView(APIView):
    def get(self, request, format=None):
        queryset = UserRequestInfo.objects.all()
        serializer = UserRequestInfoSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserRequestInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
