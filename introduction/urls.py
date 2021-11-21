from django.urls import path, include

from introduction import views

urlpatterns = [
    # introductions list
    path('introductions', views.introduction_list, name='introduction_list'),
    path('introductions/', views.introduction_list, name='introduction_list'),

    # introduction item
    path('introductions/<int:userId>', views.introduction, name='introduction'),
]