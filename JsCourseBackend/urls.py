from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from food.views import index
from main.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    # path('food/', index, name='index'),
    path('food/', include('food.urls', namespace='food')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
