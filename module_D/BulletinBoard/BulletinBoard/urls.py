from django.contrib import admin
from django.urls import path, include

from boardapp.views import LoginView, SignupView
# from boardapp.views import LoginView, SignupView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),

    path("account/login/", LoginView.as_view(), name="account_login"),
    path("account/signup/", SignupView.as_view(), name="account_signup"),
    path('account/', include("account.urls")),

    path('', include('boardapp.urls')),

]

