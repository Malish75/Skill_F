from django.urls import path
from  .views import subscribe_me, unsubscribe_me, PostsList, PostDetailView, PostSearchView, PostCreateView,PostUpdateView,PostDeleteView


urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('search/', PostSearchView.as_view(), name='post_search.html'),
    path('add/', PostCreateView.as_view(), name='post_create.html'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/subscribe/', subscribe_me, name='subscribe_me'),
    path('<int:pk>/unsubscribe/', unsubscribe_me, name='unsubscribe_me'),

    ]
