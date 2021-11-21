from django.urls import path, include

from group import views

urlpatterns = [
    # introductions list
    path('groups', views.group_list, name='group_list'),
    path('groups/', views.group_list, name='group_list'),

    # introduction item
    #path('groups/<int:userId>', views.introduction, name='introduction'),
]