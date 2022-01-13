from django.urls import path, include
from . import views
from .views import PostList, PostDetailView, PostCreate, PostUpdate, PostDelete
# from account.views import LogoutView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('update_page/<int:pk>/', views.PostUpdate.as_view(), name='update_page'),
    path('delete_page/<int:pk>/', views.PostDelete.as_view(), name='delete_page'),


]


