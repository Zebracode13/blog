"""blogpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_view
from blog_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^accounts/login/$',  auth_view.LoginView.as_view(), name='login'),
    re_path(r'^accounts/logout/$',  auth_view.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('', include('blog_app.urls', namespace='blog')),
    path('', views.AboutView.as_view(), name="about"),
]
