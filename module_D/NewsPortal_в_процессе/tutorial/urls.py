
from django.contrib import admin
from django.urls import path, include
from newapp.views import PostsList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('newapp.urls')), #  PostsView
    ]
