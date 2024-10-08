from django.contrib import admin
from django.urls import path, include
from base import urls as base_urls
from django.contrib.auth import views as auth_views 




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(base_urls)),
    path('accounts/', include('django.contrib.auth.urls'))
]
