from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

import random

from .models import User
from .serializers import UserSerializer

@api_view(['GET'])
def user_list(request):
    if request.method == 'POST':
        pass
    else:
        users = User.objects.all()
        user_list_serializers = UserSerializer(users, many=True)
        return Response(user_list_serializers.data)