from django.urls import path

from api.views import MenuAPIView

app_name = 'api'

urlpatterns = [
    path('menu/', MenuAPIView.as_view(), name='menu')
]
