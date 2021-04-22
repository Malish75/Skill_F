from django.urls import path
from .views import ProductsList, ProductCreateView,ProductDetailView, \
    ProductUpdateView, ProductDeleteView# импортируем наше представление
from simpleapp.views import ProductsList

urlpatterns = [
    path('', ProductsList.as_view()), # т.к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Ссылка на детали товара
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('/<int:pk>', ProductUpdateView.as_view(), name='product_update'),

    ]