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
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    #path('', views.login_view, name='login.html'),
    path('', views.user_login, name='user_login'),
    path('home/', views.index, name='index'),
    path('home/list_articles/', views.list_articles, name='crud_items/list_articles.html'),
    path('home/add_articles/', views.add_article, name='crud_items/add_article.html'),
    path('home/search_articles/', views.search_article, name='search_article'),
    path('home/update_articles/', views.update_article, name='crud_items/update_article.html'),
    path('home/delete_articles/', views.delete_article, name='crud_items/delete_article.html'),
    path('home/list_users/', views.list_users, name='crud_users/list_users.html'),
    path('home/regist_user/', views.regist_user, name='crud_users/regist_user.html'),
    path('home/update_user/', views.update_user, name='crud_users/update_user.html'),
    path('home/delete_user/', views.delete_user, name='crud_users/delete_user.html'),
]
