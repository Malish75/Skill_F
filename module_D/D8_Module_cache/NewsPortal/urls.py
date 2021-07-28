from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('protect.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('sign/', include('sign.urls')),
    path('account/', include('allauth.urls')),
    path('news/', include('newapp.urls')),

        ]