from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # path('', include('newapp.urls')),
    path('news/', include('newapp.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),

    path('', include('protect.urls')), # перенаправление корневой страницы в приложение protect
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    # path('news/delete/', include('protect.urls'))




    ]
