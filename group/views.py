from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Group
from .serializers import GroupSerializer

@api_view(['GET'])
def group_list(request):
    if request.method == 'POST':
        pass
    else:
        groups = Group.objects.all()
        group_list_serializers = GroupSerializer(groups, many=True)
        return Response(group_list_serializers.data)

# @api_view(['GET'])
# def group(request, userId):
#     user = get_object_or_404(User, pk=userId)
#     introduction = Introduction.objects.get(userId=user)
#     introduction_serializer = IntroductionSerializer(introduction)
#     return Response(introduction_serializer.data)