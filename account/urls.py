from django.urls import path, include

from account import views

urlpatterns = [
    # users list
    path('users', views.user_list, name='user_list'),
    path('users/', views.user_list, name='user_list'),
]