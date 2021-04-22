from django.urls import path
from .views import ProductsList, ProductDetail  # импортируем наше представление
from simpleapp.views import ProductsList

urlpatterns = [
    path('', ProductsList.as_view()), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', ProductDetail.as_view()),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
]


