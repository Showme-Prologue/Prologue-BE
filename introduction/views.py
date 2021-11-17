from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

import random

from .models import Introduction, IntroductionComponent, IntroductionQuestion
from .serializers import IntroductionListSerializer, IntroductionComponentSerializer, IntroductionQuestionSerializer

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
        introductions = Introduction.objects.filter(group_code=request.GET.get('groupCode'))
        introduction_list_serializers = IntroductionListSerializer(introductions, many=True)
        return Response(introduction_list_serializers.data)