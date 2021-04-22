
from django.contrib import admin
from django.urls import path, include
from simpleapp.views import ProductsList #  если писать вьюхи вручную

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('products/', include('simpleapp.urls')), #автоподключение адресов и simpleapp
    #path('products/', ProductsList.as_view()), # Это если каждую вьюху прописывать вручную
    # делаем так, чтобы все адреса из нашего приложения (simpleapp/urls.py) сами автоматически подключались когда мы их добавим.
]
