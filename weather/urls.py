"""weather URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from web.views import *
from web import views

urlpatterns = [
    url('admin/', admin.site.urls),
    path('',index),
    path('bd_write/bd_write.html',bd_list),
    path('index/', index),
    path('indexin/', indexin),
    path('weather/', weather),
    path('register/',register),
    path('web/',include('web.urls',namespace="user")),
    path('login/',login),
    path('bd_list/',bd_list, name='bd_list'),
    path('bd_write/',bd_write),
    path('intro/',intro),
    path('logout/',logout, name='logout'),
    path('',home),
    path('board/', board, name='board'),
    path('edit/<int:pk>', boardEdit, name='edit'),
    path('delete/<int:pk>', boardDelete, name='delete'),
]
