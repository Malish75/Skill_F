from django.urls import path
from .views import PostsList, PostDetailView, PostSearchView, PostCreateView,\
    PostUpdateView,PostDeleteView, Subscriber #, IndexView # test_mail
from django.urls import path
from django.views.decorators.cache import cache_page
from .views import set_timezone



urlpatterns = [
    # path('', cache_page(60*1)(PostsList.as_view())),                                     # добавим кэширование на главную страницу
    # path('<int:pk>/', cache_page(60*5)(PostDetailView.as_view()), name='post_detail'), # добавим кэширование на детали товара. Раз в 5 минут товар будет записываться в кэш для экономии ресурсов.
    path('', PostsList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', PostSearchView.as_view(), name='post_search.html'),
    path('add/', PostCreateView.as_view(), name='post_create.html'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('category/<int:pk>/subscribe/', Subscriber.as_view(), name='subscribe'),
    path('set_timezone', set_timezone, name = 'set_timezone'),



    ]
