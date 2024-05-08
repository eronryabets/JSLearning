from django.urls import path

from api.views import MenuAPIView, UserRequestInfoAPIView

app_name = 'api'

urlpatterns = [
    path('menu/', MenuAPIView.as_view(), name='menu'),
    path('requests/', UserRequestInfoAPIView.as_view(), name='requests'),
]
