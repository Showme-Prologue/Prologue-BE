from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

import random

from .models import Introduction, IntroductionComponent, IntroductionQuestion
from .serializers import IntroductionSerializer, IntroductionComponentSerializer, IntroductionQuestionSerializer

# Create your views here.

class IntroductionListViewSet(ModelViewSet):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer

class IntroductionComponentListViewSet(ModelViewSet):
    queryset = IntroductionComponent.objects.all()
    serializer_class = IntroductionComponentSerializer

class IntroductionQuestionListViewSet(ModelViewSet):
    queryset = IntroductionQuestion.objects.all()
    serializer_class = IntroductionQuestionSerializer