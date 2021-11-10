from django.urls import path
from . import views
from .views import PostList, PostDetail

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', views.create, name='create'),

]


