from django.urls import path, include
from .views import PostsList, PostDetailView, PostCreateView, PostSearchView, PostUpdateView, PostDeleteView


urlpatterns = [
     path('', PostsList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('add/', PostCreateView.as_view(), name='post_create.html'),
    path('search/', PostSearchView.as_view(), name='post_search.html'),

    # path('news/delete/', include('protect.urls'))
    ]

# расширение не надо указывать, это поле для обращения к этому url в шаблоне,
# а не ссылка на сам шаблон
