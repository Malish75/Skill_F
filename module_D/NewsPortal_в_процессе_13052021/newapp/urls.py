from django.urls import path
from .views import PostsList, PostDetailView,\
    PostCreateView, PostSearchView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create.html'),
    path('search/', PostSearchView.as_view(), name='post_search.html'),


    path('/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),

    ]

# расширение не надо указывать, это поле для обращения к этому url в шаблоне,
# а не ссылка на сам шаблон
#
# path('/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
#     path('/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
