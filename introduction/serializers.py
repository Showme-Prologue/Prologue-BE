from rest_framework import serializers

from .models import Introduction, IntroductionComponent, IntroductionQuestion

class IntroductionQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntroductionQuestion
        fields = '__all__'

class IntroductionComponentSerializer(serializers.ModelSerializer):
    questions = IntroductionQuestionSerializer(many=True, read_only=True)
    class Meta:
        model = IntroductionComponent
        #fields = '__all__'
        fields = ('question_order', 'questions', 'question_id', 'answer')
        depth = 1

class IntroductionSerializer(serializers.ModelSerializer):
    components = IntroductionComponentSerializer(many=True, read_only=True)
    image = serializers.ImageField(use_url=True)
    class Meta:
        model = Introduction
        fields = '__all__'