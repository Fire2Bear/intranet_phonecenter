# coding: UTF-8
from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path("hello/", views.hello, name="hello"),
    path(r'register/', views.register, name="register"),
    path(r'login/', views.login_view, name="login"),
    path(r'logout/', views.logout_view, name="logout"),
    path(r'myaccount/', views.myaccount, name="myaccount"),
    path('account-settings/', views.account_settings, name="account_settings"),

]
