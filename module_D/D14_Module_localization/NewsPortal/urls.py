from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [

    path('i18n/', include('django.conf.urls.i18n')), # подключаем встроенные эндопинты для работы с локализацией
    path('', include('protect.urls')),
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('sign/', include('sign.urls')),
    path('account/', include('allauth.urls')),
    path('news/', include('newapp.urls')),
        ]

# добавление маршрута к медиа - нужно джанге только в ОТЛАДОЧНОМ режиме
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)