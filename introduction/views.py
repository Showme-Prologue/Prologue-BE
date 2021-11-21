from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

import random

from .models import Introduction, IntroductionComponent, IntroductionQuestion
from account.models import User
from .serializers import IntroductionSerializer, IntroductionComponentSerializer, IntroductionQuestionSerializer

# Create your views here.

# class IntroductionListViewSet(ModelViewSet):
#     queryset = Introduction.objects.all()
#     serializer_class = IntroductionSerializer

# class IntroductionComponentListViewSet(ModelViewSet):
#     queryset = IntroductionComponent.objects.order_by('sequence')
#     serializer_class = IntroductionComponentSerializer

# class IntroductionQuestionListViewSet(ModelViewSet):
#     queryset = IntroductionQuestion.objects.all()
#     serializer_class = IntroductionQuestionSerializer

@api_view(['GET'])
def introduction_list(request):
    if request.method == 'POST':
        pass
    else:
        introductions = Introduction.objects.filter(groupCode=request.GET.get('groupCode'))
        introduction_list_serializers = IntroductionSerializer(introductions, many=True)
        return Response(introduction_list_serializers.data)

@api_view(['GET'])
def introduction(request, userId):
    user = get_object_or_404(User, pk=userId)
    introduction = Introduction.objects.get(userId=user)
    introduction_serializer = IntroductionSerializer(introduction)
    return Response(introduction_serializer.data)