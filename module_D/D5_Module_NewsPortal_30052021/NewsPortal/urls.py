from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', include('protect.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('newapp.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),


    ]
