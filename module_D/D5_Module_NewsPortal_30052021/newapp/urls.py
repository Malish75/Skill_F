from django.urls import path
from .views import PostsList, PostDetailView,\
    PostCreateView, PostSearchView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add/', PostCreateView.as_view(), name='post_create.html'),
    path('search/', PostSearchView.as_view(), name='post_search.html'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),


    # path('sign/upgrade/', RedirectView.as_view(url='')), #3


    # path('accounts/', include('allauth.urls'))


    ]

# расширение не надо указывать, это поле для обращения к этому url в шаблоне,
# а не ссылка на сам шаблон
