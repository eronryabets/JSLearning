from django.urls import path

from food.views import index

app_name = 'food'

urlpatterns = [
    path('', index, name='index'),
]
