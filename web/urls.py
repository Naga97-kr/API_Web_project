from django.urls import path
from . import views
from .views import *
app_name = 'user'
urlpatterns =[
    path('', board, name='board'),
    path('register/',views.register, name='register'),
    path('index/login/', views.login, name='login'),
    path('index/logout/', views.logout, name='logout'),
    path('edit/<int:pk>', boardEdit, name='edit'),
    path('delete/<int:pk>', boardDelete, name='delete'),
]