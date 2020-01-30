from django.contrib import admin
# from django.conf.urls import include
from django.urls import path, include

from chat.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('chat/', include('chat.urls', namespace='chat')),
]
