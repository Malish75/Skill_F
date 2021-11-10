from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('boardapp.urls'),),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/profile/', include('boardapp.urls'),)
]
