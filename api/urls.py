from django.urls import path

from api.views import MenuItemListAPIView

app_name = 'api'

urlpatterns = [
    path('menu-item-list/', MenuItemListAPIView.as_view(), name='menu-item-list')
]
