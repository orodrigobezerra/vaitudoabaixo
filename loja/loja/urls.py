"""
URL configuration for loja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vaitudoabaixo import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('', views.login_view, name='login.html'),
    path('', auth_views.LoginView.as_view(next_page = 'index'), name='user_login'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'user_login'), name='logout'),
    path('home/', views.index, name='index'),
    path('home/list_articles/', views.list_articles, name='list_articles'),
    path('home/add_articles/', views.add_article, name='add_articles'),
    path('home/search_articles/', views.search_article, name='search_articles'),
    path('home/update_articles/', views.update_article, name='update_articles'),
    path('home/delete_articles/', views.delete_article, name='delete_articles'),
    path('home/list_users/', views.list_users, name='list_users'),
    path('home/regist_user/', views.regist_user, name='regist_user'),
    path('home/update_user/', views.update_user, name='update_user'),
    path('home/delete_user/', views.delete_user, name='delete_user'),
    path('export/users/', views.export_users, name='export_users'),
    path('export/articles/', views.export_articles, name='export_articles'),
]
